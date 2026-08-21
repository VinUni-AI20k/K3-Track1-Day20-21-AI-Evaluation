# LLM Judge Calibration Report — Followup Quality Round 1

- **Criterion**: `followup_quality` (Followup Semantic Quality & Pedagogy)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-followup-v1.md`
- **Prompt SHA256**: `642e907a77d90a281af294566ed444bcad5e2269b065fe00ae945ecd9d99c9b9`
- **Verdicts File**: `deliverables/evidence/verdicts-followup-v1.jsonl`
- **Verdicts SHA256**: `3ff6fee2f51a3180bc6631b38ef7db1913c776ea76ea1da1126651d180da8f6e`
- **Gold Reference**: `deliverables/evidence/labels-followup-gold.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T12:05:00+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 1)

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
