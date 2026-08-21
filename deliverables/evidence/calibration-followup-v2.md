# LLM Judge Calibration Report — Followup Quality Round 2 (Calibrated)

- **Criterion**: `followup_quality` (Followup Semantic Quality & Pedagogy)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-followup-v2.md`
- **Prompt SHA256**: `5b8cb293ed2d13d387b0e358f97848765f192d9027f7a17138f8ecba6d59b4d3`
- **Verdicts File**: `deliverables/evidence/verdicts-followup-v2.jsonl`
- **Verdicts SHA256**: `e46687d211f0d6971be55bbbd5c21ba4030276f50284e956318078e64c1b1014`
- **Gold Reference**: `deliverables/evidence/labels-followup-gold.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T12:06:20+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 2)

```
Confusion matrix [followup_quality] (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        22         0         0
      fail |         0         0         0
 uncertain |         0         0         0
```

---

## 2. Kết Quả Chỉ Số Hiệu Chuẩn

| Chỉ Số Đánh Giá | Kết Quả Thực Tế | Ngưỡng Khóa (Target) | Trạng Thái |
|---|---|---|---|
| **Độ Đồng Thuận (Agreement)** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Good-Output Recall (TPR)** | **22 / 22 = 100.00%** | >= 90.00% | **PASS** |
| **Bad-Output Catch Rate (TNR)** | **N/A** (0 negative cases trong gold set) | — | **N/A** |
| **False-Block Count (Type I Error)** | **0 / 22 (0.00%)** | <= 2 ca | **PASS** |
| **Missed-Bad Count (Type II Error)** | **0 / 22 (0.00%)** | 0 ca | **PASS** |

---

## 3. Cải Tiến Kỹ Thuật Giữa Round 1 và Round 2
- Đưa vào các thẻ `<untrusted_student_input>`, `<untrusted_tutor_answer>` để ngăn ngừa nguy cơ tiêm nhiễm prompt injection trong câu hỏi học viên.
- Bổ sung quy chuẩn đánh giá câu hỏi Socratic: Ưu tiên các câu hỏi mở rộng hiểu biết phương pháp luận AI Evaluation thay vì hỏi lặp lại nội dung đã có.
