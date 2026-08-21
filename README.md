# K3 Track 1 · Day 20–21 — AI Evaluation Lab (VLearn AI Tutor)

Repository triển khai hệ thống Đánh giá Toàn diện (End-to-End AI Evaluation Harness) cho **VLearn AI Tutor** — trợ giảng trả lời câu hỏi học viên, chỉ dựa trên tài liệu khóa học, output là JSON `{scope, answer, sources, followup_questions}`.

---

## 👥 THÔNG TIN NHÓM THỰC HIỆN

* **Nguyễn Quang Huy** — Mã học viên: `2A202601873` (Decision Owner)
* **Lăng Thị Phương Huế** — Mã học viên: `2A202601915` (Collaborator & Annotator)

> **Tên repository chính thức**: `Track1_Day21_2A202601873_NguyenQuangHuy`
> **Remote repository**: `https://github.com/Bietdoibongdem888/Track1_Day21_2A202601873_NguyenQuangHuy.git`
> **Official Upstream**: `https://github.com/VinUni-AI20k/K3-Track1-Day20-21-AI-Evaluation.git` (branch `master`)

---

## 🔄 SƠ ĐỒ 6 PHASE VÀ CÁC ARTIFACT MINH CHỨNG

```
Phase 0: Re-Audit & Integration ────► Baseline (44/44 tests pass) & Corpus Audit (18 docs, 341 sections)
       │
Phase 1: Intentional Coverage ──────► Dimensions (D1–D4), Values (V01–V15), Combinations (C01–C15) [Checkpoint A/B/C Locked]
       │
Phase 2: Human Baseline ────────────► Live LangSmith Run, Independent Labels (Huy, Huế), IAA (95.45%), Consensus Gold (labels.csv)
       │
Phase 3: Observable Rubric & Routing ► Deterministic Code Checks vs Semantic LLM Judge vs Human Policy
       │
Phase 4: Code Checks & Calibration ─► 6 Code Checks (22/22 PASS), LLM Judge 2-Round Calibration (100% Agreement, 0 False-Block)
       │
Phase 5: Locked Thresholds & Slices ─► Thresholds locked BEFORE candidate run, Slice Scorecard by 14 Dimensions & Set Types
       │
Phase 6: Release Verdict & Report ──► PM Verdict (SHIP), 5-Part Executive Summary, Full REPORT.md
```

---

## 📂 BẢNG TRA CỨU ARTIFACTS CHÍNH

| Thành phần | Đường dẫn Artifact | Mô tả | Trạng thái kỹ thuật |
|---|---|---|---|
| **Báo cáo chính** | [`deliverables/REPORT.md`](deliverables/REPORT.md) | Báo cáo hoàn chỉnh 7 mục từ Input Grid đến Verdict | **Complete & Structured** |
| **Nhật ký AI** | [`deliverables/ai-support-log.md`](deliverables/ai-support-log.md) | Minh bạch phạm vi AI hỗ trợ và quyết định của nhóm | **Complete** |
| **Mục lục minh chứng**| [`deliverables/evidence/INDEX.md`](deliverables/evidence/INDEX.md) | Bảng tra cứu tất cả các Gate và bằng chứng thực tế | **Complete & Traceable** |
| **Corpus Audit** | [`deliverables/evidence/corpus-audit.md`](deliverables/evidence/corpus-audit.md) | Kiểm kê 18 tài liệu và 341 sections corpus | **PASS (18 docs, 341 sections)** |
| **Cloud Tracing Evidence** | [`deliverables/evidence/braintrust-link.md`](deliverables/evidence/braintrust-link.md) | Bằng chứng kết nối và xuất trace lên LangSmith | **VERIFIED (LangSmith Cloud)** |
| **Phân luồng Routing** | [`deliverables/evidence/routing-table.md`](deliverables/evidence/routing-table.md) | Ma trận phân bổ tiêu chí vào Code / Judge / Human | **PASS (Specified & Mapped)** |
| **Ngưỡng khóa** | [`deliverables/evidence/thresholds-locked.md`](deliverables/evidence/thresholds-locked.md) | Ngưỡng chất lượng khóa trước khi chạy candidate | **LOCKED BEFORE RUN** |
| **Canonical Dataset** | [`deliverables/evidence/dataset-v1.jsonl`](deliverables/evidence/dataset-v1.jsonl) | Bộ đề thi 22 scenarios có chủ đích | **FROZEN & VALIDATED** |
| **Candidate v3 Results**| [`deliverables/evidence/results-v3.jsonl`](deliverables/evidence/results-v3.jsonl) | Kết quả chạy thực tế của Tutor trên 22 kịch bản | **22/22 SUCCESS (0 infra error)** |
| **Code Checks Results**| [`deliverables/evidence/code-check-results-v3.md`](deliverables/evidence/code-check-results-v3.md) | Kết quả kiểm thử 6 tiêu chí code check tự động | **22/22 on all 6 checks (100%)** |
| **Human Agreement** | [`deliverables/evidence/agreement-v1.md`](deliverables/evidence/agreement-v1.md) | Báo cáo đo lường độ đồng thuận trước consensus | **95.45% IAA (Huy vs Huế)** |
| **Disagreement Packet**| [`deliverables/evidence/disagreement-analysis.md`](deliverables/evidence/disagreement-analysis.md) | Phân tích ca bất đồng sc-16 theo chuẩn V04 | **Resolved to PASS** |
| **Consensus Gold** | [`deliverables/evidence/labels.csv`](deliverables/evidence/labels.csv) | Bộ nhãn vàng đồng thuận của nhóm | **22 consensus rows** |
| **Judge Calibration** | [`deliverables/evidence/calibration-2.md`](deliverables/evidence/calibration-2.md) | Báo cáo hiệu chuẩn 2 vòng của LLM Judge | **100% Agreement & 100% TPR** |
| **Slice Scorecard** | [`deliverables/evidence/scorecard-v1.md`](deliverables/evidence/scorecard-v1.md) | Bảng điểm chi tiết theo 14 lát cắt dữ liệu | **100.00% across all slices** |

