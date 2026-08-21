# Final Evaluation Configuration Lock

- **Execution Date**: 2026-08-21T11:04:00+07:00 (Asia/Saigon)
- **Dataset File**: deliverables/evidence/dataset-v1.jsonl
- **Dataset SHA256**: 422849270fedec8c2d3fdbab87c8b3af0807dcf2cd9d93bb8cc9daeda2475629
- **Dataset Row Count**: 22 canonical scenarios (15 unique combinations C01–C15)
- **Tutor Model**: gemini/models/gemini-flash-lite-latest
- **Tutor Provider**: Google AI Studio (OpenAI-compatible REST endpoint)
- **Judge Model**: gemini/models/gemma-4-31b-it
- **Tracing Backend**: LangSmith (Project: i-evaluation)
- **Retrieval Engine**: BM25 Local over 18 documents / 341 searchable sections (top_k=5)
- **Tutor Contract**: Strict JSON with fields scope, nswer, sources, ollowup_questions (exactly 3 questions)
- **Quality Thresholds**: Locked in deliverables/evidence/thresholds-locked.md prior to valid candidate scoring
- **Git Commit Baseline**: 7f43bbb
- **Status**: FROZEN & LOCKED FOR CANDIDATE SCORING
