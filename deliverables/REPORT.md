# REPORT — Eval loop A→Z: VLearn AI Tutor

Report A→Z của eval loop — mỗi mục ứng một phase của bài lab. Mọi số liệu và quyết
định trong đây phải dẫn được xuống file data thô trong `evidence/` (dataset-v1.jsonl,
results-vN.jsonl, labels.csv, judge-prompt-vN.md, verdicts-vN.jsonl, braintrust-link.md).


---

## 1. Input Grid

> Lưới input = trục "ai hỏi" × "hỏi kiểu gì". LLM giúp sinh input, con người kiểm soát
> coverage. Trả lời các câu hỏi sau rồi vẽ lưới của bạn.

- **AI Tutor phục vụ 4 nhóm người dùng chính:**
  1. *Học viên mới (Beginner Learner):* Bắt đầu tiếp cận AI Evals, cần hiểu khái niệm nền tảng, dễ gặp các ngộ nhận / tiền đề sai về cách hoạt động của LLM.
  2. *Học viên làm bài Capstone (Hands-on Builder):* Đang trực tiếp xây dựng pipeline eval, viết PRD, cần so sánh các kỹ thuật, hỏi cách áp dụng thực tế và có thể có ý định xin đáp án bài tập.
  3. *Học viên xem slide / Ôn tập (Slide Reader):* Đang dừng ở một slide bài giảng cụ thể, thường đặt câu hỏi ngắn, câu hỏi chỉ trỏ (deixis: "cái này", "bảng này") phụ thuộc vào ngữ cảnh slide.
  4. *Người dùng ngoài lề / Tò mò (Casual User):* Đặt các câu hỏi không liên quan đến bài học (tài chính, crypto, du lịch, phần cứng).

- **4 Dimensions & Giá trị phân loại:**
  1. *Question Type (5 values):* `Concept` (Hỏi khái niệm) | `Comparison` (So sánh phương pháp) | `Application` (Áp dụng thực tế) | `Answer-seeking` (Xin đáp án/làm hộ) | `Out-of-scope` (Ngoài phạm vi bài học).
  2. *Corpus Coverage (4 values):* `Full` (Thông tin nằm trọn vẹn trong 1 section/slide) | `Distributed` (Cần tổng hợp từ nhiều docs/sections) | `Partial` (Tài liệu chỉ đề cập 1 phần) | `None` (Không có trong tài liệu).
  3. *Question Clarity (3 values):* `Clear` (Rõ ràng, đủ ngữ cảnh) | `Ambiguous` (Mơ hồ / câu chỉ trỏ cần context slide) | `Multi-intent` (Ghép nhiều câu hỏi cùng lúc).
  4. *User Premise / Assumption (3 values):* `Correct` (Tiền đề đúng chuẩn) | `Incorrect` (Tiền đề sai lệch / ngộ nhận) | `Unsupported` (Tiền đề suy diễn không căn cứ).

- **Ô rủi ro cao nhất & Tần suất cao nhất:**
  - *Tần suất cao nhất:* Ô `Concept × Clear × Correct` và `Application × Clear × Correct` (học viên tra cứu bài học và hỏi cách làm bài thực tế).
  - *Rủi ro cao nhất:* 
    1. Ô `Question with Incorrect Premise` (sc-11, sc-12, sc-13): Nếu Tutor a dua theo tiền đề sai (sycophancy) mà không đính chính, học viên sẽ tiếp thu sai lệch kiến thức nền tảng.
    2. Ô `Answer-seeking` (sc-21, sc-22): Nếu Tutor giải hộ code bài tập capstone, vi phạm nguyên tắc sư phạm và làm mất giá trị học tập.
    3. Ô `Ambiguous / Deixis` (sc-18, sc-19, sc-20): Nếu không bám sát context slide mà tự suy diễn, Tutor sẽ hallucinate hoặc cite sai section.

### Lưới của bạn (User Input Grid)

| Nhóm User \ Question Type | Concept (Khái niệm) | Comparison (So sánh) | Application (Áp dụng) | Answer-seeking (Xin giải) | Out-of-scope (Ngoài lề) |
|---|---|---|---|---|---|
| **Học viên mới** | sc-01, sc-02, sc-03 (test ✓) | sc-05, sc-06 (test ✓) | sc-08 (test ✓) | ▨ Loại (chưa làm bài) | sc-23, sc-24 (test ✓) |
| **Học viên Capstone** | sc-11, sc-14 (test ✓ - bẫy) | sc-04, sc-12 (test ✓) | sc-07, sc-09, sc-10, sc-15, sc-17 (test ✓) | sc-21, sc-22 (test ✓ - chặn) | ▨ Loại (tập trung bài) |
| **Học viên xem slide** | sc-18, sc-20 (test ✓ - deixis) | sc-16 (test ✓ - multi) | sc-13 (test ✓), sc-19 (test ✓ - deixis) | ▨ Loại | ▨ Loại |
| **Người dùng ngoài lề** | ▨ Loại | ▨ Loại | ▨ Loại | ▨ Loại | sc-25 (test ✓) |

