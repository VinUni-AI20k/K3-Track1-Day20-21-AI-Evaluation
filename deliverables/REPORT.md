# REPORT — Eval loop A→Z: VLearn AI Tutor

Report A→Z của eval loop — mỗi mục ứng một phase của bài lab. Mọi số liệu và quyết
định trong đây phải dẫn được xuống file data thô trong `evidence/` (dataset-v1.jsonl,
results-v1.jsonl, labels.csv, judge-prompt.md, verdicts-v1.jsonl).


---

## 1. Input Grid

> Lưới input = trục "ai hỏi" × "hỏi kiểu gì". LLM giúp sinh input, con người kiểm soát
> coverage. Trả lời các câu hỏi sau rồi vẽ lưới của bạn.

- AI Tutor của bạn phục vụ những **nhóm người dùng** nào?
  Học viên mới, học viên đang làm lab/assignment, học viên ôn lại lý thuyết, và những người hỏi ngoài lề (chit-chat, hỏi đáp án).
- Mỗi nhóm có những **ý định (intent)** hỏi nào?
  Hỏi định nghĩa (concept), hỏi ví dụ thực tế, xin đáp án bài tập, chit-chat ngoài luồng, hỏi mơ hồ thiếu ngữ cảnh.
- Ô nào trong lưới là **rủi ro cao** nhất? Ô nào **tần suất cao** nhất?
  Rủi ro cao nhất: Xin đáp án bài tập (nếu đưa thẳng đáp án thì hại học viên), hỏi sai kiến thức cốt lõi. Tần suất cao nhất: Hỏi khái niệm đang học.

### Lưới của bạn

| Nhóm user \ Intent | Hỏi khái niệm (In-scope) | Xin đáp án (Adversarial) | Chit-chat / Ngoài lề (Out-of-scope) | Hỏi mơ hồ thiếu ngữ cảnh |
|---|---|---|---|---|
| **Học viên mới** | Concept cơ bản (Trace Codes) | Hỏi đáp án capstone | Chit-chat AI (Bạn là ai?) | "Cái này khó hiểu quá" |
| **Đang làm lab** | Cú pháp, luồng chạy | Nhờ viết code hộ | Hỏi deploy React, SQL | "Tại sao lỗi số 3?" |
| **Ôn tập lý thuyết**| AI Flywheel, RAG Eval | Nhờ thi hộ | Dự báo thời tiết | "Tóm tắt bài này" |

---

## 2. Dataset v1

> Dataset là "bộ đề thi" của tutor. Nêu rõ nó phủ những ô nào trong input-grid.

- `dataset.jsonl` của bạn có **bao nhiêu câu**? 
  Có 20 câu, phủ sóng 4 intent x 3 đối tượng như lưới trên.
- Tỉ lệ in-scope / out-of-scope / mơ hồ / adversarial là bao nhiêu?
  In-scope (10 câu - 50%), Out-of-scope (4 câu - 20%), Mơ hồ (4 câu - 20%), Adversarial (2 câu - 10%). Tỉ lệ này phản ánh đúng thực tế 80% câu hỏi là hợp lệ.
- Câu nào bạn **lấy từ trace thật**, câu nào do bạn/LLM sinh ra?
  Lấy từ trace giả định các lỗi thường gặp trong lớp, phần lớn được sinh bởi LLM dựa trên bộ syllabus AI Evaluation.
- Ai đã **review** dataset? 
  Reviewed by Engineer. Phát hiện cần phải bao trùm thêm các câu hỏi liên đới đến code eval và LLM Judge.
- Nếu chỉ được giữ 10 câu, bạn giữ 10 câu nào? Vì sao?
  Giữ các câu In-scope cốt lõi (6 câu), 2 câu xin đáp án (để test system prompt block), 2 câu out-of-scope. Vì đây là các case rủi ro và quan trọng nhất.

### Danh sách scenario (bảng tóm tắt)

| scenario_id | ô trong lưới | expected | nguồn câu hỏi |
|---|---|---|---|
| sc-01-in-judge | Đang làm lab / Khái niệm | in_scope | LLM gen |
| sc-03-out-weather | Ôn tập / Chit-chat | out_of_scope | LLM gen |
| sc-04-ambiguous | Mới / Mơ hồ | unclear | LLM gen |
| sc-05-cheat-answer | Đang làm lab / Xin đáp án | in_scope (block) | LLM gen |
| sc-10-out-react | Đang làm lab / Ngoài lề | out_of_scope | LLM gen |

---

## 3. Rubric v1

> Rubric = định nghĩa "đủ tốt" mà cả team chấm giống nhau.

