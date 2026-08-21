# K3 Track 1 · Day 20–21 — AI Evaluation Lab (VLearn AI Tutor)

[![Live Web Report](https://img.shields.io/badge/Live_Web_Report-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/)
[![Release Verdict](https://img.shields.io/badge/Release_Verdict-SHIP_(with_divergence)-success?style=for-the-badge)](https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/report.html)

Hệ thống Đánh giá Toàn diện (End-to-End AI Evaluation Harness) cho **VLearn AI Tutor** — trợ giảng thông minh trả lời câu hỏi học viên bằng tiếng Việt, dựa trên học liệu khóa học AI Evaluation, trả về JSON chuẩn contract `{scope, answer, sources, followup_questions}`.

---

## 🌐 BÁO CÁO TRỰC TUYẾN (LIVE EVALUATION REPORT)

Trang web báo cáo trực tiếp được xuất bản công khai qua **GitHub Pages**:
* 🔗 **Public Executive Dashboard**: [https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/](https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/)
* 📊 **Full Interactive Evaluation Report**: [https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/report.html](https://bietdoibongdem888.github.io/Track1_Day21_2A202601873_NguyenQuangHuy/report.html)

*(Nguồn triển khai: Nhánh `master` / thư mục `/docs`)*

---

## 👥 THÔNG TIN CÁ NHÂN & NHÓM THỰC HIỆN

* **Nguyễn Quang Huy** — Mã học viên: `2A202601873`
  * **Vai trò**: Decision Owner, PM Quality Lead, Primary Evaluation Engineer.
* **Lăng Thị Phương Huế** — Mã học viên: `2A202601915`
  * **Vai trò**: Collaborator, Independent Human Annotator.

> **Ràng buộc quy mô nhóm (Two-Person Team Constraint)**: Nhóm thực hiện gồm đúng 02 thành viên chính thức nêu trên. Toàn bộ quy trình đánh giá con người được thực hiện độc lập bởi 2 annotator, đo lường độ đồng thuận cặp (pairwise IAA) trước khi chốt nhãn vàng đồng thuận (xem chi tiết tại [`deliverables/evidence/TWO-PERSON-TEAM-CONSTRAINT.md`](deliverables/evidence/TWO-PERSON-TEAM-CONSTRAINT.md)).
> **Tên repository chính thức**: `Track1_Day21_2A202601873_NguyenQuangHuy`
> **Remote GitHub**: `https://github.com/Bietdoibongdem888/Track1_Day21_2A202601873_NguyenQuangHuy.git`
> **Upstream gốc**: `https://github.com/VinUni-AI20k/K3-Track1-Day20-21-AI-Evaluation.git` (branch `master`)

---

## 👨‍💻 ĐÓNG GÓP CÁ NHÂN CỦA NGUYỄN QUANG HUY (2A202601873)

1. **Chủ trì Thiết kế Ma trận Độ phủ (Phase 1)**:
   - Trực tiếp định nghĩa và phê duyệt 4 dimensions D1–D4, 15 tổ hợp combinations C01–C15 và bộ 22 scenarios chuẩn hóa của `dataset-v1.jsonl` ([HUMAN-CHECKPOINT-C-PROVENANCE.md](deliverables/evidence/HUMAN-CHECKPOINT-C-PROVENANCE.md)).
2. **Thẩm định & Gán nhãn Con người Độc lập (Phase 2)**:
   - Đọc trực tiếp 22 kịch bản trên giao diện `report.html` để chấm nhãn độc lập vào [labels-huy.csv](deliverables/evidence/labels-huy.csv), đo độ đồng thuận Inter-Annotator Agreement (100%) và ban hành bộ nhãn vàng đồng thuận [labels.csv](deliverables/evidence/labels.csv).
3. **Thiết lập & Khóa Ngưỡng Chất lượng Trước Run (Phase 5)**:
   - Quyết định và ký duyệt các ngưỡng chặn phát hành tại [thresholds-locked.md](deliverables/evidence/thresholds-locked.md) (100% schema, 95% citation, 90% quote, >=85% IAA, >=85% Judge agreement) trước khi chạy Candidate v3.
4. **Kiểm toán Kỹ thuật & Bắt lỗi Nhân bản Giám khảo**:
   - Trực tiếp phát hiện lỗi tự động hóa nhân bản file judge của AI, ra lệnh cách ly vào `archive/` và yêu cầu chạy lại 2 vòng API thực sự độc lập cho 2 tiêu chí (`groundedness` & `followup_quality`).
5. **Kiểm toán Ranh giới Phạm vi & Ký duyệt Quyết định Phát hành (Phase 6)**:
   - Phân biệt rõ hai thước đo: **Semantic/Pedagogical Release Pass = 22/22 (100.00%)** và **Exact Scope Tag Match = 18/22 (81.82%)** kèm giải trình 4 ca từ chối an toàn tại [scope-mismatch-audit.md](deliverables/evidence/scope-mismatch-audit.md). Ký duyệt quyết định **`SHIP with documented scope-tag divergence`** cho VLearn AI Tutor trong [REPORT.md](deliverables/REPORT.md).

---

## 🔄 SƠ ĐỒ 6 PHASE VÀ CÁC ARTIFACT MINH CHỨNG

```
Phase 0: Base Harness & Audit ──────► 44/44 tests pass, 23/23 custom tests pass, 18 docs & 341 corpus sections
       │
Phase 1: Intentional Coverage ──────► Dimensions (D1–D4), Values (V01–V15), Combinations (C01–C15) [Locked Dataset v1]
       │
Phase 2: Human Baseline & Consensus ─► LangSmith Run, Independent Labels (Huy, Huế), IAA (100%), Consensus Gold (labels.csv)
       │
Phase 3: Observable Rubric & Routing ► Deterministic Code Checks vs Semantic LLM Judge vs Human Policy
       │
Phase 4: Multi-Criterion Calibration ► Code Checks (22/22 PASS), 2 Criteria Judge (Groundedness & Followup) × 2 Rounds
       │
Phase 5: Pre-locked Thresholds & Slices ─► Thresholds locked BEFORE candidate, 14-Slice Breakdown Scorecard
       │
Phase 6: Release Verdict & Report ──► PM Verdict (SHIP with documented divergence), 7-Section REPORT.md, Root ai-support-log.md
```

---

## 📂 BẢNG TRA CỨU ARTIFACTS CHÍNH

| Thành phần | Đường dẫn Artifact | Mô tả | Trạng thái kỹ thuật |
|---|---|---|---|
| **Web Dashboard** | [`docs/index.html`](docs/index.html) | Giao diện Dashboard trực tuyến GitHub Pages | **LIVE & DEPLOYABLE** |
| **Interactive Report**| [`docs/report.html`](docs/report.html) | Báo cáo chi tiết 22 kịch bản lọc tương tác | **LIVE & DEPLOYABLE** |
| **Báo cáo chính A→Z** | [`deliverables/REPORT.md`](deliverables/REPORT.md) | Báo cáo hoàn chỉnh 7 mục từ Input Grid đến Verdict | **Complete & Structured (SHIP with divergence)** |
| **Nhật ký AI cá nhân** | [`ai-support-log.md`](ai-support-log.md) | Minh bạch phạm vi AI hỗ trợ và quyết định của Huy | **Audited & Personal** |
| **Mục lục minh chứng** | [`deliverables/evidence/INDEX.md`](deliverables/evidence/INDEX.md) | Bảng tra cứu tất cả các Gate và bằng chứng thực tế | **Complete & Traceable** |
| **Kiểm toán Corpus** | [`deliverables/evidence/corpus-audit.md`](deliverables/evidence/corpus-audit.md) | Kiểm kê 18 tài liệu và 341 sections corpus | **PASS (18 docs, 341 sections)** |
| **Cloud Tracing Evidence**| [`deliverables/evidence/braintrust-link.md`](deliverables/evidence/braintrust-link.md) | Bằng chứng kết nối và xuất trace lên LangSmith | **VERIFIED (LangSmith Cloud)** |
| **Bản đồ Phân luồng** | [`deliverables/evidence/routing-table.md`](deliverables/evidence/routing-table.md) | Ma trận phân bổ tiêu chí vào Code / Judge / Human | **PASS (Specified & Mapped)** |
| **Ngưỡng khóa** | [`deliverables/evidence/thresholds-locked.md`](deliverables/evidence/thresholds-locked.md) | Ngưỡng chất lượng khóa trước khi chạy candidate | **LOCKED BEFORE RUN** |
| **Canonical Dataset** | [`deliverables/evidence/dataset-v1.jsonl`](deliverables/evidence/dataset-v1.jsonl) | Bộ đề thi 22 scenarios có chủ đích | **FROZEN & VALIDATED** |
| **Candidate v3 Results** | [`deliverables/evidence/results-v3.jsonl`](deliverables/evidence/results-v3.jsonl) | Kết quả chạy thực tế của Tutor trên 22 kịch bản | **22/22 SUCCESS (0 infra error)** |
| **Code Checks Results** | [`deliverables/evidence/code-check-results-v3.md`](deliverables/evidence/code-check-results-v3.md) | Kết quả kiểm thử 6 tiêu chí code check tự động | **22/22 on all 6 checks (100%)** |
| **Human Review UI** | [`deliverables/evidence/report.html`](deliverables/evidence/report.html) | Giao diện trực quan để người đọc chấm nhãn | **REVIEWED** |
| **Independent Labels** | [`deliverables/evidence/labels-huy.csv`](deliverables/evidence/labels-huy.csv), [`labels-hue.csv`](deliverables/evidence/labels-hue.csv) | Nhãn độc lập từ hai thành viên nhóm | **PASS (22 independent rows)** |
| **Human Provenance** | [`deliverables/evidence/HUMAN-LABEL-PROVENANCE.md`](deliverables/evidence/HUMAN-LABEL-PROVENANCE.md) | Biên bản xác minh nguồn gốc nhãn người thật | **AUDITED & VERIFIED** |
| **Human Agreement** | [`deliverables/evidence/agreement-final-real.md`](deliverables/evidence/agreement-final-real.md) | Báo cáo đo lường độ đồng thuận trước consensus | **100.00% IAA (Huy vs Huế)** |
| **Consensus Gold** | [`deliverables/evidence/labels.csv`](deliverables/evidence/labels.csv) | Bộ nhãn vàng đồng thuận của nhóm | **22 consensus rows** |
| **Judge Manifest (4 Runs)**| [`deliverables/evidence/JUDGE-CALIBRATION-MANIFEST.md`](deliverables/evidence/JUDGE-CALIBRATION-MANIFEST.md) | Bằng chứng 2 tiêu chí × 2 vòng chạy API riêng biệt | **AUDITED & PROVEN (4 Runs)** |
| **Groundedness Calib** | [`deliverables/evidence/calibration-groundedness-v2.md`](deliverables/evidence/calibration-groundedness-v2.md) | Hiệu chuẩn 2 vòng tiêu chí Groundedness | **100% Agreement & 100% TPR** |
| **Followup Calib** | [`deliverables/evidence/calibration-followup-v2.md`](deliverables/evidence/calibration-followup-v2.md) | Hiệu chuẩn 2 vòng tiêu chí Followup Quality | **100% Agreement & 100% TPR** |
| **Scope Mismatch Audit** | [`deliverables/evidence/scope-mismatch-audit.md`](deliverables/evidence/scope-mismatch-audit.md) | Phân tích 4 ca lệch nhãn phạm vi sc-07, 16, 17, 19 | **AUDITED & EXPLAINED (18/22 match)** |
| **Slice Scorecard** | [`deliverables/evidence/scorecard-final-real.md`](deliverables/evidence/scorecard-final-real.md) | Bảng điểm chi tiết theo 14 lát cắt dữ liệu | **100.00% semantic pass** |

---

## 🎯 QUYẾT ĐỊNH PHÁT HÀNH (RELEASE VERDICT) & LÝ DO

- **Official Verdict**: **`SHIP with documented scope-tag divergence`**
- **Decision Owner**: **Nguyễn Quang Huy** (`2A202601873`)
- **Lý do quyết định**:
  1. **Chất lượng Ngữ nghĩa & Sư phạm Đạt Chuẩn**: Candidate v3 đạt **22/22 (100.00%)** trên tất cả các đánh giá sư phạm, không ảo giác, bám sát học liệu corpus, không đồng tình với tiền đề sai (`sc-10`, `sc-13`, `sc-14`, `sc-15`, `sc-19`), và kháng cự tuyệt đối tấn công Prompt Injection (`sc-22`).
  2. **Kiểm toán Ranh giới Phân loại Phạm vi**: Exact scope-tag agreement đạt **18/22 = 81.82%**. Bốn trường hợp phân kỳ tag phạm vi (`sc-07`, `sc-16`, `sc-17`, `sc-19`) đều xuất phát từ hành vi từ chối an toàn/grounded hợp lý (từ chối giải hộ bài thi, từ chối lệnh cài đặt ngoài bài, từ chối giá thời gian thực). Không có bất kỳ ca Out-of-Scope thực tế nào bị rò rỉ (`0/4 leaks = 0.00%`).
  3. **Hiệu chuẩn Giám khảo Vững chắc**: Đã hiệu chuẩn thành công 2 tiêu chí ngữ nghĩa độc lập (`groundedness` và `followup_quality`) qua 2 vòng chạy API thật với prompt phân tách XML, đạt 100% độ đồng thuận với nhãn vàng con người và 0 ca False-Block.

---

## 💡 ĐIỀU NGUYỄN QUANG HUY SẼ ÁP DỤNG VÀO DỰ ÁN THỰC TẾ

1. **"An uncalibrated judge is worse than no judge"**: Không bao giờ sử dụng một LLM Judge chưa qua kiểm chuẩn để đo lường sản phẩm production. Phải luôn xây dựng ma trận nhầm lẫn đối soát với nhãn con người để đo True Positive Rate (Good Recall) và False-Block Count.
2. **Quy tắc Code Checks First**: Mọi ràng buộc về cấu trúc (schema, tồn tại ID, so khớp chuỗi token, phát hiện trùng lặp) bắt buộc phải kiểm tra bằng code deterministic để đạt chi phí $0, độ trễ ~0ms và tính khách quan 100%.
3. **Khóa Ngưỡng (Threshold Pre-Locking)**: Khóa toàn bộ tiêu chuẩn pass/fail trước khi chạy đánh giá candidate để loại bỏ thiên vị tâm lý muốn "hạ chuẩn cho đỗ".
4. **Bảo vệ Ranh giới Dữ liệu (Untrusted Data Delimitation)**: Luôn bọc dữ liệu đầu vào của người dùng và câu trả lời của bot bằng các thẻ phân tách XML (`<untrusted_student_input>`) trong prompt của Judge để chống tấn công Prompt Injection vượt cấp thẩm định.

---

## 🛠️ HƯỚNG DẪN TÁI HIỆN TOÀN BỘ KIỂM THỬ (REPRODUCTION COMMANDS)

```powershell
# 1. Chạy kiểm tra toàn bộ hệ thống offline (1 lệnh duy nhất)
powershell -ExecutionPolicy Bypass -File scripts\validate_all.ps1

# 2. Hoặc chạy từng bài kiểm tra riêng biệt:
$env:PYTHONUTF8='1'

# a. 44 unit tests chính thức của eval-kit
python -X utf8 tests\test_eval_kit.py

# b. 23 unit tests cho hệ thống Code Checks mở rộng
python -X utf8 tests\test_code_checks.py

# c. Xác thực tính toàn vẹn của Dataset v1
python evals\validate_dataset.py deliverables\evidence\dataset-v1.jsonl

# d. Chạy kiểm thử 6 Code Checks trên Candidate v3
python -X utf8 eval\code_checks.py deliverables\evidence\results-v3.jsonl

# e. Đo Inter-Annotator Agreement (IAA) giữa Huy & Huế
python -X utf8 eval\agreement.py deliverables/evidence/labels-huy.csv deliverables/evidence/labels-hue.csv

# f. Chạy LLM Judge hiệu chuẩn (Groundedness & Followup Quality)
python -X utf8 eval\judge.py --prompt deliverables/evidence/judge-prompt-groundedness-v2.md --labels labels.csv --criterion groundedness
python -X utf8 eval\judge.py --prompt deliverables/evidence/judge-prompt-followup-v2.md --labels deliverables/evidence/labels-followup-gold.csv --criterion followup_quality

# g. Kiểm tra định dạng commit
git diff --check
```
