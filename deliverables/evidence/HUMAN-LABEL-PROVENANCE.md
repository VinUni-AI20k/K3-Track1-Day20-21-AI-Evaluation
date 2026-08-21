# Human Label Provenance Manifest

- **Target Candidate**: Candidate Run v3 (`results-v3.jsonl`, SHA256 verified)
- **Evaluation Date**: `2026-08-21` (Asia/Saigon)
- **Scenario Count**: 22 canonical scenarios (`sc-01` to `sc-22`)

---

## 1. Reviewer Information & Roles

1. **Nguyễn Quang Huy**
   - **Mã học viên**: `2A202601873`
   - **Vai trò**: Decision Owner & Primary Evaluator
   - **File nhãn độc lập**: `deliverables/evidence/labels-huy.csv` (22/22 rows non-empty, label: `pass` kèm ghi chú nhận xét chi tiết từng câu).
   - **Phương tiện chấm**: Đọc trực tiếp câu hỏi, context và output của Candidate v3 trên giao diện `deliverables/evidence/report.html`.

2. **Lăng Thị Phương Huế**
   - **Mã học viên**: `2A202601915`
   - **Vai trò**: Collaborator & Independent Annotator
   - **File nhãn độc lập**: `deliverables/evidence/labels-hue.csv` (22/22 rows non-empty, label: `pass` kèm ghi chú nhận xét độc lập).
   - **Phương tiện chấm**: Đọc trực tiếp câu hỏi, context và output của Candidate v3 trên giao diện `deliverables/evidence/report.html`.

---

## 2. Provenance Verification
- Cả hai bộ nhãn được kiểm tra tính toàn vẹn: 22 kịch bản khớp tuyệt đối với `results-v3.jsonl`, không trùng lặp, không có ô trống.
- Ghi chú nhận xét (notes) thể hiện đánh giá độc lập về các khía cạnh sư phạm (khái niệm trace codes, ưu nhược điểm code check vs judge, từ chối câu hỏi xin đáp án, đính chính tiền đề sai, phòng thủ injection).
- Độ đồng thuận trước thảo luận đạt 22/22 = 100.00% (đồng thuận tuyệt đối trên mọi kịch bản).
