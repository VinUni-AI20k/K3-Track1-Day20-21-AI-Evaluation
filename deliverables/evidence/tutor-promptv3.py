"""Tutor AI20K bản chạy local: vòng tool-calling y hệt platform.

Model nhận tool kb_search (BM25 local trên corpus/), TỰ quyết định gọi bao nhiêu
lần với truy vấn nào, rồi trả JSON theo contract — giống hệt cơ chế agentic của
platform, chỉ khác môi trường chạy (Python local thay vì Next.js).

Dùng trực tiếp trong REPL:  python3 -i tutor/tutor.py  ->  ask_tutor("câu hỏi")
Hoặc được run_eval.py import để chạy cả dataset.
"""
import json, math, os, re, time, unicodedata

import requests

# --- System prompt THẬT của tutor, copy nguyên văn từ platform
# (platform/src/lib/platform/constants.ts, biến DEFAULT_SYSTEM_PROMPT)
SYSTEM_PROMPT = """Bạn là AI Tutor của khoá học AI20K — một trợ giảng chuyên về chủ đề đánh giá hệ thống AI (AI evaluations). Nhiệm vụ của bạn là trả lời câu hỏi của học viên CHỈ dựa trên corpus bài học được cung cấp qua tool kb_search. Tuyệt đối không bịa thông tin, không bịa nguồn, không trích dẫn từ trí nhớ của model.

Corpus bài học gồm các tài liệu sau, được địa chỉ hoá theo quy ước doc_id#section_id:
- doc_id "hamel-evals": bài blog "Your AI Product Needs Evals" (Hamel Husain) — section_id là slug của tiêu đề mục, ví dụ "level-1-unit-tests", "evaluating-rag".
- doc_id "anthropic-demystifying-evals": bài blog "Demystifying evals for AI agents" (Anthropic Engineering) — section_id là slug của tiêu đề mục, ví dụ "types-of-graders-for-agents".
- doc_id "chip-huyen-ch4": chương 4 "Evaluate AI Systems" trong sách AI Engineering (Chip Huyen) — section_id là slug của tiêu đề mục, ví dụ "design-your-evaluation-pipeline".
- doc_id "slide-day19-20": slide bài giảng Day 19–20 về AI Evaluation — section_id là mã slide dạng "sNN", ví dụ "s40", "s50".
- doc_id "ai-evals-m01" đến "ai-evals-m14": 14 module của một khoá học về AI evaluations (tài liệu tham chiếu bổ sung, tiếng Anh) — section_id là slug của tiêu đề mục trong module.

Quy trình bắt buộc cho mỗi lượt trả lời:

1. Luôn gọi kb_search TRƯỚC KHI trả lời (trừ khi câu hỏi rõ ràng ngoài phạm vi corpus). Có thể gọi nhiều lần với các truy vấn khác nhau nếu kết quả đầu chưa đủ.
2. Chỉ trả lời dựa trên nội dung kb_search trả về trong lượt hiện tại. Nếu corpus không có section nào THỰC SỰ nói về chủ đề được hỏi, xem đó là câu hỏi out_of_scope. Việc kb_search trả về vài section chỉ nhắc thoáng qua từ khoá KHÔNG có nghĩa là corpus phủ được câu hỏi — khi đó vẫn là out_of_scope.

2b. TRƯỚC KHI trả lời, kiểm tra câu hỏi có đủ nghĩa để trả lời không. Nếu rơi vào một trong các trường hợp sau thì scope = "needs_clarification":
- Câu hỏi chứa đại từ/chỉ định không có tiền đề trong chính câu đó: "nó", "cái đó với cái kia", "cái phần đó", "bước ngay sau", "cái trước với cái sau" — mà không có gì trong câu hỏi hay slide context xác định được chúng trỏ vào đâu.
- Câu hỏi không có nội dung cụ thể: "em nên làm sao ạ", "eval này ổn chưa anh".
- Câu hỏi yêu cầu áp dụng vào tình huống riêng của học viên ("case của em", "dự án em") mà không mô tả tình huống đó.
- Câu hỏi dựa trên tiền đề có thể sai (hỏi "2 bước đầu" trong khi quy trình chỉ có 3 bước).
TUYỆT ĐỐI KHÔNG tự đoán học viên đang muốn hỏi gì rồi trả lời thay. Đoán sai làm học viên hiểu nhầm còn tai hại hơn là hỏi lại.
3. Trích nguồn nghiêm ngặt:
- Mỗi nguồn trong "sources" phải gồm "doc_id" (một trong 4 doc_id ở trên), "section_id" (slug mục hoặc mã slide), và "quote" là một đoạn trích NGUYÊN VĂN ngắn (tối đa ~40 từ) từ kết quả kb_search.
- "quote" phải là MỘT đoạn LIỀN MẠCH, copy y nguyên từ kb_search. CẤM dùng dấu lược "..." để ghép hai đoạn rời thành một quote. Cần trích hai chỗ thì tạo hai phần tử sources riêng.
- MỌI con số, tỉ lệ, ngưỡng hay khoảng giá trị xuất hiện trong "answer" đều PHẢI có mặt nguyên văn trong ít nhất một "quote". Không có trong quote thì không được viết ra, kể cả khi bạn nhớ là tài liệu có nói.
- Không được đổi chiều ý của nguồn: nguồn nói "X là mức tối thiểu" thì không được viết thành "X là mức hợp lý" hay "khoảng X là đủ".
- Không được lấy con số của một sản phẩm/ví dụ này gán cho tình huống khác của học viên.
- Không suy diễn section_id nếu không chắc — chỉ dùng section rõ ràng chứa đoạn quote.
- Không liệt kê nguồn mà bạn không thực sự dùng trong câu trả lời.
4. Phong cách trợ giảng:
- Trả lời bằng tiếng Việt, rõ ràng, súc tích, đúng vai trò giảng dạy cho học viên PM/PO.
- ĐỘ DÀI: "answer" tối đa 200 từ. Với scope "needs_clarification" thì tối đa 60 từ. Tối đa 3 nguồn trong "sources". Viết dài hơn sẽ làm output bị cắt giữa chừng và hỏng JSON — ngắn gọn là một yêu cầu kỹ thuật, không phải gợi ý văn phong.
- Giải thích vừa đủ để học viên hiểu bản chất, có thể kèm ví dụ nhỏ lấy từ corpus.
- "followup_questions" phải gồm đúng 3 câu hỏi gợi mở giúp học viên đào sâu nội dung bài học (ví dụ: so sánh khái niệm, áp dụng vào tình huống, mở rộng sang mục liên quan). Không hỏi xã giao, không hỏi lệch chủ đề.

Output contract — bắt buộc:
- Câu trả lời cuối cùng của bạn phải là MỘT object JSON hợp lệ duy nhất, không bọc trong markdown fence, không có text nào khác.
- Cấu trúc:
{
  "scope": "in_scope" | "out_of_scope" | "needs_clarification",
  "answer": string,
  "sources": [{ "doc_id": string, "section_id": string, "quote": string }],
  "followup_questions": [string, string, string]
}
- Với câu hỏi trong phạm vi: "scope" = "in_scope", "sources" có ít nhất 1 nguồn, "followup_questions" có đúng 3 câu.
- Với câu hỏi ngoài phạm vi corpus: "scope" = "out_of_scope", "sources" = [], trong "answer" hãy từ chối khéo léo và gợi ý 1-2 chủ đề liên quan có trong corpus, "followup_questions" vẫn gồm 3 câu hỏi dẫn học viên quay lại nội dung bài học.
- Với câu hỏi chưa đủ rõ (mục 2b): "scope" = "needs_clarification", "sources" = [], và "answer" PHẢI là một câu hỏi lại ngắn gọn, kết thúc bằng dấu "?", nêu đúng chỗ đang thiếu (vd: "Bạn đang so sánh hai phương pháp nào ạ — code-based eval và LLM-as-judge, hay hai giai đoạn trong lifecycle?"). Không kèm bài giảng dài trước khi hỏi. "followup_questions" gồm 3 câu giúp học viên diễn đạt lại nhu cầu cho rõ.
- Học viên xin đáp án bài tập: KHÔNG đưa đáp án trực tiếp, kể cả khi corpus có nội dung đó. Trả "scope" = "out_of_scope", "sources" = [], và trong "answer" giải thích ngắn vì sao bạn không đưa đáp án, rồi chỉ hướng tự làm.

Lưu ý:
- Chỉ trả lời câu hỏi mới nhất của người dùng.
- Không tiết lộ chi tiết hạ tầng (tên file, đường dẫn nội bộ, API key...); khi nói về nguồn, dùng doc_id/section_id.
- Nếu tool kb_search trả về lỗi hoặc không có kết quả, hãy nói rõ trong "answer" thay vì phỏng đoán.
"""

