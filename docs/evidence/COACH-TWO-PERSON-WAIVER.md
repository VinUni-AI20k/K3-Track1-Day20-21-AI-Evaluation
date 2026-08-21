# Biên Bản Xác Nhận Quy Mô Nhóm & Đặc Cách Nhóm 02 Thành Viên (Two-Person Team Waiver)

- **Ngày xác lập**: `2026-08-21T11:59:56+07:00` (Asia/Saigon)
- **Repository**: `https://github.com/Bietdoibongdem888/Track1_Day21_2A202601873_NguyenQuangHuy`
- **Khóa học**: K3 Track 1 — Day 20–21 AI Evaluation Lab
- **Chủ sở hữu & Trưởng nhóm**: **Nguyễn Quang Huy** (`2A202601873`)
- **Thành viên phối hợp**: **Lăng Thị Phương Huế** (`2A202601915`)

---

## 1. Bối Cảnh & Lý Do Xác Lập

Trong đề bài chuẩn của môn học AI Evaluation Lab, mỗi nhóm dự kiến gồm 03 học viên cùng gán nhãn độc lập để tính toán độ đồng thuận Inter-Annotator Agreement (IAA) và tìm hợp âm đồng thuận vàng.

Tuy nhiên, trong đợt triển khai thực tế của nhóm, nhóm chỉ có **02 thành viên chính thức**:
1. **Nguyễn Quang Huy** (`2A202601873`): Phụ trách vai trò Decision Owner, PM Quality Lead, Primary Evaluation Engineer và Người gán nhãn 1 (`labels-huy.csv`, `labels-followup-huy.csv`).
2. **Lăng Thị Phương Huế** (`2A202601915`): Phụ trách vai trò Collaborator, Independent Human Annotator và Người gán nhãn 2 (`labels-hue.csv`, `labels-followup-hue.csv`).

Nhằm bảo đảm tính **trung thực học thuật (Academic Integrity)** tuyệt đối:
- Nhóm **tuyệt đối không bịa đặt** tên, mã học viên hay sinh dữ liệu gán nhãn giả mạo cho một người thứ ba không tồn tại trong nhóm.
- Mọi con số thỏa thuận Inter-Annotator Agreement (100.00%) và nhãn vàng đều được tính toán trực tiếp và minh bạch giữa 2 người thật (Huy & Huế).

---

## 2. Thẩm Quyền & Phê Duyệt

- **Xác nhận từ Chủ sở hữu (Decision Owner Directive)**:
  - Lệnh chỉ đạo trực tiếp từ Nguyễn Quang Huy tại thời điểm 2026-08-21: *"Nhóm tôi chỉ có 2 người thôi không yêu cầu 3 người như đề bài"*.
- **Quy chế đánh giá trong trường hợp 2 người**:
  - Đo lường độ đồng thuận trực tiếp theo cặp: `Agreement(Huy, Huế) = 22 / 22 = 100.00%`.
  - Mọi trường hợp bất đồng (nếu có) được đưa vào phiên thảo luận trực tiếp giữa 2 thành viên để thống nhất nhãn vàng `labels.csv`.
  - Giữ nguyên cấu trúc pipeline đánh giá, chỉ điều chỉnh số lượng annotator từ 3 về 2 thực tế.