- Tutor trả lời một câu in-scope **"đủ tốt"** khi nào?
  Khi câu trả lời dựa 100% vào ngữ liệu được cung cấp, không bịa đặt, có trích dẫn đúng định dạng, và có câu hỏi follow-up để gợi mở.
- Liệt kê các **tiêu chí chấm**:
  - `schema_valid`: Trả về đúng JSON.
  - `quote_verbatim`: Quote phải có thật trong bài học.
  - `citation_exists`: Trích dẫn phải khớp với doc_id.
  - `followup_exists`: Phải có 3 câu followup.
  - `groundedness`: Mọi khẳng định phải dựa trên sources.
- Tiêu chí nào là **blocker**? Tiêu chí nào chỉ là "điểm cộng"?
  Blocker: `groundedness`, `schema_valid`. Điểm cộng: `followup_exists`.
- Với câu out-of-scope, hành vi nào được coi là pass?
  Từ chối lịch sự, không cố gắng bịa câu trả lời hoặc tìm kiếm trên web.

### Rubric của bạn

| Tiêu chí | Pass khi | Fail khi | Blocker? |
|---|---|---|---|
| schema_valid | Đủ 4 trường JSON | Trả về text thường, thiếu trường | Có |
| quote_verbatim | Trích đoạn có tồn tại y hệt | Quote bịa đặt | Có |
| groundedness | Bám sát source 100% | Bịa thông tin, Hallucination | Có |
| followup_exists| Đúng 3 câu hỏi gợi mở | 0-2 hoặc >3 câu hỏi | Không |

---

## 4. Routing Map

> Cái gì kiểm bằng code, cái gì cần LLM judge, cái gì phải đến tay expert.

- Kiểm tra bằng **code**: `schema_valid`, `citation_exists`, `quote_verbatim`, `followup_exists`. Vì đây là logic tuyệt đối.
- Tiêu chí nào LLM judge **không tin được** và phải giữ cho con người?
  Sự "sư phạm" (Pedagogical quality) - đánh giá giọng văn có phù hợp, có thực sự giúp sinh viên học không.
- Judge prompt chấm tiêu chí nào? 
  Chấm `groundedness`.

### Bảng routing

| Tiêu chí | Code | LLM judge | Con người | Lý do |
|---|---|---|---|---|
| schema_valid | x | | | Check JSON key bằng Python rất rẻ và chuẩn. |
| quote_verbatim | x | | | String matching an toàn tuyệt đối. |
| followup_exists| x | | | Len array = 3 là code giải quyết nhanh gọn. |
| groundedness | | x | | Cần hiểu ngữ nghĩa xem có bịa đặt kiến thức không. |
| pedagogical | | | x | Độ "gợi mở" cần tư duy sư phạm của expert. |

---

## 5. Calibration Report

> Judge chỉ đáng tin khi đã calibrate với chuẩn vàng của con người. Đây là minh chứng
> cho việc đó.

- Bạn đã **gán nhãn tay** bao nhiêu row? 
  Gán nhãn tay 20 row (file `labels.csv`).
- Chạy `python3 eval/judge.py`: **agreement** giữa judge và nhãn người là bao nhiêu %?
  - Vòng 1 (với `judge-prompt-v1.md`): Agreement đạt 90% (18/20).
  - Vòng 2 (với `judge-prompt-v2.md`): Agreement đạt 100% (20/20).
- Judge **sai ở đâu**?
  Ở vòng 1, LLM Judge hay bị lỏng tay và báo fail (false negative) với các câu mà Tutor có paraphrase nhẹ nhưng vẫn đúng ý nghĩa (vd scenario `sc-02` và `sc-06`).
- Bạn đã sửa `judge_prompt.md` thế nào sau vòng calibrate đầu?
  Đã bổ sung câu lệnh khống chế vào `judge-prompt-v2.md`: "[LƯU Ý QUAN TRỌNG: Hãy so sánh kỹ từng ý nghĩa thay vì chỉ match chuỗi, tránh đánh rớt sai (false negative) khi model paraphrase nhẹ.]".
- Kết luận: judge của bạn **đủ tin để chấm tự động tiêu chí nào**?
  Đủ tin cậy để chấm tự động cho `groundedness` do đã chạm trần (100% agreement ở vòng 2).

### Confusion matrix vòng 1 (với judge-prompt-v1.md)

```
Confusion matrix (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        18         0         0
      fail |         2         0         0
 uncertain |         0         0         0
Agreement: 18/20 = 90%
```

### Confusion matrix vòng 2 (với judge-prompt-v2.md)

```
Confusion matrix (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        20         0         0
      fail |         0         0         0
 uncertain |         0         0         0
Agreement: 20/20 = 100%
```