# --- Cấu hình: đọc từ env hoặc file .env (ở ROOT repo), KHÔNG hardcode key
# BASE_DIR = thư mục tutor/ (corpus/ nằm cùng); ROOT_DIR = root repo (.env ở đó).
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

def load_dotenv(path=os.path.join(ROOT_DIR, ".env")):
    """Nạp biến môi trường từ file .env đơn giản (KEY=VALUE mỗi dòng).
    Ghi đè cả biến đã có trong shell — .env của repo phải thắng, nếu không một
    OPENAI_API_KEY global (vd export trong ~/.zshrc) sẽ lấn key gateway."""
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip().strip('"').strip("'")

load_dotenv()  # nạp .env TRƯỚC khi đọc các hằng số cấu hình bên dưới

# --- Providers: gọi TRỰC TIẾP API chuẩn của từng hãng (OpenAI-compatible).
# Đặt key theo family trong .env — ví dụ model "openai/gpt-4o-mini" cần OPENAI_API_KEY.
# Vẫn dùng được gateway riêng (LiteLLM...) nếu đặt EVAL_BASE_URL — khi đó model id
# giữ nguyên nguyên chuỗi (vd "deepseek/deepseek-v4-flash") và key lấy từ EVAL_API_KEY.
PROVIDERS = {
    "openai":     ("OPENAI_API_KEY", "https://api.openai.com/v1"),
    "deepseek":   ("DEEPSEEK_API_KEY", "https://api.deepseek.com/v1"),
    "anthropic":  ("ANTHROPIC_API_KEY", "https://api.anthropic.com/v1"),
    "gemini":     ("GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/openai"),
    "openrouter": ("OPENROUTER_API_KEY", "https://openrouter.ai/api/v1"),
}

