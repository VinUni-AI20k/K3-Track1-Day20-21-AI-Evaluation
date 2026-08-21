# Báo Cáo Đo Lường Độ Đồng Thuận Đánh Giá Con Người (Inter-Annotator Agreement — Final Report)

- **Người đánh giá 1**: Nguyễn Quang Huy (`2A202601873` — Decision Owner)
- **Người đánh giá 2**: Lăng Thị Phương Huế (`2A202601915` — Annotator)
- **Phiên bản Candidate**: Candidate Run v3 (`results-v3.jsonl`)
- **Ngày đánh giá**: `2026-08-21T11:40:00+07:00` (Asia/Saigon)
- **Phương pháp**: Hai người đánh giá độc lập sử dụng giao diện `report.html`, điền nhãn vào `labels-huy.csv` và `labels-hue.csv`.

---

## 1. Kết Quả Đo Lường Độ Đồng Thuận (IAA Metrics)

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
- Quá trình chốt nhãn vàng đồng thuận không cần bước phân xử trọng tài vì hai bên đã đồng thuận hoàn toàn trên tất cả các kịch bản.
