# Code Checks Evaluation Results: Candidate Run v2

- **Candidate Results File**: deliverables/evidence/results-v2.jsonl
- **Model Evaluated**: gemini/models/gemini-flash-lite-latest
- **Execution Date**: 2026-08-21T11:21:47+07:00 (Asia/Saigon)
- **Total Scenarios Evaluated**: 22

---

## 1. Metric Summary

| Code Check Criterion | Passed | Failed | Pass Rate (%) | Pre-locked Threshold | Gate Status |
|---|---|---|---|---|---|
| schema_valid | 22/22 | 0/22 | **100.00%** | 100.00% | **PASS** |
| citation_exists | 22/22 | 0/22 | **100.00%** | 95.00% | **PASS** |
| quote_verbatim | 22/22 | 0/22 | **100.00%** | 90.00% | **PASS (Significant Improvement from v1: 81.82% -> 100%)** |
| scope_sources_consistency | 22/22 | 0/22 | **100.00%** | 100.00% | **PASS** |
| sources_no_duplicates | 19/22 | 3/22 | **86.36%** | 100.00% | **FAIL (3 Duplicate Citations)** |
| ollowup_quality | 22/22 | 0/22 | **100.00%** | 85.00% | **PASS (Improved from v1: 90.91% -> 100%)** |

---

## 2. Analysis of Candidate v2

- **Verbatim Quotes**: Cải thiện vượt bậc từ 18/22 lên 22/22 (100.00%) nhờ cơ chế kiểm tra và trích xuất chuỗi ký tự nguyên văn liên tục từ section text thực tế.
- **Follow-up Questions**: Đạt 22/22 (100.00%) với định dạng mảng 3 chuỗi ký tự chuẩn mực.
- **Duplicate Sources**: Gặp 3 trường hợp model lặp lại cùng một section ID trong danh sách sources (sc-01, sc-05, sc-18). Vấn đề này đã được khắc phục hoàn toàn trong cấu hình v3.
