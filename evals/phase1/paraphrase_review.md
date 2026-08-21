# Paraphrase Generation and Review

## Gate

`BLOCKER: Cannot run final paraphrase generation because combinations are not yet human-approved.`

No user inputs have been AI-generated. No `KEEP`, `REWRITE`, or `REJECT` decision is claimed.

## Output table after combination approval

| combination_id | variant_id | user_input | style | preserved_constraints | notes |
| --- | --- | --- | --- | --- | --- |
| PENDING | PENDING | PENDING | PENDING | PENDING | PENDING |

## Quality audit after generation

| Row | Combination | Intent preserved | Constraint preserved | Natural | Duplicate risk | AI recommendation | Human decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PENDING | PENDING | NOT YET OBSERVED | NOT YET OBSERVED | NOT YET OBSERVED | NOT YET OBSERVED | PENDING | PENDING |

Human decision must be one of `KEEP`, `REWRITE`, or `REJECT`. AI recommendations cannot populate that field.

## Required controls

- Exactly two natural inputs per approved combination.
- Preserve intent, support level, difficulty, ambiguity, false assumptions, and missing context.
- Do not add an answer hint, new intent, or helpful context absent from the approved design.
- Use distinct styles while testing the same behavior.
