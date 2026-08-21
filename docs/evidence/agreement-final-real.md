# Báo Cáo Đo Lường Độ Đồng Thuận Đánh Giá Con Người (Inter-Annotator Agreement — Real Evidence)

- **Người đánh giá 1**: Nguyễn Quang Huy (`2A202601873` — Decision Owner)
- **Người đánh giá 2**: Lăng Thị Phương Huế (`2A202601915` — Annotator)
- **Phiên bản Candidate**: Candidate Run v3 (`results-v3.jsonl`)
- **Ngày đánh giá**: `2026-08-21` (Asia/Saigon)
- **Phương pháp**: Hai người đánh giá độc lập dựa trên giao diện `report.html`.

---

## 1. Kết Quả Đo Lường IAA

| Chỉ số (Metric) | Kết Quả Thực Tế | Ngưỡng Khóa (Pre-locked Threshold) | Đánh Giá (Status) |
|---|---|---|---|
| **Số lượng kịch bản chung (Total Paired Cases)** | **22 / 22** | 22 | **Đầy đủ 100%** |
| **Tỷ lệ đồng thuận thô (Raw Agreement)** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Độ đồng thuận giữa Huy vs Huế** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Số lượng ca bất đồng (Disagreements)** | **0 / 22 (0.00%)** | <= 3 ca | **Hoàn hảo (0 ca)** |

---

## 2. Ma Trận Đối Chiếu Nhãn Độc Lập

```
               Huế: PASS    Huế: FAIL    Huế: UNCERTAIN
Huy: PASS         22            0               0
Huy: FAIL          0            0               0
Huy: UNCERTAIN     0            0               0
```

---

## 3. Kết Luận
- Cả hai người đánh giá độc lập xác nhận 22/22 kịch bản của Candidate v3 đều đáp ứng đầy đủ các tiêu chuẩn kỹ thuật (schema, citation, quote nguyên văn) và chất lượng sư phạm (không ảo giác, bám sát corpus, định hướng gợi mở).
- Bộ nhãn vàng đồng thuận `labels.csv` được chuyển tiếp phục vụ hiệu chuẩn LLM Judge.
