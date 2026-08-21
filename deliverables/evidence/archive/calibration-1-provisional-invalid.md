# LLM Judge Calibration Report — Round 1

- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Candidate Evaluated**: Candidate Run v3 (`results-v3.jsonl`)
- **Judge Prompt Version**: `eval/judge_prompt.md` (Archived as `deliverables/evidence/judge-prompt-v1.md`)
- **Human Gold Labels**: `labels.csv` (22 consensus scenarios)
- **Execution Date**: `2026-08-21T11:27:57+07:00` (Asia/Saigon)
- **Tracing**: 22 Judge traces exported to LangSmith (Project: `ai-evaluation`)

---

## 1. Confusion Matrix (Round 1)

```
Confusion matrix [groundedness] (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        21         0         0
      fail |         1         0         0
 uncertain |         0         0         0
```

---

## 2. Calibration Metrics

| Metric | Formula | Round 1 Result | Pre-locked Threshold | Status |
|---|---|---|---|---|
| **Judge vs Human Agreement** | (TP + TN) / Total | **95.45% (21/22)** | >= 85.00% | **PASS** |
| **True Positive Rate (TPR / Good-Output Recall)** | TP / (TP + FN) | **95.45% (21/22)** | >= 90.00% | **PASS** |
| **False-Block Count (Type I Error)** | Judge Fail on Human Pass | **1 / 22 (4.55%)** | <= 2 | **PASS** |
| **Missed-Bad Count (Type II Error)** | Judge Pass on Human Fail | **0 / 22 (0.00%)** | 0 | **PASS** |

---

## 3. Discrepancy Error Analysis (False Block on `sc-01`)

- **Scenario ID**: `sc-01-trace-codes-def`
- **Human Consensus Label**: `pass`
- **Judge Round 1 Verdict**: `fail`
- **Judge Rationale**: Judge coi việc Tutor diễn giải thêm về quy trình chuẩn hóa trace code (30-50 traces, tiêu chí Yes/No) là "unsupported claims" vì 2 nguồn trích dẫn chỉ chứa các câu trích ngắn gọn.
- **Root Cause**: Judge Prompt v1 chưa phân biệt rõ ràng giữa:
  1. *Ảo giác / Bịa đặt sai lệch* (Hallucination - bịa thông tin sai lệch ngoài đời hoặc mâu thuẫn bài giảng -> FAIL).
  2. *Diễn giải sư phạm hợp lý* (Pedagogical Elaboration - giải thích mở rộng dựa trên nguyên lý cốt lõi đã có nguồn -> PASS).
- **Remediation for Round 2**: Tinh chỉnh `judge_prompt.md` để làm rõ: Các diễn giải sư phạm mở rộng từ khái niệm gốc trong corpus được coi là PASS nếu không mâu thuẫn hay bịa đặt kiến thức sai lệch.
