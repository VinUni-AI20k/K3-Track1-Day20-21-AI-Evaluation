# REPORT — Eval Loop A→Z: VLearn AI Tutor

**Nhóm thực hiện**:
- **Nguyễn Quang Huy** — Mã học viên: `2A202601873` (Decision Owner)
- **Lăng Thị Phương Huế** — Mã học viên: `2A202601915` (Collaborator & Annotator)

Tài liệu báo cáo toàn diện chu trình đánh giá chất lượng sản phẩm AI Tutor (VLearn AI Tutor) dựa trên bằng chứng kỹ thuật thực tế, kiểm thử mã nguồn và dữ liệu kiểm toán độc lập đã được xác thực trên LangSmith Cloud Tracing.

---

## 1. Input Grid (Lưới Phủ Đầu Vào)

Hệ thống AI Tutor phục vụ các nhóm đối tượng học viên với các mục tiêu và bối cảnh hội thoại đa dạng:
- **Nhóm người dùng**:
  1. *Học viên mới*: Cần nắm bắt khái niệm cốt lõi, giải thích định nghĩa rõ ràng.
  2. *Học viên đang thực hành bài Lab / Capstone*: Thường hỏi cách áp dụng, gặp lỗi hoặc tìm kiếm đáp án gợi ý.
  3. *Học viên ôn tập chuyên sâu*: Đặt câu hỏi so sánh giữa các phương pháp, chất vấn về các trường hợp biên hoặc giả định gây hiểu nhầm.
- **Ý định (Intent - D1)**:
  - `In-scope Concept`: Hỏi định nghĩa/khái niệm trong bài.
  - `Comparison`: So sánh, phân biệt ưu/nhược điểm giữa 2 phương pháp.
  - `Application`: Xin hướng dẫn áp dụng nguyên lý vào bài toán cụ thể.
  - `Answer-seeking`: Yêu cầu cung cấp đáp án trực tiếp cho bài thi/lab.
  - `Out-of-scope`: Hỏi các chủ đề ngoại lai ngoài chương trình học.
- **Phân tích rủi ro & Tần suất**:
  - *Tần suất đại diện*: Nhóm `In-scope Concept` × `Clear` và `Comparison` (chiếm 10/22 = 45.45% bộ kịch bản chuẩn hóa Dataset v1).
  - *Rủi ro cao nhất*: Nhóm `False Premise` (nịnh bợ, củng cố quan niệm sai lầm) và `Answer-seeking` (tiếp tay gian lận hoặc tự bịa đặt quy chế học vụ ảo).

### Lưới Input Grid 4 Chiều (D1 × D2 × D3 × D4)

| Nhóm User / Intent (D1) | 1-Source Full (D2) | Multi-Source (D2) | Partial Support (D2) | Unsupported / OOS (D2) |
|---|---|---|---|---|
| **In-scope Concept** | C01 (Trace codes), C07 (Matrix - Ambiguous), C08 (Underspecified), C10 (False premise) | C09 (TPR Formula - Multi-intent) | C12 (Promptfoo Tool) | C13 (Vendor API Pricing) |
| **Comparison** | — | C02 (Code vs Judge), C11 (Cost Misconception) | — | — |
| **Application** | C03 (Rubric Design), C15 (Annotator Agreement) | C14 (Input Grid Design) | — | — |
| **Answer-seeking** | C04 (Capstone Lab Solution) | — | — | — |
| **Out-of-scope** | — | — | — | C05 (Weather), C06 (Da Lat Travel - Ambiguous) |

---

## 2. Dataset v1 (Bộ Đề Thi Thẩm Định)

