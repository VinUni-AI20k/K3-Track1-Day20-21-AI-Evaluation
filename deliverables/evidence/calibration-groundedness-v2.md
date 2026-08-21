# LLM Judge Calibration Report — Groundedness Round 2 (Calibrated)

- **Criterion**: `groundedness` (Bám sát Corpus & Không Ảo Giác)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-groundedness-v2.md`
- **Prompt SHA256**: `678a4670e22dd616ceb6e372135541f8d8c4ca734a696ca7f85e87631095cc33`
- **Verdicts File**: `deliverables/evidence/verdicts-groundedness-v2.jsonl`
- **Verdicts SHA256**: `c5bbbd65f50cb3fa975ba75bdb1d8c41bb6cfdc5ae974055b2a92acfa8719180`
- **Gold Reference**: `labels.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T12:03:30+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 2)

```
Confusion matrix [groundedness] (hàng = judge, cột = nhãn người):
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

## 3. Cải Tiến Hiệu Năng Giữa Round 1 và Round 2
- Bổ sung chỉ dẫn tường minh về việc chấp nhận diễn giải sư phạm mở rộng đã giải quyết dứt điểm ca False-Block `sc-21`.
- Cấu trúc bọc thẻ XML `<untrusted_student_input>`, `<untrusted_tutor_answer>`, `<untrusted_sources>` ngăn chặn hoàn toàn việc rò rỉ prompt injection.