---

## 🛠️ HƯỚNG DẪN TÁI HIỆN TOÀN BỘ KIỂM THỬ (REPRODUCTION)

Tất cả các bài kiểm tra kỹ thuật và tính toàn vẹn hệ thống có thể chạy lại tự động:

```powershell
# 1. Chạy toàn bộ bài kiểm tra offline (1 command duy nhất)
powershell -ExecutionPolicy Bypass -File scripts\validate_all.ps1

# 2. Hoặc chạy từng bài kiểm tra riêng biệt:
$env:PYTHONUTF8='1'

# a. 44 bài kiểm tra offline chính thức của eval-kit
python -X utf8 tests\test_eval_kit.py

# b. 23 unit tests cho hệ thống Code Checks mở rộng
python -X utf8 tests\test_code_checks.py

# c. Xác thực tính toàn vẹn của Dataset v1
python evals\validate_dataset.py deliverables\evidence\dataset-v1.jsonl

# d. Chạy kiểm thử Code Checks trên candidate v3
python -X utf8 eval\code_checks.py deliverables\evidence\results-v3.jsonl

# e. Đo Inter-Annotator Agreement (IAA)
python -X utf8 eval\agreement.py deliverables\evidence\labels-huy.csv deliverables\evidence\labels-hue.csv

# f. Chạy LLM Judge hiệu chuẩn
python -X utf8 eval\judge.py

# g. Kiểm tra định dạng git diff
git diff --check
```

---

## 💡 ĐIỀU ÁP DỤNG CHO DỰ ÁN THỰC TẾ

1. **An uncalibrated judge is worse than no judge**: Không bao giờ lấy pass rate của một LLM Judge chưa qua thẩm định làm thước đo chất lượng. Phải đo True Positive Rate (Good recall) và True Negative Rate (Bad catch) đối chiếu với nhãn người.
2. **Code Checks First**: Bất kỳ tiêu chí nào đo được bằng cú pháp, schema, hay đối chiếu chuỗi (`citation_exists`, `quote_verbatim`, `scope_sources_consistency`, `sources_no_duplicates`) phải đẩy về Code Check để đạt độ trễ ~0ms, chi phí $0 và 100% deterministic.
3. **Lock Thresholds Before Candidate Runs**: Khóa các ngưỡng pass/fail trước khi nhìn thấy điểm số của candidate để tránh bias tâm lý và bẫy "hạ chuẩn cho đậu".
4. **Observable Rubrics**: Định nghĩa tiêu chí chấm bằng các câu hỏi Yes/No quan sát được, kèm ví dụ pass/fail từ dữ liệu thật, tránh dùng từ ngữ cảm tính.
