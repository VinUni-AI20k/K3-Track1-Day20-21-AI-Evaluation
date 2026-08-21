# Run Status

## Đã hoàn thành (Complete)

- **Dataset**: 24 scenarios (18 calibration + 6 holdout) in `dataset-v1.jsonl`, `dataset-v2.jsonl`, and `dataset.jsonl`.
- **Tutor Execution**: Executed `tutor.py` on 24 scenarios -> `results-v1.jsonl` & `results.jsonl`.
- **Code-Based Checks**: `eval/code_checks.py` executed -> `code-checks-v1.txt`. Result: 45.8% `quote_verbatim` pass rate (13 fails).
- **Human Baseline & Agreement**: 3 raters (`van`, `linh`, `mai`) completed independent labeling (`labels-van.csv`, `labels-linh.csv`, `labels-mai.csv`). Agreement script `eval/agreement.py` run -> `agreement-v1.txt` (83.3% 3-way agreement, 95.8% max pairwise). Gold consensus saved to `labels.csv` and `deliverables/evidence/labels.csv`.
- **Report HTML**: `eval/report.py` executed -> `report.html` (24 rows embedded).
- **Judge Calibration V1**: Prompt V1 executed on 18 calibration rows -> `verdicts-v1.jsonl` & `judge-metrics-v1.txt` (67% agreement; identified false alarm on refusal scenarios).
- **Judge Calibration V2**: Refusal rules added to `judge_prompt.md` -> `judge-prompt-v2.md`, `verdicts-v2.jsonl` & `judge-metrics-v2.txt` (88.9% agreement; passed ≥85% calibration gate).
- **Holdout Evaluation**: Executed V2 prompt on 6 holdout rows -> `verdicts-holdout.jsonl` & `judge-metrics-holdout.txt` (83.3% agreement; passed ≥80% holdout gate).
- **Report Finalization**: `deliverables/REPORT.md` updated with full empirical metrics, scorecard, confusion matrices, and final **HOLD** verdict.
