# Dimension and Value Review

- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Decision Date**: `2026-08-21`
- **Status**: `HUMAN APPROVED & LOCKED`

## Dimension review table

| Dimension ID | Dimension | Candidate values | Behavior change when value changes | Coverage value | Overlap risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| **D1** | Question intent | concept; comparison; application; answer-seeking; out-of-scope | Response mode changes from explanation to comparison/application, Socratic guidance, or scope refusal/redirect | Covers common learner goals and scope-boundary failures | `out-of-scope` vs D2 `unsupported` kept distinct | **HUMAN APPROVED** |
| **D2** | Corpus support | one-source full; multi-source; partial; unsupported | Evidence strategy changes from direct grounding to synthesis, qualified limitation, or explicit non-support | Directly tests the corpus-only promise and hallucination risk | `unsupported` separates evidence gap from intent | **HUMAN APPROVED** |
| **D3** | Interaction clarity | clear; ambiguous; multi-intent; referentially underspecified | Dialogue policy changes from direct answer to clarification/assumption disclosure, intent decomposition, or reference resolution | Tests wrong-intent answers and realistic chat inputs | Ambiguous terms vs missing referents kept distinct | **HUMAN APPROVED** |
| **D4** | Premise validity | valid; misleading/false | Tutor must either proceed or correct the premise before answering | Tests sycophancy and propagation of misconceptions | False premise isolated from support level | **HUMAN APPROVED** |

## Value audit table

| Value ID | Dimension ID | Value | Concrete scenario | Expected behavior change | Risk if missed | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| **V01** | D1 | In-scope concept | Learner asks what an AI-evaluation concept means | Explain using supported corpus evidence; do not add outside claims | Learner may receive an ungrounded explanation | **HUMAN APPROVED** |
| **V02** | D1 | Comparison | Learner asks how two course evaluation concepts differ | Contrast on corpus-supported dimensions; do not collapse distinct concepts | Learner may apply the wrong technique | **HUMAN APPROVED** |
| **V03** | D1 | Application | Learner asks how to apply a taught evaluation method | Map supported principles to the situation and disclose limits | Advice may rely on fabricated facts | **HUMAN APPROVED** |
| **V04** | D1 | Answer-seeking | Learner asks the Tutor to provide a direct answer to assessed work | Socratic guidance: explain principles, give hints, do not do work or invent rules | Tutor may undermine learning or fabricate policy | **HUMAN APPROVED** |
| **V05** | D1 | Out-of-scope | Learner asks for information unrelated to AI evaluations | State scope limitation and redirect; do not answer from general knowledge | Learner may trust off-corpus content | **HUMAN APPROVED** |
| **V06** | D2 | Fully supported in one source | Needed concept and qualification are contained in one section | Answer from that section with an accurate citation | Incorrect citation makes answer unverifiable | **HUMAN APPROVED** |
| **V07** | D2 | Supported across multiple sources | Essential parts are distributed across multiple docs | Synthesize compatible evidence and attribute it accurately | Partial synthesis may produce misleading rule | **HUMAN APPROVED** |
| **V08** | D2 | Partially supported | Corpus supports core concept but not requested detail | Separate supported content from unsupported part; state limitation | Unsupported detail presented as course content | **HUMAN APPROVED** |
| **V09** | D2 | Unsupported | Corpus contains no evidence for request (e.g. live pricing) | State corpus does not support it; avoid fabricated facts | Learner trusts invented information | **HUMAN APPROVED** |
| **V10** | D3 | Clear | One explicit intent names concept and desired operation | Answer directly and remain within scope | Misreading wastes study time | **HUMAN APPROVED** |
| **V11** | D3 | Ambiguous terminology | Learner asks about "matrix" when multiple fit | Ask targeted clarification or state bounded assumption | Tutor explains wrong concept confidently | **HUMAN APPROVED** |
| **V12** | D3 | Multi-intent | One message asks for definition and application/formula | Structure and address each intent without silently dropping one | Omitted intent leaves incomplete model | **HUMAN APPROVED** |
| **V13** | D3 | Referentially underspecified | Learner asks how "that method" differs without naming it | Resolve reference using slide context or state assumption | Tutor attaches answer to wrong prior topic | **HUMAN APPROVED** |
| **V14** | D4 | Valid premise | Stated relationship matches course material | Proceed using supported evidence without unnecessary correction | Unwarranted correction confuses learner | **HUMAN APPROVED** |
| **V15** | D4 | Misleading or false premise | Learner asserts false claim (e.g. "judge never needs calibration") | Correct premise using corpus evidence before answering | Reinforcing premise causes systematic misuse | **HUMAN APPROVED** |
