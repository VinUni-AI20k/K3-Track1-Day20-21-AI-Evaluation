"""Code checks — kiểm tra results.jsonl bằng rule thuần Python (không tốn API).

Đây là làn "Code check" của bài lab: những tiêu chí viết được thành rule thì kiểm
bằng code — nhanh, rẻ, khách quan, chạy lại bao nhiêu lần cũng được.

Chạy:  python3 eval/code_checks.py            # in bảng pass/fail từng check từng row
Mở rộng: thêm hàm check_* mới của riêng nhóm (xem 3 hàm mẫu dưới).
"""
import json
import os
import re
import sys
from pathlib import Path

# tutor.py nằm ở tutor/ (khu vực sản phẩm) — thêm vào sys.path để import được
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))

import tutor  # dùng lại load_corpus

EXPECTED_FIELDS = {"scope", "answer", "sources", "followup_questions"}


def check_schema(rec):
    """Output parse được và đủ 4 field đúng contract."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return False, "JSON không parse được (xem raw_content)"
    missing = EXPECTED_FIELDS - set(out)
    if missing:
        return False, "thiếu field: " + ", ".join(sorted(missing))
    return True, None


def check_citation_exists(rec, valid_ids):
    """Mọi doc_id/section_id trong sources phải tồn tại thật trong corpus."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        key = (s.get("doc_id"), s.get("section_id"))
        if key not in valid_ids:
            return False, f'nguồn không tồn tại: {key[0]}#{key[1]}'
    return True, None


def _token_subsequence(needle, haystack):
    """True nếu chuỗi token của needle xuất hiện liên tiếp trong haystack."""
    if not needle:
        return True
    n = len(needle)
    return any(haystack[i:i + n] == needle for i in range(len(haystack) - n + 1))


def check_quote_verbatim(rec, section_tokens):
    """Quote phải truy được về section đã cite — so theo chuỗi token (bỏ dấu, lowercase,
    bỏ mọi dấu câu/khoảng trắng) nên khác biệt gạch ngang/ngoặc kép không tính là sai.

    Rule v2 (sửa sau khi đối chiếu với nhãn tay ở Phase 4): dấu lược "..." KHÔNG còn bị
    tính là fail nếu MỌI mảnh hai bên dấu lược đều nằm trong đúng section đã cite.
    Lý do: v1 gộp chung ba mức nghiêm trọng rất khác nhau — bịa nguyên câu trích (6 ca),
    cite sai địa chỉ section (1 ca) và lược trích đúng thông lệ (5 ca). Chỉ hai loại đầu
    mới là lỗi groundedness; loại thứ ba là cách trích dẫn hợp lệ.
    Ai muốn siết nguyên văn tuyệt đối thì đặt QUOTE_STRICT=1."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    strict = os.environ.get("QUOTE_STRICT") == "1"
    for s in out.get("sources") or []:
        tokens = section_tokens.get((s.get("doc_id"), s.get("section_id")), [])
        quote = s.get("quote") or ""
        pieces = [quote] if strict else [p for p in quote.replace("…", "...").split("...") if p.strip()]
        for piece in pieces:
            pt = tutor.tokens(piece)
            if pt and not _token_subsequence(pt, tokens):
                return False, f'quote không truy được về section {s.get("section_id")}: "{piece.strip()[:40]}..."'
    return True, None


def check_scope_contract(rec):
    """C5 (phần cứng): out_of_scope thì sources PHẢI rỗng; in_scope thì PHẢI có ≥1 nguồn.

    Đây là ràng buộc contract viết được thành rule — phần "câu này corpus có phủ không"
    mới cần judge. Tách ra để judge khỏi phải chấm thứ code kiểm được."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    scope = out.get("scope")
    n = len(out.get("sources") or [])
    if scope == "out_of_scope" and n > 0:
        return False, f"out_of_scope nhưng vẫn trích {n} nguồn"
    if scope == "in_scope" and n == 0:
        return False, "in_scope nhưng sources rỗng"
    if scope not in ("in_scope", "out_of_scope"):
        return False, f"scope không hợp lệ: {scope!r}"
    return True, None


def check_followup_count(rec):
    """C7 (phần đếm được): đúng 3 câu follow-up, không rỗng, không trùng nhau.

    Chất lượng dẫn dắt thì để judge; còn "đủ 3 câu và không lặp" là việc của code."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    fu = out.get("followup_questions") or []
    if len(fu) != 3:
        return False, f"có {len(fu)} câu follow-up, cần đúng 3"
    if any(not str(q).strip() for q in fu):
        return False, "có câu follow-up rỗng"
    if len({str(q).strip().lower() for q in fu}) < 3:
        return False, "có câu follow-up trùng nhau"
    return True, None


CHECKS = [  # thêm check của nhóm vào đây
    ("schema_valid", check_schema),
    ("citation_exists", check_citation_exists),
    ("quote_verbatim", check_quote_verbatim),
    ("scope_contract", check_scope_contract),      # nhóm thêm — C5 phần cứng
    ("followup_count", check_followup_count),      # nhóm thêm — C7 phần đếm
]


def main(path="results.jsonl"):
    if not os.path.exists(path):
        raise SystemExit("Không thấy %s — chạy python3 eval/run_eval.py trước." % path)
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]

    sections = tutor.load_corpus()
    valid_ids = {(s["doc_id"], s["section_id"]) for s in sections}
    section_tokens = {(s["doc_id"], s["section_id"]): tutor.tokens(s["text"]) for s in sections}

    totals = {name: [0, 0] for name, _ in CHECKS}  # [pass, fail] (skip không đếm)
    for rec in rows:
        sid = rec.get("scenario_id", "?")
        line = [sid]
        for name, fn in CHECKS:
            if fn in (check_schema, check_scope_contract, check_followup_count):
                ok, reason = fn(rec)
            elif fn is check_citation_exists:
                ok, reason = fn(rec, valid_ids)
            else:
                ok, reason = fn(rec, section_tokens)
            if ok is None:
                line.append(f"{name}: skip")
                continue
            totals[name][0 if ok else 1] += 1
            line.append(f"{name}: {'pass' if ok else 'FAIL — ' + str(reason)}")
        print(" | ".join(line))

    print("\nTổng kết:")
    for name, (p, f) in totals.items():
        print(f"  {name}: {p} pass / {f} fail")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "results.jsonl")