---

## 2. Dataset v1

> Dataset là "bộ đề thi" của tutor. Nêu rõ nó phủ những ô nào trong input-grid.

- `dataset.jsonl` gồm **25 câu hỏi**, được thiết kế phủ đều các ô đại diện và ô thử thách trong User Input Grid, loại bỏ hoàn toàn câu trùng lặp (0% overlap).
- **Tỉ lệ phân bổ:**
  - In-scope cốt lõi & tổng hợp (Concept/Comparison/Application): **14 câu (56%)**
  - In-scope bẫy tiền đề sai/suy diễn (Incorrect/Unsupported Premise): **4 câu (16%)**
  - In-scope mơ hồ / deixis gắn slide context: **3 câu (12%)**
  - Out-of-scope & Xin đáp án (Adversarial/Boundary): **4 câu (16%)**
  *Lý do chọn tỉ lệ:* Đảm bảo kiểm tra toàn diện cả 3 năng lực: (1) Trả lời chính xác và trích dẫn chuẩn cho câu hỏi nghiệp vụ; (2) Giữ vững lập trường, đính chính ngộ nhận của học viên; (3) Từ chối đúng mực và bảo vệ ranh giới bài học.
- **Nguồn câu hỏi:** Trích xuất từ các thắc mắc thực tế của học viên qua các khoá, đối chiếu với slide bài giảng Day 19-20 (s05, s06, s08, s10, s15, s18, s20, s21, s25, s29, s40, s48, s51, s60) và các tài liệu chuyên gia (Hamel Husain, Anthropic Evals, Chip Huyen Ch4, Course modules).
- **Review dataset:** Đã chạy kiểm tra tự động và rà soát thủ công: không có câu trùng ý, các câu hỏi deixis đều được gán `metadata.slide` chuẩn xác, kết quả BM25 retrieval offline đều match trúng các section liên quan trong corpus.
- **10 câu nòng cốt (nếu chỉ được giữ 10 câu):**
  1. `sc-01-concept-calib`: Khái niệm cốt lõi về Calibration LLM judge (s51).
  2. `sc-02-concept-tracecode`: Kỹ năng PM cốt lõi về Trace codes và Trace analysis (s29).
  3. `sc-04-compare-code-judge`: Quyết định kiến trúc chọn Code-based vs LLM judge (s40).
  4. `sc-05-compare-eval-test`: Bản chất phân biệt giữa AI Eval và Unit Test truyền thống (s05).
  5. `sc-07-apply-prd-design`: Kỹ năng viết AI-native PRD cho tính năng cụ thể (s21).
  6. `sc-11-premise-100-pass`: Thử thách bẫy tiền đề sai: Ngưỡng pass rate là quyết định sản phẩm (s48).
  7. `sc-13-premise-50-prompts`: Thử thách bẫy ngộ nhận: LLM dataset saturation (s25).
  8. `sc-18-ambiguous-slide-metric`: Thử thách câu hỏi deixis mơ hồ dựa vào context slide (s05).
  9. `sc-21-cheat-capstone-code`: Kiểm tra ranh giới an toàn: Từ chối làm hộ bài tập capstone.
  10. `sc-23-out-crypto-invest`: Kiểm tra ranh giới scope: Từ chối câu hỏi ngoài bài học.
  *Lý do:* 10 câu này kiểm tra trọn vẹn 10 hành vi sản phẩm quan trọng nhất của AI Tutor từ định nghĩa, so sánh, ứng dụng, bẫy ngộ nhận đến ranh giới an toàn.

### Danh sách scenario (bảng tóm tắt 25 scenarios)

