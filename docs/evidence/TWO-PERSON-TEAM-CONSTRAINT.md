# Two-Person Team Constraint & Human Baseline Documentation

- **Dự án**: K3 Track 1 — Day 20–21 AI Evaluation Lab (VLearn AI Tutor)
- **Repository**: `https://github.com/Bietdoibongdem888/Track1_Day21_2A202601873_NguyenQuangHuy`
- **Nhóm thực hiện**: Đúng 02 thành viên chính thức:
  1. **Nguyễn Quang Huy** — Mã học viên: `2A202601873` (Decision Owner, PM Quality Lead, Primary Evaluation Engineer, Annotator 1)
  2. **Lăng Thị Phương Huế** — Mã học viên: `2A202601915` (Collaborator, Independent Annotator 2)

---

## 1. Ràng Buộc Thực Tế Của Dự Án (Project Team Constraint)

Nhóm thực hiện dự án này gồm đúng **02 thành viên chính thức** nêu trên. Để bảo đảm tính **trung thực học thuật (Academic Integrity)** tuyệt đối:
- Nhóm **tuyệt đối không bịa đặt** tên, mã học viên, nhãn giả mạo hoặc phê duyệt giả định của bên thứ ba.
- Nhóm không dừng quy trình đánh giá mà triển khai trọn vẹn quy trình đánh giá con người chuẩn mực theo cấu trúc 2 người độc lập.

---

## 2. Quy Trình Đánh Giá Con Người 2 Thành Viên (Two-Person Human Baseline)

1. **Gán nhãn độc lập (Independent Annotation)**:
   - Cả 2 thành viên đọc trực quan từng kịch bản trên giao diện `report.html` và chấm điểm độc lập trước khi xem nhãn của nhau:
     - `labels-huy.csv` và `labels-followup-huy.csv` (Nguyễn Quang Huy)
     - `labels-hue.csv` và `labels-followup-hue.csv` (Lăng Thị Phương Huế)
2. **Đo lường độ đồng thuận cặp (Pairwise Inter-Annotator Agreement)**:
   - Đo lường trước khi tổ chức phiên đồng thuận bằng lệnh `eval/agreement.py`.
   - Kết quả: **22 / 22 = 100.00% Agreement** trên cả 2 tiêu chí (Groundedness và Follow-up Quality).
3. **Chốt nhãn vàng đồng thuận (Consensus Gold Standards)**:
   - Do 2 người đánh giá đạt đồng thuận hoàn toàn trên 22 kịch bản (0 ca bất đồng), bộ nhãn được chuẩn hóa thành `labels.csv` và `labels-followup-gold.csv`.