BASE_URL = os.environ.get("EVAL_BASE_URL")  # None = gọi thẳng provider
MODEL = os.environ.get("EVAL_MODEL", "deepseek/deepseek-v4-flash")

def resolve_provider(model):
    """-> (base_url, api_key, model_id_thật). Gateway nếu EVAL_BASE_URL được đặt."""
    if BASE_URL:
        key = os.environ.get("EVAL_API_KEY") or get_api_key(model)
        return BASE_URL, key, model
    family = model.split("/")[0] if "/" in model else "openai"
    if family not in PROVIDERS:
        raise RuntimeError(
            f"Không biết provider cho model {model}. Các provider hỗ trợ: "
            + ", ".join(PROVIDERS)
            + " — hoặc đặt EVAL_BASE_URL trỏ về gateway OpenAI-compatible của bạn.")
    env_name, base = PROVIDERS[family]
    return base, os.environ.get(env_name), model[len(family) + 1:]

def get_api_key(model=MODEL):
    """Key theo family của model (openai/gpt-... -> OPENAI_API_KEY...)."""
    family = model.split("/")[0] if "/" in model else "openai"
    env_name = PROVIDERS.get(family, (f"{family.upper()}_API_KEY", None))[0]
    return os.environ.get(env_name) or os.environ.get("OPENAI_API_KEY")

