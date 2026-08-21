# Corpus Integrity & Grounding Audit

- **Timestamp**: 2026-08-21T10:48:00+07:00 (Asia/Saigon)
- **Total Documents in Manifest**: 18
- **Total Sections in Manifest**: 337
- **Total Sections Loaded Dynamically by 	utor.load_corpus()**: 341 (337 manifest sections + 4 supplementary sub-headings parsed in Markdown)
- **Manifest File**: 	utor/corpus/manifest.json
- **Corpus Root**: 	utor/corpus/
- **Integrity Status**: PASS - 100% Clean & Verified

---

## 1. Document Inventory

| # | Document ID | Title | File Path | Exists | Manifest Sections | Dynamic Sections |
|---|---|---|---|---|---|---|
| 1 | hamel-evals | Your AI Product Needs Evals | hamel-evals.md | Yes | 20 | 20 |
| 2 | nthropic-demystifying-evals | Demystifying evals for AI agents | nthropic-demystifying-evals.md | Yes | 19 | 19 |
| 3 | chip-huyen-ch4 | AI Engineering — Chapter 4: Evaluate AI Systems | chip-huyen-ai-engineering-ch4.md | Yes | 15 | 15 |
| 4 | slide-day19-20 | AI Evaluation — slide deck Day 19–20 (Track 1) | slides/day19-20-deck.md | Yes | 63 | 63 |
| 5 | i-evals-m01 | Module 1: Introduction | course/module-01-introduction.md | Yes | 15 | 15 |
| 6 | i-evals-m02 | Module 2: The AI Eval Lifecycle | course/module-02-the-ai-eval-lifecycle.md | Yes | 10 | 10 |
| 7 | i-evals-m03 | Module 3: AI-native PRDs | course/module-03-ai-native-prds.md | Yes | 9 | 9 |
| 8 | i-evals-m04 | Module 4: Principles of Trace Analysis | course/module-04-principles-of-trace-analysis.md | Yes | 18 | 18 |
| 9 | i-evals-m05 | Module 5: Principles of Automated Evaluation | course/module-05-principles-of-automated-evaluation.md | Yes | 13 | 13 |
| 10 | i-evals-m06 | Module 6: Code-based Evaluation | course/module-06-code-based-evaluation.md | Yes | 16 | 16 |
| 11 | i-evals-m07 | Module 7: LLM-Judge based Evaluation | course/module-07-llm-judge-based-evaluation.md | Yes | 16 | 16 |
| 12 | i-evals-m08 | Module 8: Managing Eval Datasets | course/module-08-managing-eval-datasets.md | Yes | 19 | 19 |
| 13 | i-evals-m09 | Module 9: Measuring Judge Alignment | course/module-09-measuring-judge-alignment.md | Yes | 19 | 19 |
| 14 | i-evals-m10 | Module 10: Iteration to Improve Agent Quality | course/module-10-iteration-to-improve-agent-quality.md | Yes | 18 | 18 |
| 15 | i-evals-m11 | Module 11: User Monitoring | course/module-11-user-monitoring.md | Yes | 14 | 14 |
| 16 | i-evals-m12 | Module 12: Evaluating Complex Agents | course/module-12-evaluating-complex-agents.md | Yes | 22 | 24 |
| 17 | i-evals-m13 | Module 13: Visualizing Multi-Step Evals | course/module-13-visualizing-multi-step-evals.md | Yes | 17 | 18 |
| 18 | i-evals-m14 | Module 14: Vibecoding Custom Trace Analysis Apps | course/module-14-vibecoding-custom-trace-analysis-apps.md | Yes | 14 | 15 |
| **Total** | **18 Docs** | — | — | **18/18** | **337** | **341** |

---

## 2. Searchability & BM25 Retrieval Verification

| Query | Target Doc ID | Top Retrieved (Doc ID # Section ID) | Match Status | Ghi chú kỹ thuật |
|---|---|---|---|---|
| calibration | i-evals-m09 | i-evals-m09#why-calibration-is-the-whole-game | **PASS** | Khớp chính xác module về Alignment |
| input grid | slide-day19-20 | slide-day19-20#s22, slide-day19-20#s23 | **PASS** | Khớp chính xác slide Input Grid |
| 	ypes of graders for agents | nthropic-demystifying-evals | nthropic-demystifying-evals#types-of-graders-for-agents | **PASS** | Khớp chính xác bài của Anthropic |
| 	race analysis | i-evals-m04 | i-evals-m04#principles-of-trace-analysis | **PASS** | Khớp chính xác module Trace Analysis |
| llm judge | i-evals-m07 | i-evals-m07#llm-judge-based-evaluation | **PASS** | Khớp chính xác module LLM Judge |
| evaluating rag | hamel-evals | hamel-evals#evaluating-rag | **PASS** | Khớp chính xác blog Hamel Husain |

---

## 3. Verification Checklist

- [x] Manifest schema conforms to ersion, updated, ddressing, docs.
- [x] All 18 document files exist on disk with valid UTF-8 encoding.
- [x] 0 duplicate doc_id.
- [x] 0 duplicate section_id within individual documents.
- [x] Dynamic loader generates 341 searchable sections (tested via official 	est_eval_kit.py).
- [x] BM25 local search retrieves target documents with 100% precision on domain queries.
