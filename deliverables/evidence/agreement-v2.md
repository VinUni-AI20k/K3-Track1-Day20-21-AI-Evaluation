# Báo Cáo Đo Lường Độ Đồng Thuận Con Người (Inter-Annotator Agreement — IAA)

- **Người đánh giá 1**: Nguyễn Quang Huy (`2A202601873` — Decision Owner)
- **Người đánh giá 2**: Lăng Thị Phương Huế (`2A202601915` — Collaborator / Annotator)
- **Candidate Evaluated**: Candidate Run v3 (`results-v3.jsonl`)
- **Ngày đánh giá**: `2026-08-21T11:37:30+07:00` (Asia/Saigon)
- **Phương pháp**: Đánh giá độc lập trên giao diện `report.html` trước khi họp đồng thuận.

---

## 1. Kết Quả Đo Lường IAA

| Chỉ số | Giá trị Thực tế | Ngưỡng Tối thiểu | Đánh giá |
|---|---|---|---|
| **Số lượng kịch bản chung (Total Paired Cases)** | **22 / 22** | 22 | **Đầy đủ** |
| **Độ đồng thuận tuyệt đối (Overall Agreement)** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Tỷ lệ đồng thuận giữa Huy vs Huế** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Số ca bất đồng (Disagreements)** | **0 ca** | <= 3 ca | **Hoàn hảo** |

---

## 2. Ma Trận Đối Chiếu Nhãn Độc Lập

```
               Huế: PASS    Huế: FAIL    Huế: UNCERTAIN
Huy: PASS         22            0               0
Huy: FAIL          0            0               0
Huy: UNCERTAIN     0            0               0
```

---

## 3. Kết Luận & Chốt Nhãn Vàng Đồng Thuận
- Cả hai người đánh giá đều độc lập xác nhận toàn bộ 22 kịch bản của Candidate Run v3 đạt đầy đủ các tiêu chí về schema, trích dẫn, nguyên văn quote, bám sát nội dung và phân loại phạm vi.
- Toàn bộ 22 kịch bản được chuyển thành **Bộ Nhãn Vàng Đồng Thuận Chính Thức (Consensus Gold Standard)** tại `labels.csv` và `deliverables/evidence/labels.csv`.
