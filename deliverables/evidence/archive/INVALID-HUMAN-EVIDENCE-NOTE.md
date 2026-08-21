# Forensic Audit Note: Archival of Synthetic Human Baseline Artifacts

- **Archival Date**: `2026-08-21T11:34:00+07:00` (Asia/Saigon)
- **Status**: `INVALID FOR FINAL HUMAN BASELINE / EXCLUDED FROM OFFICIAL SCORING`

---

## 1. Reason for Archival

Trong quá trình thực thi tự động trước đó, AI đã tự động điền các nhãn vào `labels-huy.csv`, `labels-hue.csv` và `labels.csv` nhằm kiểm thử luồng chạy code của `agreement.py` và `judge.py`.

Chiểu theo quy chuẩn **Liêm chính Học thuật (Academic Integrity)** và quy định của bài thi AI Evaluation Lab:
1. Nhãn do AI tự động sinh ra KHÔNG ĐƯỢC COI LÀ nhãn người độc lập (Independent Human Labels).
2. Tỷ lệ đồng thuận IAA và ma trận calibration tính toán dựa trên các nhãn này là **PROVISIONAL / INVALID** cho việc đánh giá cuối cùng.
3. Các file này được chuyển vào thư mục `archive/` để bảo lưu lịch sử kiểm toán minh bạch, tuyệt đối không được dùng làm căn cứ cấp nhãn vàng chính thức.

---

## 2. Danh sách Artifacts Lưu trữ

- `agreement-ai-generated-invalid.md`: Báo cáo IAA tính từ nhãn tự sinh.
- `disagreement-ai-generated-invalid.md`: Phân tích bất đồng giả lập.
- `calibration-1-provisional-invalid.md`: Vòng 1 calibration đối chiếu với nhãn tự sinh.
- `calibration-2-provisional-invalid.md`: Vòng 2 calibration đối chiếu với nhãn tự sinh.

---

## 3. Hành động Khắc phục (Remediation)

1. Tái tạo lại hai file phôi chấm độc lập hoàn toàn sạch: `deliverables/evidence/labels-huy.csv` và `deliverables/evidence/labels-hue.csv` với cột `label` và `note` để TRỐNG.
2. Tách riêng bảng phân tích đề xuất của AI thành `deliverables/evidence/labels-ai-review.csv` (ghi rõ nguồn gốc AI Pre-Review).
3. Chờ hai thành viên thật (**Nguyễn Quang Huy** và **Lăng Thị Phương Huế**) đọc kết quả Candidate v3 trên `report.html` và trực tiếp điền nhãn độc lập.