| scenario_id | ô trong lưới (Dimension Values) | expected | nguồn câu hỏi / slide context |
|---|---|---|---|
| `sc-01-concept-calib` | Concept · Full · Clear · Correct | in_scope | Slide s51 (Calibration) |
| `sc-02-concept-tracecode` | Concept · Full · Clear · Correct | in_scope | Slide s29 (Trace codes) |
| `sc-03-concept-flywheel` | Concept · Full · Clear · Correct | in_scope | Slide s20 (AI Flywheel) / m01 |
| `sc-04-compare-code-judge` | Comparison · Distributed · Clear · Correct | in_scope | Slide s40, s41 (Code vs Judge) |
| `sc-05-compare-eval-test` | Comparison · Distributed · Clear · Correct | in_scope | Slide s05 / hamel-evals |
| `sc-06-compare-model-app` | Comparison · Distributed · Clear · Correct | in_scope | Slide s06 / m01 (Model vs App Evals) |
| `sc-07-apply-prd-design` | Application · Distributed · Clear · Correct | in_scope | Slide s21, s22 (AI PRD) |
| `sc-08-apply-uig-step` | Application · Full · Clear · Correct | in_scope | Slide s29 (Quy trình UIG) |
| `sc-09-apply-expert-loop` | Application · Distributed · Clear · Correct | in_scope | Slide s60, s61 (Expert in loop) |
| `sc-10-apply-rag-eval` | Application · Distributed · Clear · Correct | in_scope | hamel-evals (evaluating-rag) |
| `sc-11-premise-100-pass` | Concept · Full · Clear · **Incorrect** | in_scope | Slide s48 (Pass rate threshold) |
| `sc-12-premise-replace-human` | Comparison · Distributed · Clear · **Incorrect** | in_scope | Slide s09, s53 (Triad eval) |
| `sc-13-premise-50-prompts` | Application · Full · Clear · **Incorrect** | in_scope | Slide s25 (50 test prompts) |
| `sc-14-premise-unsupported` | Concept · Partial · Clear · **Unsupported** | in_scope | Slide s08 (Notion AI evals) |
| `sc-15-partial-agentic` | Application · Partial · Clear · Correct | in_scope | anthropic-demystifying-evals |
| `sc-16-multi-intent-vibe-off` | Concept · Distributed · **Multi-intent** · Correct | in_scope | Slide s15, s17 (Vibe check to offline) |
| `sc-17-multi-intent-cost-gate` | Application · Distributed · **Multi-intent** · Correct | in_scope | Slide s18 (Quality gate & sample size) |
| `sc-18-ambiguous-slide-metric` | Concept · Full · **Ambiguous** · Correct | unclear | Slide s05 (Agent Success Rate) |
| `sc-19-ambiguous-slide-table` | Application · Full · **Ambiguous** · Correct | unclear | Slide s10 (RACI team roles) |
| `sc-20-ambiguous-slide-gate` | Concept · Full · **Ambiguous** · Correct | unclear | Slide s18 (Regression traces) |
| `sc-21-cheat-capstone-code` | Answer-seeking · None · Clear · Correct | out_of_scope | Xin code bài tập capstone |
| `sc-22-cheat-test-pass` | Answer-seeking · None · Clear · Correct | out_of_scope | Yêu cầu gian lận test unit |
| `sc-23-out-crypto-invest` | Out-of-scope · None · Clear · Correct | out_of_scope | Hỏi đầu tư crypto/Bitcoin |
| `sc-24-out-travel-food` | Out-of-scope · None · Clear · Correct | out_of_scope | Hỏi du lịch Đà Nẵng |
| `sc-25-out-hardware-pc` | Out-of-scope · None · Clear · Correct | out_of_scope | Tư vấn cấu hình PC gaming |

---

## 3. Rubric v1

> Rubric = định nghĩa "đủ tốt" mà cả team chấm giống nhau. Thu hẹp scope trước khi
> viết tiêu chí.

- Tutor trả lời một câu in-scope **"đủ tốt"** khi nào? Viết bằng 1–2 câu ai cũng hiểu.
- Liệt kê các **tiêu chí chấm** (gợi ý: groundedness, citation đúng format, đúng scope,
  chất lượng sư phạm, follow-up có giá trị...). Mỗi tiêu chí: pass/fail thế nào, ví dụ
  pass, ví dụ fail.
- Tiêu chí nào là **blocker** (fail là cả lượt fail)? Tiêu chí nào chỉ là "điểm cộng"?
- Với câu out-of-scope, hành vi nào được coi là pass? (từ chối + gợi ý chủ đề liên quan?)
- Bạn đã thử chấm chéo với ai chưa? Hai người chấm lệch nhau ở tiêu chí nào, sửa rubric
  ra sao sau đó?

### Rubric của bạn

| Tiêu chí | Pass khi | Fail khi | Blocker? |
|---|---|---|---|
| | | | |

---

## 4. Routing Map

> Cái gì kiểm bằng code, cái gì cần LLM judge, cái gì phải đến tay expert. Không phải
> tiêu chí nào cũng cần LLM.

- Với từng tiêu chí trong rubric (mục 3 ở trên): kiểm tra bằng **code** (deterministic), **LLM
  judge**, hay **con người**? Vì sao?
- Tiêu chí nào bạn ban đầu định cho LLM judge chấm nhưng hoá ra code kiểm được rẻ hơn
  (ví dụ: output có parse được JSON không, sources có đủ doc_id hợp lệ không)?
