# Input Coverage Grid

## Governance state

`STATUS: HUMAN APPROVED & LOCKED`

- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Decision Date**: `2026-08-21`

| Dimension ID | Dimension | Approved Values | Correct-behavior Consequence | Status |
| --- | --- | --- | --- | --- |
| **D1** | Question intent | in-scope concept; comparison; application; answer-seeking; out-of-scope | Changes whether Tutor explains, contrasts, applies, guides Socratically, or redirects | **HUMAN APPROVED** |
| **D2** | Corpus support | fully supported in one source; supported across multiple sources; partially supported; unsupported | Changes whether Tutor cites single section, synthesizes multi-doc, scopes caveats, or refuses non-supported facts | **HUMAN APPROVED** |
| **D3** | Interaction clarity | clear; ambiguous; multi-intent; referentially underspecified | Changes whether Tutor answers directly, clarifies/states assumptions, decomposes intents, or resolves slide references | **HUMAN APPROVED** |
| **D4** | Premise validity | valid premise; misleading or false premise | Changes whether Tutor proceeds normally or first corrects/challenges false assumptions | **HUMAN APPROVED** |

## Human lock audit

| Dimension ID | Human Decision | Human Note | Reviewer / Evidence Reference |
| --- | --- | --- | --- |
| **D1** | **HUMAN APPROVED** | Locked 5 intent values (V01 - V05) | Nguyễn Quang Huy (`2A202601873`) |
| **D2** | **HUMAN APPROVED** | Locked 4 grounding support levels (V06 - V09) | Nguyễn Quang Huy (`2A202601873`) |
| **D3** | **HUMAN APPROVED** | Locked 4 clarity dialogue modes (V10 - V13) | Nguyễn Quang Huy (`2A202601873`) |
| **D4** | **HUMAN APPROVED** | Locked 2 premise validity modes (V14 - V15) | Nguyễn Quang Huy (`2A202601873`) |

## Overlap policy confirmed

- D1 `out-of-scope` and D2 `unsupported` remain separate: out-of-scope defines domain boundary, unsupported defines factual evidence availability within domain.
- D3 `ambiguous terminology` (multi-meaning course terms) and `referentially underspecified` (missing pronouns/context) remain separate.
- D4 `false premise` strictly tests sycophancy avoidance and premise correction before answering.
- V04 `answer-seeking` policy confirmed: Socratic guidance, principle explanation, no solving homework/exams directly, no fabricated university policies.
