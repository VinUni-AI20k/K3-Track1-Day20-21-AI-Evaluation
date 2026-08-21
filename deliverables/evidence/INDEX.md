# Evidence & Artifacts Traceability Index

Bảng đối chiếu toàn bộ các Gate, yêu cầu kỹ thuật, file artifact, lệnh kiểm thử và trạng thái thực tế.

| Gate | Yêu cầu kiểm thử | Artifact minh chứng | Lệnh kiểm tra / Tái hiện | Trạng thái thực tế |
|---|---|---|---|---|
| **Phase 0** | Tích hợp Eval-Kit an toàn | `tests/test_eval_kit.py`, `deliverables/evidence/baseline-validation.md` | `$env:PYTHONUTF8='1'; python tests\test_eval_kit.py` | **PASS (44/44 tests)** |
| **Phase 0** | Kiểm kê Corpus 18 tài liệu | `tutor/corpus/manifest.json`, `deliverables/evidence/corpus-audit.md` | `python tests\test_eval_kit.py` | **PASS (18 docs, 341 sections)** |
| **Gate 1** | Phê duyệt Dimensions D1-D4 | `evals/phase1/dimensions.md`, `deliverables/evidence/HUMAN-CHECKPOINT-A-APPROVED.md` | Đối chiếu biên bản phê duyệt | **PASS (HUMAN APPROVED & LOCKED)** |
| **Gate 1** | Phê duyệt Values V01-V15 | `evals/phase1/human_decision_packet.md`, `deliverables/evidence/coverage-matrix.md` | Đối chiếu ma trận coverage | **PASS (HUMAN APPROVED & LOCKED)** |
| **Gate 1** | Phê duyệt Combinations C01-C15 | `deliverables/evidence/combinations-candidate-pool.md`, `deliverables/evidence/HUMAN-CHECKPOINT-B-APPROVED.md` | Đối chiếu mapping corpus (341 sections) | **PASS (HUMAN APPROVED & LOCKED)** |
| **Gate 1** | Canonical Dataset v1 | `deliverables/evidence/dataset-v1.jsonl`, `dataset.jsonl` | `python evals\validate_dataset.py deliverables\evidence\dataset-v1.jsonl` | **PASS (22 rows frozen & validated)** |
| **Gate 2** | Chạy Tutor thực tế | `deliverables/evidence/results-v3.jsonl`, `deliverables/evidence/braintrust-link.md` | `python eval\run_eval.py` | **PASS (22/22 LangSmith Traced)** |
| **Gate 2** | Gán nhãn độc lập 2 thành viên | `deliverables/evidence/labels-huy.csv`, `deliverables/evidence/labels-hue.csv` | Kiểm tra file nhãn độc lập | **PASS (22 independent rows)** |
| **Gate 2** | Đo Agreement trước consensus | `deliverables/evidence/agreement-v1.md`, `deliverables/evidence/disagreement-analysis.md` | `python eval\agreement.py labels-huy.csv labels-hue.csv` | **PASS (95.45% IAA, sc-16 resolved)** |
| **Gate 2** | Nhãn vàng đồng thuận | `labels.csv`, `deliverables/evidence/labels.csv` | Đối chiếu nhãn đồng thuận | **PASS (22 consensus rows)** |
| **Gate 3** | Rubric V1 quan sát được | `deliverables/REPORT.md` (Mục 3) | Đối chiếu bảng rubric | **PASS (6 criteria specified & observable)** |
| **Gate 3** | Ma trận Routing phân luồng | `deliverables/evidence/routing-table.md` | Đối chiếu bảng routing | **PASS (Code vs Judge vs Human mapped)** |
| **Gate 4** | Bộ Code Checks thực tế | `eval/code_checks.py`, `deliverables/evidence/code-check-results-v3.md` | `python eval\code_checks.py deliverables/evidence/results-v3.jsonl` | **PASS (22/22 on all 6 criteria)** |
| **Gate 4** | Hiệu chuẩn LLM Judge (2 vòng) | `judge-prompt-v1.md`, `judge-prompt-v2.md`, `calibration-1.md`, `calibration-2.md` | `python eval\judge.py` | **PASS (100% Agreement & TPR, 0 False-Block)** |
| **Gate 5** | Khóa Ngưỡng trước Run | `deliverables/evidence/thresholds-locked.md` | Đối chiếu timestamp & threshold | **PASS (Thresholds locked before run)** |
| **Gate 5** | Scorecard theo Slice | `deliverables/evidence/scorecard-v1.md` | Merge metadata + results + verdicts | **PASS (14 slices calculated & passed)** |
| **Gate 6** | Báo cáo A→Z 7 mục | `deliverables/REPORT.md` | Đọc báo cáo hoàn chỉnh | **PASS (Official 7-section report complete)** |
| **Gate 6** | Quyết định Release (Verdict) | `deliverables/REPORT.md` (Mục 7) | Phê duyệt từ PM/Nhóm | **PASS (SHIP VERDICT APPROVED)** |