- Tiêu chí nào LLM judge **không tin được** và phải giữ cho con người?
- Judge prompt của bạn (`eval/judge_prompt.md`) chấm tiêu chí nào? Nhiệt độ, model judge là
  gì, vì sao chọn khác model của tutor?

### Bảng routing

| Tiêu chí | Code | LLM judge | Con người | Lý do |
|---|---|---|---|---|
| | | | | |

---

## 5. Calibration Report

> Judge chỉ đáng tin khi đã calibrate với chuẩn vàng của con người. Đây là minh chứng
> cho việc đó.

- Bạn đã **gán nhãn tay** bao nhiêu row? (labels.csv, export từ report.html)
- Chạy `python3 eval/judge.py`: **agreement** giữa judge và nhãn người là bao nhiêu %? Dán
  confusion matrix vào đây.
- Judge **sai ở đâu**? (chặt quá / lỏng quá / lệch ở nhóm câu nào — in-scope hay
  out-of-scope?)
- Bạn đã sửa `eval/judge_prompt.md` thế nào sau vòng calibrate đầu? Agreement sau sửa?
- Kết luận: judge của bạn **đủ tin để chấm tự động tiêu chí nào**, và tiêu chí nào vẫn
  phải giữ cho người?

### Confusion matrix (dán output judge.py)

```
(dán ở đây)
```

---

## 6. Scorecard & Gate

> Tổng hợp điểm theo rubric trên dataset v1, rồi ra quyết định gate như một PM thật.

- Kết quả chạy `eval/run_eval.py` + `eval/judge.py` trên dataset v1: **pass rate** theo từng tiêu
  chí là bao nhiêu? (kèm link/chỉ đường tới results.jsonl, verdicts.jsonl, report.html)
- Chi phí 1 vòng eval là bao nhiêu ($, token)? Latency trung bình 1 câu?
- **Gate**: ngưỡng nào thì ship? Ví dụ: groundedness pass ≥ 90%, không có fail nào ở
  nhóm blocker... — định nghĩa ngưỡng của bạn và giải thích vì sao.
- Kết quả hiện tại: **SHIP hay CHƯA SHIP**? Căn cứ vào gate ở trên.
- Nếu chưa ship: 3 lỗi lớn nhất cần fix ở tutor (prompt, retrieval, corpus)?

### Scorecard

| Tiêu chí | Pass | Fail | Uncertain | Pass rate |
|---|---|---|---|---|
| | | | | |

### Quyết định gate

**SHIP / CHƯA SHIP** — vì: ...

---

## 7. Verdict + Report cuối

> Kết luận cuối cùng của bạn với tư cách PM chịu trách nhiệm chất lượng tutor.
> Verdict đi kèm report 1 trang đủ 5 phần — viết bằng ngôn ngữ PM, không dán log thô.

### Report

#### 1. Dataset đã đánh giá

(tập nào, bao nhiêu traces, coverage chính là gì, blind spot nào còn lại)

#### 2. Quá trình đồng thuận của con người

- Agreement vòng độc lập (nhãn tổng): ___% — kèm thống kê từ note: tiêu chí nào gây bất đồng nhiều nhất
- Mâu thuẫn lớn nhất: (case/tiêu chí nào, hai phía nghĩ gì)
- Nhóm xử lý bằng cách nào: (siết định nghĩa / đổi thang / bỏ tiêu chí...)

#### 3. LLM judge

- Model judge: ________________
- Số vòng calibration: ___ — sau đó judge nhận đúng ___% output tốt và bắt đúng ___% output xấu
- Judge nào không calibrate nổi, vì sao: ________________

#### 4. Bảng quyết định routing (kèm lý giải)

| Tiêu chí | Ngưỡng pass | Giao cho | Vì sao (dựa trên số liệu) |
|---|---|---|---|
| vd: groundedness | ≥90% | LLM judge + audit 10%/tuần | bắt đúng 91% output xấu sau 2 vòng near-miss |
|  |  |  |  |
|  |  |  |  |

#### 5. Verdict + bước tiếp theo

**Ship / Ship with conditions / Hold** — vì: ________________

- Nếu Ship: monitoring tuần đầu xem gì, sample bao nhiêu %, alert ở ngưỡng nào?
- Nếu Hold: đòn bẩy tiếp theo (prompt → model → architecture) và metric chứng minh đã sẵn sàng?

### Câu hỏi tự soi

- Tin cậy nhất ở đâu, đáng lo nhất ở đâu? (dẫn scenario_id cụ thể)
- Nếu chỉ được fix **một thứ** trước khi cho học viên thật dùng, đó là gì?
- Eval loop này sẽ chạy lại **khi nào** (mỗi lần đổi prompt? mỗi tuần? khi corpus đổi?) và ai nhìn kết quả?
- Điều gì trong bài này bạn sẽ **mang về áp dụng** vào sản phẩm thật của mình?
