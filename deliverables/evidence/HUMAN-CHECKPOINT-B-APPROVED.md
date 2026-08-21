# Human Checkpoint B: Official Decision Record

- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Decision Date**: `2026-08-21`
- **Overall Decision**: `APPROVE ALL C01 - C15`
- **Governance State**: `LOCKED & FROZEN`

---

## Approved Purposeful Combinations (C01 - C15)

All 15 combinations have been verified against the 341 sections of the 18 corpus documents:

1. **`C01`** (In-scope concept / 1-Source full / Clear / Valid premise): **`APPROVED`**
   - Topic: Trace codes definition & standardization (`slide-day19-20` / `s29`, `ai-evals-m04` / `lesson-1-what-is-a-trace`)
   - Set Type: `representative`
2. **`C02`** (Comparison / Multi-Source / Clear / Valid premise): **`APPROVED`**
   - Topic: Code-based eval vs LLM judge trade-offs (`ai-evals-m06` / `what-exactly-is-a-code-based-eval`, `ai-evals-m07` / `when-to-use-llm-as-judge`)
   - Set Type: `representative`
3. **`C03`** (Application / 1-Source full / Clear / Valid premise): **`APPROVED`**
   - Topic: Observable rubric design for summarization (`anthropic-demystifying-evals` / `design-the-eval-harness-and-graders`, `ai-evals-m07` / `lesson-1-principles-of-llm-judge-design`)
   - Set Type: `representative`
4. **`C04`** (Answer-seeking / 1-Source full / Clear / Valid premise): **`APPROVED`**
   - Topic: Socratic guidance for Capstone task (`slide-day19-20` / `s62`, `ai-evals-m01` / `lesson-1-the-ai-flywheel`)
   - Set Type: `challenge`
5. **`C05`** (Out-of-scope / Unsupported / Clear / Valid premise): **`APPROVED`**
   - Topic: Weather query rejection & redirect (`None`)
   - Set Type: `representative`
6. **`C06`** (Out-of-scope / Unsupported / Ambiguous / Valid premise): **`APPROVED`**
   - Topic: Travel query outside course domain (`None`)
   - Set Type: `challenge`
7. **`C07`** (In-scope concept / 1-Source full / Ambiguous / Valid premise): **`APPROVED`**
   - Topic: Multi-meaning "Matrix" disambiguation (`slide-day19-20` / `s48`, `ai-evals-m09` / `the-confusion-matrix`)
   - Set Type: `challenge`
8. **`C08`** (In-scope concept / 1-Source full / Underspecified / Valid premise): **`APPROVED`**
   - Topic: Slide context `s51` resolution for missing pronoun (`slide-day19-20` / `s51`)
   - Set Type: `challenge`
9. **`C09`** (In-scope concept / Multi-Source / Multi-intent / Valid premise): **`APPROVED`**
   - Topic: True Positive Rate definition & calculation formula (`ai-evals-m09` / `why-calibration-is-the-whole-game`, `slide-day19-20` / `s52`)
   - Set Type: `representative`
10. **`C10`** (In-scope concept / 1-Source full / Clear / False premise): **`APPROVED`**
    - Topic: Disproving "LLM judge never needs calibration" (`ai-evals-m09` / `why-calibration-is-the-whole-game`, `slide-day19-20` / `s51`)
    - Set Type: `high-risk`
11. **`C11`** (Comparison / Multi-Source / Clear / False premise): **`APPROVED`**
    - Topic: Disproving "Code checks cost more than LLM judge" (`ai-evals-m06` / `what-exactly-is-a-code-based-eval`, `ai-evals-m07` / `when-to-use-llm-as-judge`)
    - Set Type: `high-risk`
12. **`C12`** (In-scope concept / Partial support / Clear / Valid premise): **`APPROVED`**
    - Topic: Automated eval principles vs ungrounded external tool Promptfoo CLI (`ai-evals-m05` / `lesson-1-when-and-how-to-write-automated-evals`)
    - Set Type: `challenge`
13. **`C13`** (In-scope concept / Unsupported / Clear / Valid premise): **`APPROVED`**
    - Topic: Non-supported live external vendor pricing (`None`)
    - Set Type: `high-risk`
14. **`C14`** (Application / Multi-Source / Multi-intent / Valid premise): **`APPROVED`**
    - Topic: Input grid & 15 purposeful test combinations design (`slide-day19-20` / `s22`, `s23`, `ai-evals-m08` / `building-the-initial-dataset`)
    - Set Type: `representative`
15. **`C15`** (Application / 1-Source full / Ambiguous / False premise): **`APPROVED`**
    - Topic: Disproving "Single annotator is enough for gold standard" (`ai-evals-m09` / `step-1-collect-human-labels`, `slide-day19-20` / `s48`)
    - Set Type: `high-risk`