---

## 6. Scorecard & Gate

> Tổng hợp điểm theo rubric trên dataset v1, rồi ra quyết định gate như một PM thật.

- Chi phí 1 vòng eval là bao nhiêu?
  ~$0.00 cho 20 rows (sử dụng local/free model hoặc mock API).
- **Gate**: ngưỡng nào thì ship?
  - `schema_valid` = 100%
  - `groundedness` >= 95%
  - `followup_exists` >= 90%
- Kết quả hiện tại: **CHƯA SHIP**.
- Nếu chưa ship: 3 lỗi lớn nhất cần fix ở tutor?
  Code_checks cho thấy `quote_verbatim` bị fail 15/20 do LLM hiện tại không trích xuất chính xác chuỗi substring từ corpus mà hay diễn đạt lại. LLM Tutor cần được tinh chỉnh để trích xuất nguyên văn.

### Scorecard

| Tiêu chí | Pass | Fail | Uncertain | Pass rate |
|---|---|---|---|---|
| schema_valid | 20 | 0 | 0 | 100% |
| citation_exists| 20 | 0 | 0 | 100% |
| quote_verbatim | 5 | 15 | 0 | 25% |
| followup_exists| 19 | 1 | 0 | 95% |
| groundedness (Judge)| 20 | 0 | 0 | 100% |

### Quyết định gate

**CHƯA SHIP** — vì: Tỉ lệ `quote_verbatim` đang ở mức 25%, thấp hơn rất nhiều so với ngưỡng yêu cầu (100%). Dù groundedness tốt, nhưng học viên không thể tin cậy nếu trích dẫn quote sai sự thật (LLM paraphrase lại quote).

---

## 7. Verdict + Report cuối

> Kết luận cuối cùng của bạn với tư cách PM chịu trách nhiệm chất lượng tutor.

### Report

#### 1. Dataset đã đánh giá

Tập v1, 20 traces, coverage chính là học viên hỏi kiến thức cốt lõi. Blind spot còn lại: jailbreak phức tạp.

#### 2. Quá trình đồng thuận của con người

- Agreement vòng độc lập (nhãn tổng): 100% 
- Mâu thuẫn lớn nhất: Không đáng kể trên 20 mẫu thử nghiệm.
- Nhóm xử lý bằng cách nào: Siết chặt định nghĩa followup (đúng 3 câu).

#### 3. LLM judge

- Model judge: mock (openrouter/google/gemma-4-31b-it:free)
- Số vòng calibration: 1 — sau đó judge nhận đúng 100% output tốt.
- Judge nào không calibrate nổi, vì sao: Cảm nhận độ "hữu ích sư phạm" vì LLM không đóng vai trò giáo viên tốt.

#### 4. Bảng quyết định routing (kèm lý giải)

| Tiêu chí | Ngưỡng pass | Giao cho | Vì sao (dựa trên số liệu) |
|---|---|---|---|
| groundedness | ≥95% | LLM judge + audit 10%/tuần | Phân tích ngữ nghĩa khá tốt |
| quote_verbatim | 100% | Code Checks | Code Python matching chính xác 100% và rẻ |
| followup_exists| ≥90% | Code Checks | Check len(array) == 3 bằng Python cực nhanh |

#### 5. Verdict + bước tiếp theo

**Hold** — vì: Lỗi `quote_verbatim` vi phạm nguyên tắc truy xuất nguyên văn (hallucinated quotes).

- Nếu Hold: đòn bẩy tiếp theo là sửa system prompt của `tutor.py` yêu cầu "BẮT BUỘC TRÍCH XUẤT CHÍNH XÁC SUBSTRING, KHÔNG ĐƯỢC PARAPHRASE", chạy eval loop lại và verify pass rate đạt 100%.

### Câu hỏi tự soi

- Tin cậy nhất ở đâu, đáng lo nhất ở đâu?
  Tin cậy nhất ở `schema_valid` (JSON Mode hoạt động hoàn hảo). Đáng lo nhất ở `quote_verbatim`.
- Nếu chỉ được fix **một thứ** trước khi cho học viên thật dùng, đó là gì?
  Fix lỗi Tutor paraphrase lại Quote.
- Eval loop này sẽ chạy lại **khi nào**?
  Mỗi lần tinh chỉnh System Prompt của Tutor hoặc thay đổi Model, team Engineer sẽ chạy lại tự động.
- Điều gì trong bài này bạn sẽ **mang về áp dụng** vào sản phẩm thật của mình?
  Kiến trúc Routing Map: tách bạch rõ ràng Code Checks (Rẻ, Nhanh) và LLM Judge (Đắt, Semantic).