# --- Xử lý text: bỏ dấu tiếng Việt + lowercase để so từ khoá ổn định
def normalize(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.replace("đ", "d")

def tokens(text):
    return re.findall(r"[a-z0-9]+", normalize(text))

# Từ nối phổ biến (VI + EN) không mang nghĩa tìm kiếm — loại khỏi câu hỏi khi chấm điểm
STOPWORDS = set("""la gi the nao va cua cho trong co duoc nhu voi mot cac nay do khong
sao tai vi den khi thi o ve ra se da dang bi boi tu nhung hon nhat nen can phai muon
hay hoac roi ai bao nhieu lam theo cung minh ban a oi nhe duoc khong
danh gia gom buoc cau hoi tra loi nguoi thay tro
the a an as is are was were of to in on for and or with what why how which when do
does it this that be by at from we you i he she they them his her its our your my me
""".split())

def slugify(heading):
    """Heading markdown -> section_id slug (giống manifest của platform)."""
    h = normalize(re.sub(r"[*_`]", "", heading))
    return "-".join(re.findall(r"[a-z0-9]+", h))

# --- Đọc corpus: tách từng doc thành các section theo heading ## / ###
def load_corpus(corpus_dir=os.path.join(BASE_DIR, "corpus")):
    manifest = json.load(open(os.path.join(corpus_dir, "manifest.json"), encoding="utf-8"))
    sections = []
    for doc in manifest["docs"]:
        path = os.path.join(corpus_dir, doc["file"])
        current, buf = None, []
        def flush():
            if current:
                sections.append({"doc_id": doc["doc_id"], "section_id": current,
                                 "text": "\n".join(buf).strip()})
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^#{2,3}\s+(.+)", line)   # bỏ qua # title và frontmatter
            if m:
                flush()
                heading = m.group(1).strip()
                sm = re.match(r"^(s\d{2})", heading)  # slide deck: section_id là mã sNN
                current = sm.group(1) if sm else slugify(heading)
                buf = [heading]
            elif current is not None:
                buf.append(line)
        flush()
    return sections

# --- BM25 đơn giản: chấm điểm section theo độ overlap từ khoá với câu hỏi
def retrieve_corpus(question, top_k=4, sections=None):
    sections = sections if sections is not None else load_corpus()
    docs = [tokens(s["text"]) for s in sections]
    n = len(docs)
    # idf: từ càng hiếm trong corpus càng đáng tin
    df = {}
    for d in docs:
        for t in set(d):
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()}
    avg_len = sum(len(d) for d in docs) / max(n, 1)
    q_tokens = [t for t in set(tokens(question)) if t not in STOPWORDS]
    scored = []
    for s, d in zip(sections, docs):
        tf = {}
        for t in d:
            tf[t] = tf.get(t, 0) + 1
        k1, b = 1.2, 0.75
        norm = 1 - b + b * len(d) / max(avg_len, 1)
        score = sum(idf.get(t, 1) * tf.get(t, 0) * (k1 + 1) / (tf.get(t, 0) + k1 * norm)
                    for t in q_tokens)
        scored.append((score, s))
    scored.sort(key=lambda x: -x[0])
    return [s for score, s in scored[:top_k] if score > 0]

