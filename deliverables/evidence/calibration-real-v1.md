# LLM Judge Calibration Report — Real Round 1

- **Run Type**: Live Independent Execution (Round 1)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Candidate Evaluated**: Candidate Run v3 (`results-v3.jsonl`)
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-real-v1.md`
- **Judge Prompt SHA256**: `9ad5c07681c856d958bc24958d50746f282415697bbfd1d2e13691a254a6fa67`
- **Verdicts Output Path**: `deliverables/evidence/verdicts-real-v1.jsonl`
- **Verdicts SHA256**: `f510adbfdfad3e67009a712cca30f7c040beee3f9a7b1cdd1295af1311abb99d`
- **Human Gold Reference**: `labels.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T11:46:30+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 1)

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
| **Độ Nhạy (TPR / Good Recall)** | **22 / 22 = 100.00%** | >= 90.00% | **PASS** |
| **False-Block Count (Type I Error)** | **0 / 22 (0.00%)** | <= 2 ca | **PASS** |
| **Missed-Bad Count (Type II Error)** | **0 / 22 (0.00%)** | 0 ca | **PASS** |
| **Số ca Mismatches** | **0 ca** | — | **Hoàn hảo** |
