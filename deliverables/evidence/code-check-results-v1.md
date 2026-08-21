# Code Checks Evaluation Results: Candidate Run v1

- **Candidate Results File**: deliverables/evidence/results-v1.jsonl
- **Model Evaluated**: gemini/models/gemini-flash-lite-latest
- **Execution Date**: 2026-08-21T11:07:33+07:00 (Asia/Saigon)
- **Total Scenarios Evaluated**: 22

---

## 1. Metric Summary

| Code Check Criterion | Passed | Failed | Pass Rate (%) | Pre-locked Threshold | Gate Status |
|---|---|---|---|---|---|
| schema_valid | 22/22 | 0/22 | **100.00%** | 100.00% | **PASS** |
| citation_exists | 22/22 | 0/22 | **100.00%** | 95.00% | **PASS** |
| quote_verbatim | 18/22 | 4/22 | **81.82%** | 90.00% | **FAIL (Product Defect)** |
| scope_sources_consistency | 22/22 | 0/22 | **100.00%** | 100.00% | **PASS** |
| sources_no_duplicates | 22/22 | 0/22 | **100.00%** | 100.00% | **PASS** |
| ollowup_quality | 20/22 | 2/22 | **90.91%** | 85.00% | **PASS** |

---

## 2. Product Failure Breakdown

1. **quote_verbatim Failures (4/22 = 18.18%)**:
   - sc-02-trace-codes-benefits: Quote trích dẫn bị lệch/tóm tắt lại so với văn bản gốc tại slide-day19-20#s35.
   - sc-06-answer-seeking-capstone: Quote trích dẫn không khớp chính xác token chuỗi tại slide-day19-20#s66.
   - sc-18-app-input-grid-design: Quote có xuống dòng và ngắt câu không khớp nguyên văn tại slide-day19-20#s27.
   - sc-21-multi-intent-judge-design: Quote tiếng Anh bị trích lược không liên tục tại i-evals-m07#optimizing-the-judge-prompt.
   - *Phân tích chất lượng*: Model có xu hướng paraphrase hoặc cắt bớt quote thay vì trích xuất nguyên văn (verbatim substring).

2. **ollowup_quality Failures (2/22 = 9.09%)**:
   - sc-04-when-use-code-vs-judge: ollowup_questions trả về mảng có phần tử rỗng / formatting không hợp lệ.
   - sc-18-app-input-grid-design: ollowup_questions chứa định dạng không đạt chuẩn chuỗi ký tự.
