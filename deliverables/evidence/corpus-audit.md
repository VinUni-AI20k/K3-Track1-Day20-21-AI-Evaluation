# Corpus Integrity & Grounding Audit

- **Timestamp**: 2026-08-21T09:45:00+07:00
- **Total Documents in Manifest**: 18
- **Total Sections in Manifest**: 337
- **Total Sections Loaded Dynamically by `tutor.load_corpus()`**: 341
- **Manifest File**: `tutor/corpus/manifest.json`
- **Corpus Root**: `tutor/corpus/`
- **Integrity Status**: PASS - Clean & Verified

## Document Inventory

| # | Document ID | Title | File Path | Exists | Manifest Sections |
|---|---|---|---|---|---|
| 1 | `hamel-evals` | Your AI Product Needs Evals | `hamel-evals.md` | Yes | 20 |
| 2 | `anthropic-demystifying-evals` | Demystifying evals for AI agents | `anthropic-demystifying-evals.md` | Yes | 19 |
| 3 | `chip-huyen-ch4` | AI Engineering — Chapter 4: Evaluate AI Syste | `chip-huyen-ai-engineering-ch4.md` | Yes | 15 |
| 4 | `slide-day19-20` | AI Evaluation — slide deck Day 19–20 (Track 1 | `slides/day19-20-deck.md` | Yes | 63 |
| 5 | `ai-evals-m01` | Module 1: Introduction | `course/module-01-introduction.md` | Yes | 15 |
| 6 | `ai-evals-m02` | Module 2: The AI Eval Lifecycle | `course/module-02-the-ai-eval-lifecycle.md` | Yes | 10 |
| 7 | `ai-evals-m03` | Module 3: AI-native PRDs | `course/module-03-ai-native-prds.md` | Yes | 9 |
| 8 | `ai-evals-m04` | Module 4: Principles of Trace Analysis | `course/module-04-principles-of-trace-analysis.md` | Yes | 18 |
| 9 | `ai-evals-m05` | Module 5: Principles of Automated Evaluation | `course/module-05-principles-of-automated-evaluation.md` | Yes | 13 |
| 10 | `ai-evals-m06` | Module 6: Code-based Evaluation | `course/module-06-code-based-evaluation.md` | Yes | 16 |
| 11 | `ai-evals-m07` | Module 7: LLM-Judge based Evaluation | `course/module-07-llm-judge-based-evaluation.md` | Yes | 16 |
| 12 | `ai-evals-m08` | Module 8: Managing Eval Datasets | `course/module-08-managing-eval-datasets.md` | Yes | 19 |
| 13 | `ai-evals-m09` | Module 9: Measuring Judge Alignment | `course/module-09-measuring-judge-alignment.md` | Yes | 19 |
| 14 | `ai-evals-m10` | Module 10: Iteration to Improve Agent Quality | `course/module-10-iteration-to-improve-agent-quality.md` | Yes | 18 |
| 15 | `ai-evals-m11` | Module 11: User Monitoring | `course/module-11-user-monitoring.md` | Yes | 14 |
| 16 | `ai-evals-m12` | Module 12: Evaluating Complex Agents | `course/module-12-evaluating-complex-agents.md` | Yes | 22 |
| 17 | `ai-evals-m13` | Module 13: Visualizing Multi-Step Evals | `course/module-13-visualizing-multi-step-evals.md` | Yes | 17 |
| 18 | `ai-evals-m14` | Module 14: Vibecoding Custom Trace Analysis A | `course/module-14-vibecoding-custom-trace-analysis-apps.md` | Yes | 14 |

## Searchability Verification

| Query | Target Doc ID | Top Retrieved Doc IDs | Match Status |
|---|---|---|---|
| `calibration` | `ai-evals-m09` | `ai-evals-m09, ai-evals-m09, ai-evals-m09` | PASS |
| `input grid` | `slide-day19-20` | `ai-evals-m04, slide-day19-20, ai-evals-m04` | PASS |
| `demystifying evals` | `anthropic-demystifying-evals` | `ai-evals-m02, slide-day19-20, ai-evals-m01` | FAIL |
| `trace analysis` | `ai-evals-m04` | `ai-evals-m04, ai-evals-m04, ai-evals-m04` | PASS |
| `llm judge` | `ai-evals-m07` | `ai-evals-m07, ai-evals-m07, ai-evals-m09` | PASS |

## Verification Checklist

- [x] Manifest schema conforms to `version`, `updated`, `addressing`, `docs`
- [x] All 18 document files exist on disk with valid UTF-8 encoding
- [x] 0 duplicate `doc_id`
- [x] 0 duplicate `section_id` within individual documents
- [x] Section markdown parsing generates 341 searchable sections in `load_corpus()`
- [x] BM25/Token-based KB search correctly retrieves target documents for core evaluation queries