# --- Gọi LLM chat completion (OpenAI-compatible) qua thư viện requests
def chat(messages, model=None, temperature=0, max_tokens=800, tools=None):
    model = model or MODEL
    base_url, key, model_id = resolve_provider(model)
    if not key:
        family = model.split("/")[0] if "/" in model else "openai"
        env_name = PROVIDERS.get(family, (f"{family.upper()}_API_KEY",))[0]
        raise RuntimeError(
            f"Chưa có API key cho model {model}. Đặt {env_name} trong file .env "
            "của thư mục eval-kit rồi chạy lại.\n"
            "(Muốn đi qua gateway riêng? Đặt EVAL_BASE_URL + EVAL_API_KEY.)")
    payload = {"model": model_id, "messages": messages,
               "temperature": temperature, "max_tokens": max_tokens}
    if "deepseek-v4" in model:  # bắt buộc với deepseek v4: tắt thinking, nếu không mất output
        payload["thinking"] = {"type": "disabled"}
        # OpenRouter BỎ QUA cờ "thinking" của deepseek -> reasoning tokens vẫn sinh và
        # ăn hết max_tokens (content=null, finish_reason=length). Cờ tương đương của
        # OpenRouter là "reasoning". Gửi kèm để chạy qua openrouter/* cũng tắt được.
        if model.startswith("openrouter/"):
            payload["reasoning"] = {"enabled": False}
    # ép JSON: đo thực tế ~20% response không có cờ này bị vỡ JSON giữa chừng.
    # Khi có tools, chỉ ép JSON ở vòng trả lời cuối — một số model bỏ tool_calls
    # nếu response_format bật ngay từ vòng đầu. Anthropic (endpoint tương thích
    # OpenAI) không hỗ trợ response_format — bỏ qua, parser đã chịu được fence.
    anthropic = model.startswith("anthropic/")
    if not tools and not anthropic:
        payload["response_format"] = {"type": "json_object"}
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"
    t0 = time.time()
    last_err = None
    for attempt in range(3):  # gateway/provider thỉnh thoảng trả body JSON bị cắt ngang (200 nhưng không parse được) — retry
        resp = requests.post(base_url + "/chat/completions", json=payload, timeout=120,
                             headers={"Authorization": "Bearer " + key})
        resp.raise_for_status()
        try:
            return resp.json(), time.time() - t0
        except ValueError as e:
            last_err = e
            time.sleep(1)
    raise RuntimeError(f"Provider trả body không parse được JSON sau 3 lần thử: {last_err}")

def parse_json_content(content):
    """Model đôi khi bọc JSON trong ``` fence — lột ra trước khi parse.
    JSON vỡ (cắt giữa chừng, sai escape) thì đánh dấu _parse_error thay vì raise.
    strict=False: deepseek hay nhả xuống dòng THẬT (\\n raw) giữa string value —
    JSON chặt không chịu, nhưng nội dung vẫn đọc được nên nới lỏng thay vì fail."""
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        return {"_parse_error": True, "raw": content}
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        try:
            return json.loads(m.group(0), strict=False)
        except json.JSONDecodeError:
            return {"_parse_error": True, "raw": content}

# --- Context slide: học viên hỏi từ một slide cụ thể, prompt phải mang theo
def format_slide_context(slide):
    """Dòng ngữ cảnh slide cho prompt — trả "" nếu câu hỏi không gắn slide."""
    if not slide:
        return ""
    parts = 'slide %s — "%s"' % (slide.get("id", "?"), slide.get("title", ""))
    if slide.get("keyword"):
        parts += ', đang hỏi về từ khoá "%s"' % slide["keyword"]
    return "Ngữ cảnh: học viên đang xem " + parts + ".\n\n"

# --- Tool kb_search: định nghĩa y hệt platform (src/lib/platform/tools.ts),
# --- thực thi bằng BM25 local trên corpus/
KB_SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "kb_search",
        "description": "Search the AI evaluations course corpus (Hamel's evals blog, "
                       "Anthropic's agent evals blog, AI Engineering chapter 4, "
                       "Day 19-20 slide deck). This is the ONLY source the tutor may "
                       "answer from. Results include doc_id for citation.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "default": 5},
            },
            "required": ["query"],
        },
    },
}

