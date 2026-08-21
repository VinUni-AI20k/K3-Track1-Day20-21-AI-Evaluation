# VLearn AI Tutor — Phase 1

## Status

`STATUS: PROPOSED — HUMAN DECISION REQUIRED`

`GATE 1: BLOCKED`

This directory is a governance-first Phase 1 packet. It does not claim human approval, corpus evidence, Tutor traces, runtime results, or final Dataset v1 status.

## Workspace audit

| Field | Finding |
| --- | --- |
| Repository | `C:\Users\Huy\HUYCOCKIUDEPZAI` |
| Branch | `main` tracking `origin/main` |
| HEAD during audit | `f580eec` (`Initial commit`) |
| Working tree before Phase 1 work | Clean |
| Existing Phase 1 artifacts | None observed |
| Existing dataset | None observed |
| Existing AI Support Log | None observed |
| Existing corpus references | None observed |
| README / guide | Root README only; no guide |
| Day 20 / Day 21 artifacts | None observed |
| Templates / eval-kit | None observed |

### Missing evidence and artifacts

- Human-approved dimensions and values
- Corpus inventory or section-level metadata
- Human-approved combinations
- Approved real-world constraints
- AI paraphrases and per-row human `KEEP` / `REWRITE` / `REJECT` decisions
- A 20–30 row Dataset v1
- Executable coverage statistics and a populated coverage matrix

### File boundaries

Safe to modify for this task: files under `evals/phase1/`.

Must remain untouched: `.git/` and any future product code, corpus, or unrelated project artifacts.

## Artifact index

- `input_grid.md`: proposed coverage grid and human lock form
- `dimensions.md`: dimension review and concrete value audit
- `combinations.md`: gated combination-selection template
- `real_world_constraints.md`: gated constraint template
- `paraphrase_review.md`: paraphrase governance and review table
- `dataset_v1.csv`: schema-only placeholder; not a final dataset
- `coverage_matrix.md`: coverage/statistics audit placeholder
- `gate1_audit.md`: objective Gate 1 status and blockers
- `ai_support_log.md`: disclosure of AI assistance
- `version_log.md`: coverage change record
- `corpus_inventory.md`: local corpus discovery result
- `traceability_matrix.md`: row-level provenance scaffold
- `validate_dataset.py`: read-only Dataset v1 validator
- `continuation_report.md`: latest evidence-backed execution report
- `human_decision_packet.md`: consolidated human review surface
- `execution_report.md`: latest resume execution report
- `human_review_report.md`: complete 19-item decision analysis and reply block

## Required human workflow

1. Review the proposed dimensions and every value in `dimensions.md`.
2. Record `HUMAN APPROVED` or `REJECTED BY HUMAN`; edit values where needed.
3. Provide corpus inventory/evidence so support-level scenarios can be instantiated truthfully.
4. Only then generate and select 12–15 meaningful combinations.
5. Approve combination-specific constraints and high-level expected behaviors.
6. Only then generate two paraphrases per approved combination.
7. Record `KEEP`, `REWRITE`, or `REJECT` for every generated input.
8. Assemble only kept/rewritten rows into Dataset v1 and rerun Gate 1.

Do not start Phase 2 until Gate 1 passes.
