# AI Support Log — VLearn AI Tutor Evaluation Lab

- **Project**: AI Evaluation Lab (Track 1 Day 20–21)
- **Repository**: `C:\Users\Huy\Track1_Day21_2A202601873_NguyenQuangHuy`
- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Collaborator / Annotator**: Lăng Thị Phương Huế (`2A202601915`)
- **Evaluation Date**: `2026-08-21`

---

## 1. Minh bạch Trách nhiệm & Mức độ Hỗ trợ của AI

| Hạng mục công việc | Mức độ AI hỗ trợ | Vai trò của Con người (Huy / Huế) | Bằng chứng kiểm toán (Audit Evidence) |
|---|---|---|---|
| **Phase 0: Base Harness & Forensic Audit** | AI hỗ trợ refactor code checks, fix unit tests và audit corpus 341 sections. | Quyết định tiêu chuẩn hóa và phê duyệt baseline kiểm thử. | `current-state-audit.md`, `tests/test_eval_kit.py` (44 pass), `tests/test_code_checks.py` (23 pass). |
| **Gate 1: Intentional Coverage & Dataset v1** | AI hỗ trợ sinh đề xuất ma trận 15 combinations và 22 scenarios từ corpus. | Huy phê duyệt Checkpoint A (D1-D4), Checkpoint B (C01-C15), Checkpoint C (KEEP 22 scenarios). | `HUMAN-CHECKPOINT-A-APPROVED.md`, `HUMAN-CHECKPOINT-B-APPROVED.md`, `HUMAN-CHECKPOINT-C-PROVENANCE.md`, `dataset-v1.jsonl`. |
| **Gate 2: Live Traced Run & Human Baseline** | AI thực thi batch run trên model thật, ghi nhận 22 trace lên LangSmith, sinh file review packet. | Huy và Huế đọc `report.html` để gán nhãn độc lập trên `labels-huy.csv` và `labels-hue.csv`. | `results-v3.jsonl`, `labels-huy.csv`, `labels-hue.csv`, `agreement-final-real.md`, `labels.csv`. |
| **Gate 3: Observable Rubric & Routing Map** | AI hỗ trợ soạn thảo bảng routing và quy tắc nhị phân quan sát được. | Nhóm phê duyệt triết lý "Ưu tiên code checks làm mặc định, dùng judge cho ngữ nghĩa". | `routing-table.md`, `deliverables/REPORT.md` (Sections 3 & 4). |
| **Gate 4: Code Checks & Judge Calibration** | AI chạy kiểm thử code checks thật (100% 22/22 pass), thực hiện 2 vòng hiệu chuẩn judge độc lập thực sự. | Nhóm phê duyệt ranh giới rubric cho `judge-prompt-real-v2.md`. | `code-check-results-v3.md`, `judge-prompt-real-v1.md`, `judge-prompt-real-v2.md`, `calibration-real-v1.md`, `calibration-real-v2.md`, `JUDGE-CALIBRATION-MANIFEST.md`. |
| **Gate 5: Locked Thresholds & Slice Scorecard** | AI tính toán bảng điểm chi tiết theo 14 lát cắt dữ liệu kỹ thuật. | Huy pre-lock ngưỡng kỹ thuật trước candidate scoring tại `thresholds-locked.md`. | `thresholds-locked.md`, `scorecard-final-real.md`. |
| **Gate 6: PM Report & Release Decision** | AI tổng hợp báo cáo 7 phần chuẩn cấu trúc upstream. | Huy ký duyệt quyết định phát hành chính thức (`SHIP`). | `deliverables/REPORT.md`, `braintrust-link.md`, `README.md`. |

---

## 2. Ghi chú Kiểm toán & Khắc phục Lỗi Nhân Bản Giám Khảo (Judge Calibration Repair)

1. **Phát hiện Kiểm toán (Forensic Finding)**:
   - Trong một lượt chạy trước đó, hệ thống tự động đã vô tình nhân bản file kết quả của cùng 1 lần chạy Judge thành 2 vòng.
2. **Biện pháp Xử lý Dứt điểm (Definitive Remediation)**:
   - Toàn bộ các file nhân bản cũ đã được di chuyển vào thư mục lưu trữ `deliverables/evidence/archive/judge-calibration-invalid/` kèm biên bản `INVALID-JUDGE-CALIBRATION-NOTE.md`.
   - Tiến hành chạy lại **2 vòng hiệu chuẩn API trực tiếp độc lập thực sự** (`Real Round 1` và `Real Round 2` với prompt cải tiến bọc XML untrusted data).
   - Xác nhận mã băm Prompt (`SHA256(v1) != SHA256(v2)`) và mã băm Verdicts (`SHA256(v1) != SHA256(v2)`) hoàn toàn phân biệt và có trace độc lập trên LangSmith.
   - Xuất biên bản đối chiếu `deliverables/evidence/JUDGE-CALIBRATION-MANIFEST.md`.
