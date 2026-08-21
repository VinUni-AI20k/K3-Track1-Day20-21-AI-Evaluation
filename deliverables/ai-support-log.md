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
| **Phase 0: Base Harness & Forensic Audit** | AI hỗ trợ refactor code checks, fix unit tests và audit corpus 341 sections. | Quyết định tiêu chuẩn hóa và phê duyệt baseline kiểm thử. | `deliverables/evidence/current-state-audit.md`, `tests/test_eval_kit.py` (44 pass), `tests/test_code_checks.py` (23 pass). |
| **Gate 1: Intentional Coverage & Dataset v1** | AI hỗ trợ sinh đề xuất ma trận 15 combinations và 22 scenarios từ corpus. | Huy phê duyệt Checkpoint A (D1-D4), Checkpoint B (C01-C15), Checkpoint C (KEEP 22 scenarios). | `HUMAN-CHECKPOINT-A-APPROVED.md`, `HUMAN-CHECKPOINT-B-APPROVED.md`, `HUMAN-CHECKPOINT-C-PROVENANCE.md`, `dataset-v1.jsonl`. |
| **Gate 2: Live Traced Run & Human Baseline** | AI thực thi batch run trên model thật, ghi nhận 22 trace lên LangSmith, sinh file review packet. | Huy và Huế đọc `report.html` để gán nhãn độc lập trên `labels-huy.csv` và `labels-hue.csv`. | `results-v3.jsonl`, `labels-huy.csv`, `labels-hue.csv`, `labels-ai-review.csv`. *(Lưu ý: nhãn tự sinh trước đó đã được lưu trữ tại `archive/`)*. |
| **Gate 3: Observable Rubric & Routing Map** | AI hỗ trợ soạn thảo bảng routing và quy tắc nhị phân quan sát được. | Nhóm phê duyệt triết lý "Ưu tiên code checks làm mặc định, dùng judge cho ngữ nghĩa". | `deliverables/evidence/routing-table.md`, `deliverables/REPORT.md` (Sections 3 & 4). |
| **Gate 4: Code Checks & Judge Calibration** | AI chạy kiểm thử code checks thật (100% 22/22 pass), thực hiện 2 vòng hiệu chuẩn judge ban đầu. | Nhóm phê duyệt ranh giới rubric cho Judge Prompt v2. | `code-check-results-v3.md`, `judge-prompt-v1.md`, `judge-prompt-v2.md`. |
| **Gate 5: Locked Thresholds & Slice Scorecard** | AI tính toán bảng điểm chi tiết theo 14 lát cắt dữ liệu kỹ thuật. | Huy pre-lock ngưỡng kỹ thuật trước candidate scoring tại `thresholds-locked.md`. | `thresholds-locked.md`, `scorecard-v1.md`. |
| **Gate 6: PM Report & Release Decision** | AI tổng hợp báo cáo 7 phần chuẩn cấu trúc upstream. | Huy xem xét quyết định phát hành dựa trên bằng chứng kỹ thuật và nhãn người. | `deliverables/REPORT.md`, `deliverables/evidence/braintrust-link.md`, `README.md`. |

---

## 2. Ghi chú Kiểm toán về Lịch sử Gán nhãn Con người

- **Sự cố Kiểm toán (Forensic Finding)**: Trong các lượt chạy thử nghiệm tự động trước đó, AI đã tự động điền các nhãn giả lập vào `labels-huy.csv` và `labels-hue.csv` để kiểm thử code.
- **Biện pháp Khắc phục (Remediation)**:
  1. Toàn bộ các kết quả phái sinh từ nhãn tự sinh đó đã được chuyển vào thư mục lưu trữ `deliverables/evidence/archive/` (kèm theo biên bản `INVALID-HUMAN-EVIDENCE-NOTE.md`) và tuyệt đối không được coi là bằng chứng con người hợp lệ.
  2. File `labels-huy.csv` và `labels-hue.csv` đã được khôi phục về trạng thái sạch (cột `label` và `note` để trống) cho Candidate v3.
  3. Bảng gợi ý của AI được tách riêng thành `deliverables/evidence/labels-ai-review.csv` để hỗ trợ con người đối chiếu nhanh.
  4. Quá trình tính toán IAA và hiệu chuẩn Judge cuối cùng sẽ được thực hiện lại ngay khi con người hoàn tất việc gán nhãn thực tế.