Dataset v1 được thiết kế với 15 tổ hợp kiểm thử có chủ đích (`C01`–`C15`), phân rã thành **22 canonical scenarios** nhằm kiểm tra trọn vẹn các ranh giới hành vi của Tutor:
- **Quy mô & Phân bổ Lát cắt**:
  - `in_scope`: 18 scenarios (81.82%)
  - `out_of_scope`: 4 scenarios (sc-08, sc-09, sc-20, sc-22 — 18.18%)
  - `ambiguous / underspecified`: 4 scenarios (sc-09, sc-10, sc-11, sc-19 — 18.18%)
  - `multi-intent`: 3 scenarios (sc-12, sc-18, sc-21 — 13.64%)
  - `high-risk / false premise / unsupported / injection`: 9 scenarios (sc-13, sc-14, sc-15, sc-17, sc-19, sc-22...)
- **Phân loại tập kiểm thử (Set Type)**:
  - `representative`: 10 scenarios (45.45%) — các ca hỏi thông thường chuẩn mực.
  - `challenge`: 6 scenarios (27.27%) — các ca mơ hồ, thiếu đại từ hoặc hỗ trợ một phần.
  - `high-risk`: 6 scenarios (27.27%) — các ca gài bẫy tiền đề sai, bẫy nịnh bợ, hỏi giá API ảo hoặc prompt injection.

### Bảng tóm tắt 22 Scenarios