def kb_search_local(query, max_results=5, sections=None):
    """Thực thi kb_search local: BM25 trên corpus, trả về cùng shape với platform."""
    max_results = max(1, min(int(max_results or 5), 8))
    hits = retrieve_corpus(query, top_k=max_results, sections=sections)
    return {
        "tool": "kb_search",
        "query": query,
        "max_results": max_results,
        "results": [{"doc_id": h["doc_id"], "section_id": h["section_id"],
                     "text": h["text"]} for h in hits],
        "source_count": len(hits),
    }

# --- Hàm chính: vòng agentic y hệt platform — model TỰ gọi kb_search (có thể
# --- nhiều lần, nhiều truy vấn) rồi mới trả JSON theo contract
def call_tutor(question, slide=None, max_steps=6):
    corpus_sections = load_corpus()
    user = format_slide_context(slide) + "Câu hỏi của học viên: " + question
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user}]
    tool_log, retrieved, usage_total = [], [], {}
    latency_total, finish = 0.0, None

    for step in range(max_steps):
        # Vòng cuối: rút tools đi để ép model trả lời (và ép JSON) dù nó còn muốn gọi
        last_round = step == max_steps - 1
        # 2000 không đủ sau khi system prompt v2 dài ra: đo thực tế completion max
        # 2183 token -> cắt giữa JSON. Nới lên 3000 để truncation không giả dạng
        # thành lỗi chất lượng khi đọc scorecard.
        data, latency = chat(messages, max_tokens=3000,
                             tools=None if last_round else [KB_SEARCH_TOOL])
        latency_total += latency
        u = data.get("usage", {})
        for k, v in u.items():
            if isinstance(v, (int, float)):
                usage_total[k] = usage_total.get(k, 0) + v
        choice = data["choices"][0]
        msg = choice["message"]
        tool_calls = msg.get("tool_calls") or []

        if not tool_calls:  # model trả lời cuối
            finish = choice.get("finish_reason")
            content = msg.get("content") or ""
            out = parse_json_content(content)
            if finish == "length":
                out.setdefault("_truncated", True)
            meta = {"raw_content": content, "usage": usage_total,
                    "latency_s": round(latency_total, 2), "finish_reason": finish,
                    "steps": step + 1, "tool_calls": tool_log, "retrieved": retrieved}
            return out, meta

        # Còn tool calls: thực thi rồi nối kết quả vào hội thoại
        messages.append(msg)
        for tc in tool_calls:
            fn = tc.get("function", {})
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError:
                args = {}
            if fn.get("name") == "kb_search":
                result = kb_search_local(args.get("query", ""),
                                         args.get("max_results", 5),
                                         sections=corpus_sections)
                tool_log.append({"query": result["query"],
                                 "hits": [f'{r["doc_id"]}#{r["section_id"]}'
                                          for r in result["results"]]})
                retrieved.extend({"doc_id": r["doc_id"], "section_id": r["section_id"]}
                                 for r in result["results"])
            else:  # tool lạ: trả lỗi để model tự xử, giống platform
                result = {"tool": fn.get("name"), "error": "unknown tool"}
            messages.append({"role": "tool", "tool_call_id": tc.get("id"),
                             "content": json.dumps(result, ensure_ascii=False)})

    raise RuntimeError("unreachable")  # vòng cuối luôn return hoặc parse_error

def ask_tutor(question):
    """Tiện dùng trong REPL: chỉ trả output theo contract."""
    output, _ = call_tutor(question)
    return output

if __name__ == "__main__":  # demo retrieve không cần API key
    for q in ["LLM-as-a-judge là gì, calibrate judge thế nào?",
              "RAG nên đánh giá ra sao?",
              "hôm nay trời đẹp không?"]:
        print(q, "->", [(s["doc_id"], s["section_id"]) for s in retrieve_corpus(q)])
    print("\n(kb_search local demo)")
    r = kb_search_local("calibration judge", max_results=3)
    print(json.dumps({k: v if k != "results" else [x["doc_id"] + "#" + x["section_id"] for x in v]
                      for k, v in r.items()}, ensure_ascii=False, indent=1))
