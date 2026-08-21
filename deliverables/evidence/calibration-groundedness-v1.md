# LLM Judge Calibration Report — Groundedness Round 1

- **Criterion**: `groundedness` (Bám sát Corpus & Không Ảo Giác)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-groundedness-v1.md`
- **Prompt SHA256**: `e514737aa9c56e1e8d2ce49ea11b19b4f22bfd37a52b9fd24cc5a81fa5d87c2a`
- **Verdicts File**: `deliverables/evidence/verdicts-groundedness-v1.jsonl`
- **Verdicts SHA256**: `885160595a9be4d4012b7a50b0d2be7d5cf0b16837ba206c2d8573c4b149d517`
- **Gold Reference**: `labels.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T12:02:00+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 1)

```
Confusion matrix [groundedness] (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        21         0         0
      fail |         1         0         0
 uncertain |         0         0         0
```

---

## 2. Kết Quả Chỉ Số Hiệu Chuẩn

| Chỉ Số Đánh Giá | Kết Quả Thực Tế | Ngưỡng Khóa (Target) | Trạng Thái |
|---|---|---|---|
| **Độ Đồng Thuận (Agreement)** | **21 / 22 = 95.45%** | >= 85.00% | **PASS** |
| **Good-Output Recall (TPR)** | **21 / 22 = 95.45%** | >= 90.00% | **PASS** |
| **Bad-Output Catch Rate (TNR)** | **N/A** (0 negative cases trong gold set) | — | **N/A** |
| **False-Block Count (Type I Error)** | **1 / 22 (4.55%)** | <= 2 ca | **PASS** |
| **Missed-Bad Count (Type II Error)** | **0 / 22 (0.00%)** | 0 ca | **PASS** |
| **Ca Lệch (Mismatch ID)** | `sc-21-multi-intent-judge-design` | — | **False-Block** |

---

## 3. Phân Tích Ca Lệch `sc-21`
- **Nguyên nhân**: Prompt v1 chưa làm rõ việc Tutor có thể đưa ra các diễn giải sư phạm mở rộng bổ trợ kiến thức. Judge Round 1 đã bắt lỗi quá chặt khi thấy Tutor giải thích thêm về trade-off latency/cost.
- **Biện pháp khắc phục cho Round 2**: Nâng cấp prompt v2 với ranh giới rõ ràng về việc chấp nhận diễn giải sư phạm mở rộng hợp lý và bọc XML untrusted data.
