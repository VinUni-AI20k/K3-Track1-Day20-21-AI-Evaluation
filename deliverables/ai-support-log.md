# AI Support Log — VLearn AI Tutor Evaluation Lab

- **Project**: AI Evaluation Lab (Track 1 Day 20–21)
- **Repository**: `C:\Users\Huy\Track1_Day21_2A202601873_NguyenQuangHuy`
- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Collaborator / Annotator**: Lăng Thị Phương Huế (`2A202601915`)
- **Evaluation Date**: `2026-08-21`

---

## 1. Phân định Trách nhiệm & Mức độ Hỗ trợ của AI

| Hạng mục công việc | Mức độ AI hỗ trợ | Vai trò của Con người (Huy / Huế) | Bằng chứng kiểm toán (Audit Evidence) |
|---|---|---|---|
| **Phase 0: Base Harness & Forensic Audit** | AI hỗ trợ refactor code checks, fix unit tests và audit corpus 341 sections. | Quyết định tiêu chuẩn hóa và phê duyệt baseline kiểm thử. | `deliverables/evidence/current-state-audit.md`, `tests/test_eval_kit.py` (44 pass), `tests/test_code_checks.py` (23 pass). |
| **Gate 1: Intentional Coverage & Dataset v1** | AI hỗ trợ sinh đề xuất ma trận 15 combinations và 22 scenarios từ corpus. | Huy phê duyệt Checkpoint A (D1-D4), Checkpoint B (C01-C15), Checkpoint C (KEEP 22 scenarios). | `HUMAN-CHECKPOINT-A-APPROVED.md`, `HUMAN-CHECKPOINT-B-APPROVED.md`, `HUMAN-CHECKPOINT-C-PROVENANCE.md`, `dataset-v1.jsonl`. |
| **Gate 2: Live Traced Run & Human Baseline** | AI thực thi batch run trên model thật, ghi nhận trace lên LangSmith, sinh file pre-review. | Huy và Huế chấm nhãn độc lập trên `report.html`, ghi nhận IAA trước đồng thuận, thảo luận ca `sc-16`. | `results-v3.jsonl`, `labels-huy.csv`, `labels-hue.csv`, `agreement-v1.md`, `disagreement-analysis.md`, `labels.csv`. |
| **Gate 3: Observable Rubric & Routing Map** | AI hỗ trợ soạn thảo bảng routing và quy tắc nhị phân quan sát được. | Nhóm phê duyệt triết lý "Ưu tiên code checks làm mặc định, dùng judge cho ngữ nghĩa". | `deliverables/evidence/routing-table.md`, `deliverables/REPORT.md` (Sections 3 & 4). |
| **Gate 4: Code Checks & Judge Calibration** | AI chạy kiểm thử code checks thật, thực hiện 2 vòng calibration LLM judge và phân tích lỗi. | Nhóm phê duyệt định nghĩa ranh giới sư phạm cho Judge Prompt v2. | `code-check-results-v3.md`, `judge-prompt-v1.md`, `judge-prompt-v2.md`, `calibration-1.md`, `calibration-2.md`. |
| **Gate 5: Locked Thresholds & Slice Scorecard** | AI tính toán bảng điểm chi tiết theo 14 lát cắt dữ liệu. | Huy pre-lock ngưỡng kỹ thuật trước candidate scoring tại `thresholds-locked.md`. | `thresholds-locked.md`, `scorecard-v1.md`. |
| **Gate 6: PM Report & Release Decision** | AI tổng hợp báo cáo 7 phần chuẩn cấu trúc upstream. | Huy và Huế ký duyệt quyết định phát hành chính thức (`SHIP`). | `deliverables/REPORT.md`, `deliverables/evidence/braintrust-link.md`, `README.md`. |

---

## 2. Báo cáo Chi tiết Từng Giai đoạn Tương tác

1. **Khởi tạo & Khắc phục Lỗi Hạ tầng (Attempt v1 -> Candidate v3)**:
   - AI phát hiện lỗi 429 quota trên Gemini Free Tier, snapshot raw invalid data thành `results-attempt-v1-invalid.jsonl`.
   - AI bổ sung Exponential Backoff và delay 3.0s, chuyển cấu hình model sang `gemini/models/gemini-flash-lite-latest`.
   - AI tích hợp thành công LangSmith Cloud Tracing (HTTP 200).

2. **Cải tiến Kỹ thuật Đảm bảo Chất lượng Sản phẩm (Candidate v1 -> v2 -> v3)**:
   - Candidate v1: `quote_verbatim` đạt 81.82% do model chèn dấu ba chấm (`...`). AI phân tích nguyên nhân và bổ sung module `ground_verbatim_quote`.
   - Candidate v2: `quote_verbatim` tăng lên 100%, nhưng xuất hiện duplicate sources (86.36%). AI bổ sung deduplication.
   - Candidate v3: Đạt **100.00% (22/22)** trên toàn bộ 6 tiêu chí Code Checks.

3. **Gán nhãn Con người & Đo lường Độ đồng thuận (Gate 2)**:
   - AI chuẩn bị dữ liệu review trực quan trong `report.html` và sinh `labels-ai-review.csv` hỗ trợ con người tra cứu nhanh.
   - Nguyễn Quang Huy và Lăng Thị Phương Huế chấm độc lập, đạt độ đồng thuận 95.45% (21/22).
   - Ca bất đồng `sc-16` được đưa vào `disagreement-analysis.md` và giải quyết theo chuẩn Socratic V04.

4. **Hiệu chuẩn LLM Judge (Gate 4)**:
   - Round 1: Judge v1 đạt 95.45% Agreement (bị 1 false-block trên `sc-01`).
   - Round 2: Sau khi AI tinh chỉnh `judge-prompt-v2.md` làm rõ ranh giới diễn giải sư phạm, Judge v2 đạt **100.00% Agreement & 100.00% TPR**.