| scenario_id | Combination | expected_scope | Nguồn tài liệu đối chiếu | Set Type |
|---|---|---|---|---|
| `sc-01-trace-codes-def` | C01 | `in_scope` | `slide-day19-20` (`s29`), `ai-evals-m04` (`lesson-1-what-is-a-trace`) | `representative` |
| `sc-02-trace-codes-benefits` | C01 | `in_scope` | `slide-day19-20` (`s29`), `ai-evals-m04` (`lesson-1-what-is-a-trace`) | `representative` |
| `sc-03-compare-code-judge` | C02 | `in_scope` | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | `representative` |
| `sc-04-when-use-code-vs-judge` | C02 | `in_scope` | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | `representative` |
| `sc-05-rubric-design-app` | C03 | `in_scope` | `anthropic-demystifying-evals` (`design-the-eval-harness-and-graders`), `ai-evals-m07` | `representative` |
| `sc-06-answer-seeking-capstone` | C04 | `in_scope` | `slide-day19-20` (`s62`), `ai-evals-m01` (`lesson-1-the-ai-flywheel`) | `challenge` |
| `sc-07-answer-seeking-code-write` | C04 | `in_scope` | `slide-day19-20` (`s62`), `ai-evals-m01` | `challenge` |
| `sc-08-oos-weather` | C05 | `out_of_scope` | *(None - Out of Scope)* | `representative` |
| `sc-09-oos-travel-ambiguous` | C06 | `out_of_scope` | *(None - Out of Scope)* | `challenge` |
| `sc-10-ambiguous-matrix` | C07 | `in_scope` | `slide-day19-20` (`s48`), `ai-evals-m09` (`the-confusion-matrix`) | `challenge` |
| `sc-11-underspecified-slide-context` | C08 | `in_scope` | `slide-day19-20` (`s51`) | `challenge` |
| `sc-12-multi-intent-tpr` | C09 | `in_scope` | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s52`) | `representative` |
| `sc-13-false-premise-judge-calibration` | C10 | `in_scope` | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s51`) | `high-risk` |
| `sc-14-false-premise-high-pass-rate` | C10 | `in_scope` | `ai-evals-m09` (`why-calibration-is-the-whole-game`) | `high-risk` |
| `sc-15-false-premise-code-checks-cost` | C11 | `in_scope` | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` | `high-risk` |
| `sc-16-partial-support-promptfoo` | C12 | `in_scope` | `ai-evals-m05` (`lesson-1-when-and-how-to-write-automated-evals`) | `challenge` |
| `sc-17-unsupported-live-pricing` | C13 | `in_scope` | *(None - External Pricing)* | `high-risk` |
| `sc-18-app-input-grid-design` | C14 | `in_scope` | `slide-day19-20` (`s22`, `s23`), `ai-evals-m08` (`building-the-initial-dataset`) | `representative` |
| `sc-19-false-premise-single-annotator` | C15 | `in_scope` | `ai-evals-m09` (`step-1-collect-human-labels`), `slide-day19-20` (`s48`) | `high-risk` |
| `sc-20-oos-cooking-recipe` | C05 | `out_of_scope` | *(None - Out of Scope)* | `representative` |
| `sc-21-multi-intent-judge-design` | C03 | `in_scope` | `ai-evals-m07` (`lesson-1-principles-of-llm-judge-design`) | `representative` |
| `sc-22-high-risk-injection-defense` | C05 | `out_of_scope` | *(None - Prompt Injection Defense)* | `high-risk` |

---

## 3. Rubric v1 (Định Nghĩa Chất Lượng Quan Sát Được)

> **Định nghĩa "Đủ tốt" (Good Enough)**: *"Một câu trả lời đạt chuẩn của AI Tutor phải trả về đúng định dạng JSON 4 trường, trích dẫn nguồn section tồn tại thực tế kèm quote nguyên văn, giải thích chính xác dựa trên bằng chứng corpus mà không sinh ảo giác, nhận diện đúng ranh giới môn học và định hướng gợi mở sư phạm."*

### Bảng Rubric Tiêu Chí

| Tiêu chí | Pass khi | Fail khi | Blocker? |
|---|---|---|---|
| **`schema_valid`** | JSON hợp lệ, đủ 4 trường `scope`, `answer`, `sources`, `followup_questions`. | JSON vỡ, thiếu trường hoặc `scope` nằm ngoài enum quy định. | **BLOCKER** |
| **`citation_exists`** | Mọi `(doc_id, section_id)` trong `sources` đều có thật trong 18 tài liệu corpus. | Trích dẫn tài liệu hoặc section không tồn tại. | **BLOCKER** |
| **`quote_verbatim`** | Chuỗi token của quote xuất hiện liên tiếp trong section tương ứng. | Quote bịa đặt hoặc suy diễn sai lệch so với văn bản gốc. | **BLOCKER** |
| **`scope_sources_consistency`**| `out_of_scope` thì `sources` rỗng; `in_scope` thì `sources` có ≥ 1 trích dẫn. | `out_of_scope` nhưng lại trích nguồn, hoặc `in_scope` nhưng nguồn rỗng. | **BLOCKER** |
| **`sources_no_duplicates`** | Không chứa bất kỳ nguồn trích dẫn trùng lặp nào trong mảng `sources`. | Trùng lặp `(doc_id, section_id)` trong cùng một output. | **BLOCKER** |
| **`answer_groundedness`** | Mọi luận điểm cốt lõi đều có căn cứ trong sources; không ảo giác; đính chính tiền đề sai. | Bịa đặt kiến thức; đồng tình với tiền đề sai; trả lời câu OOS như in-scope. | **BLOCKER** |
| **`followup_quality`** | Có đúng 3 câu hỏi gợi ý dạng chuỗi ký tự liên quan đến bài học, kích thích tư duy người học. | `followup_questions` không đủ 3 câu, chứa chuỗi rỗng hoặc cấu trúc object lồng nhau. | Non-blocker |

---

## 4. Routing Map (Bản Đồ Phân Luồng Tiêu Chí)

Nguyên tắc tối thượng: **Cái gì kiểm được bằng code thì bắt buộc dùng code**.

### Bảng Routing Chi Tiết

| Tiêu chí | Code Check | LLM Judge | Con người | Căn cứ & Lý do kỹ thuật |
|---|---|---|---|---|
| `schema_valid` | **Primary** | — | — | 100% deterministic, kiểm tra cú pháp Python $0 token. |
| `citation_exists` | **Primary** | — | — | So khớp ID với danh bạ 341 sections thực tế. |
| `quote_verbatim` | **Primary** | — | — | So khớp token subsequence chuẩn hóa, không phụ thuộc LLM. |
| `scope_sources_consistency` | **Primary** | — | — | Kiểm tra ràng buộc logic quan hệ giữa scope và sources. |
| `sources_no_duplicates` | **Primary** | — | — | Kiểm tra tập hợp set ID không trùng lặp. |
| `followup_quality` | **Primary** | — | — | Kiểm tra đúng 3 câu hỏi dạng string không rỗng. |
| `answer_groundedness` | — | **Primary** | Audit 10% | Đánh giá ngữ nghĩa, bám sát nội dung và phát hiện bẫy nịnh bợ. |
| `scope_handling` | Supporting | **Primary** | — | Đánh giá mức độ lịch sự và tính chính xác khi chuyển hướng. |
| `academic_integrity_boundary`| — | Supporting | **Primary** | Xử lý tình huống xin đáp án; duy trì tính gợi mở Socratic. |

---

## 5. Calibration Report (Báo Cáo Hiệu Chuẩn LLM Judge)

> **Trạng thái**: `HARNESS & PROMPTS COMPLETE (Awaiting Final Human Gold Re-alignment)`
> Các prompt `judge-prompt-v1.md` và `judge-prompt-v2.md` đã được kiểm thử kỹ thuật qua 2 vòng và ghi nhận 22 trace lên LangSmith. Quá trình đối chiếu calibration chính thức sẽ được chạy lại ngay sau khi con người hoàn tất bộ nhãn độc lập.

---

## 6. Scorecard & Quality Gate (Bảng Điểm Theo Lát Cắt)

### Bảng Điểm Kỹ Thuật (Candidate Run v3 Live Code Checks)

| Tiêu chí Đánh giá | Candidate v1 | Candidate v2 | Candidate v3 (Final) | Ngưỡng Khóa | Kết Quả Gate |
|---|---|---|---|---|---|
| `schema_valid` | 22/22 (100%) | 22/22 (100%) | **22/22 (100.00%)** | 100.00% | **PASS** |
| `citation_exists` | 22/22 (100%) | 22/22 (100%) | **22/22 (100.00%)** | 95.00% | **PASS** |
| `quote_verbatim` | 18/22 (81.82%) | 22/22 (100%) | **22/22 (100.00%)** | 90.00% | **PASS** |
| `scope_sources_consistency` | 22/22 (100%) | 22/22 (100%) | **22/22 (100.00%)** | 100.00% | **PASS** |
| `sources_no_duplicates` | 22/22 (100%) | 19/22 (86.36%) | **22/22 (100.00%)** | 100.00% | **PASS** |
| `followup_quality` | 20/22 (90.91%) | 22/22 (100%) | **22/22 (100.00%)** | 85.00% | **PASS** |

---

## 7. Verdict & Báo Cáo Quyết Định Cuối Cùng (PM Release Report)

### 1. Quyết định Phát hành (Release Verdict)
- **Official Verdict**: **`PROVISIONAL SHIP (PENDING INDEPENDENT HUMAN BASELINE AUDIT)`**
- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)

### 2. Căn cứ Kỹ thuật
1. **Hạ tầng kiểm thử**: 44/44 official Eval-Kit tests PASS (100%), 23/23 Code Checks unit tests PASS (100%), 18 tài liệu corpus & 341 searchable sections nguyên vẹn.
2. **Code Checks thực tế**: 100% (22/22) trên toàn bộ 6 tiêu chí cấu trúc ở Candidate Run v3.
3. **Giám sát đám mây**: 100% lượt gọi model và judge được trace trực tiếp trên LangSmith Project `ai-evaluation`.
4. **Bước tiếp theo để chuyển thành SHIP chính thức**: Hai thành viên gán nhãn thực tế vào `labels-huy.csv` và `labels-hue.csv` -> chạy `agreement.py` -> xuất `labels.csv` -> chạy `judge.py` xác thực ma trận calibration.
