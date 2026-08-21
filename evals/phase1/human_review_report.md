# Phase 1 Human Decision Review

## Evidence state

- Dimensions pending: 4
- Values pending: 15
- Verified corpus documents: 0
- All human decisions remain `PENDING HUMAN REVIEW`.
- Every corpus-specific support claim below is `UNVERIFIED — CORPUS REQUIRED`.

## Dimension reviews

### D1 — Question intent

- Values: in-scope concept, comparison, application, answer-seeking, out-of-scope.
- Behavior change: the Tutor shifts between explaining, contrasting, applying, respecting learning boundaries, and declining/redirecting outside scope.
- Coverage benefit: represents common learner goals plus the important product scope boundary.
- Overlap: out-of-scope frequently correlates with D2 unsupported, but D1 describes what the learner asks while D2 describes available evidence. Answer-seeking may depend on an unverified course policy.
- Risk if omitted: the dataset may overrepresent simple concept questions and miss scope violations or inappropriate completion of assessed work.
- Test A: PASS — values require distinct response modes.
- Test B: PASS — this is behavioral, not surface style.
- Test C: MANAGEABLE OVERLAP — retain separate from D2 with explicit definitions.
- Test D: PASS — adds scope and learner-goal boundaries.
- Test E: PASS — supports representative, challenge, and high-risk coverage.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### D2 — Corpus support

- Values: fully supported in one source, supported across multiple sources, partially supported, unsupported.
- Behavior change: the Tutor shifts among direct grounding, synthesis, qualified limitation, and refusal to invent.
- Coverage benefit: directly tests the central corpus-only contract, citation integrity, synthesis, and hallucination resistance.
- Overlap: unsupported can coincide with D1 out-of-scope; partial support can interact with multi-intent. The evidence state, however, remains independent of intent/clarity.
- Risk if omitted: the dataset cannot intentionally test fabricated claims/citations or missing cross-document synthesis.
- Test A: PASS — evidence strategy changes materially.
- Test B: PASS — not wording/style.
- Test C: MANAGEABLE OVERLAP — orthogonal when defined as evidence availability.
- Test D: PASS — creates critical grounding boundaries.
- Test E: PASS — required especially for challenge and high-risk cases.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for every concrete scenario assignment.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### D3 — Interaction clarity

- Values: clear, ambiguous terminology, multi-intent, referentially underspecified.
- Behavior change: the Tutor shifts among direct response, clarification/assumption disclosure, intent decomposition, and referent resolution.
- Coverage benefit: captures realistic chat behavior and wrong-interpretation failures.
- Overlap: ambiguous terminology and referentially underspecified are both ambiguity subtypes. They remain meaningfully distinct if the former means multiple plausible concepts and the latter means a missing referent.
- Risk if omitted: synthetic clear questions dominate and the Tutor is never tested on clarifying or decomposing requests.
- Test A: PASS — dialogue action changes by value.
- Test B: PASS — style may accompany these values but is not their definition.
- Test C: MODERATE INTERNAL OVERLAP — use the subtype definitions above during combination design.
- Test D: PASS — adds wrong-intent and dropped-intent boundaries.
- Test E: PASS — essential for challenge coverage; clear supports representative coverage.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### D4 — Premise validity

- Values: valid premise, misleading or false premise.
- Behavior change: the Tutor either proceeds normally or corrects/qualifies the premise before addressing the request.
- Coverage benefit: tests misconception reinforcement, sycophancy, and confident continuation from a false assumption.
- Overlap: a false premise can also be partially supported or unsupported under D2, but premise validity concerns the learner's assertion rather than corpus availability.
- Risk if omitted: the Tutor may appear grounded while endorsing a harmful misconception.
- Test A: PASS — response ordering and content policy change.
- Test B: PASS — not a style distinction.
- Test C: MANAGEABLE OVERLAP — define independently from evidence availability.
- Test D: PASS — adds a meaningful high-risk product boundary.
- Test E: PASS — valid premise supports representative cases; false premise supports challenge/high-risk cases.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

## Value reviews

### V01 — In-scope concept

- Parent: D1 Question intent.
- Scenario: learner requests an explanation of a course-domain evaluation concept.
- Expected behavior: explain using available supported evidence and avoid outside additions.
- Difference from siblings: asks for meaning, not comparison/application, assessed-work completion, or outside-scope information.
- Risk: unsupported material may be presented as course content.
- Overlap: usually combines with D2 support and D3 clarity; no material duplication.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for any named concept.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V02 — Comparison

- Parent: D1 Question intent.
- Scenario: learner asks how two evaluation concepts or methods differ.
- Expected behavior: contrast only supported dimensions and preserve meaningful distinctions.
- Difference from siblings: requires relational synthesis rather than a standalone definition or application.
- Risk: learner may select or apply the wrong method.
- Overlap: may require D2 multi-source support, but comparison intent does not imply it.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for specific concept pairs.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V03 — Application

- Parent: D1 Question intent.
- Scenario: learner asks how to apply a taught evaluation method to a described situation.
- Expected behavior: map supported principles to known facts and disclose missing-context limits.
- Difference from siblings: requires contextual transfer, not definition or contrast.
- Risk: advice may depend on invented project facts.
- Overlap: can interact with D2 partial support and D3 multi-intent; still a distinct response goal.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for any named method.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V04 — Answer-seeking

- Parent: D1 Question intent.
- Scenario: learner requests a direct answer to assessed work.
- Expected behavior: support learning according to the actual course policy without inventing an integrity rule.
- Difference from siblings: correct handling depends on a learning/assessment boundary, not merely requested content.
- Risk: the Tutor may complete assessed work improperly or falsely claim a policy.
- Overlap: can resemble application if the assessment framing is absent.
- Issue: the authoritative academic-integrity/course policy is not available, so the expected action is underspecified beyond “do not invent policy.”
- AI recommendation: `RECOMMEND REVISE` — retain the behavioral category only after the human specifies the intended product/course boundary or reframes it as “direct-answer request with policy-dependent handling.”
- Human decision: `PENDING HUMAN REVIEW`.

### V05 — Out-of-scope

- Parent: D1 Question intent.
- Scenario: learner requests material unrelated to the AI-evaluations course domain.
- Expected behavior: state the boundary and redirect rather than answer from general knowledge.
- Difference from siblings: the requested topic itself is outside product scope.
- Risk: off-corpus information may be mistaken for official course material.
- Overlap: often also D2 unsupported; retain both labels because scope and evidence are different properties.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V06 — Fully supported in one source

- Parent: D2 Corpus support.
- Scenario: all necessary explanation and qualifications occur in one source.
- Expected behavior: ground the answer in that source and cite it accurately.
- Difference from siblings: no synthesis or limitation is needed.
- Risk: incorrect attribution makes the answer unverifiable.
- Overlap: none significant; combines with many intents.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` until a real document is mapped.
- AI recommendation: `RECOMMEND APPROVE` at behavioral level.
- Human decision: `PENDING HUMAN REVIEW`.

### V07 — Supported across multiple sources

- Parent: D2 Corpus support.
- Scenario: necessary evidence is distributed across at least two corpus sources.
- Expected behavior: synthesize compatible evidence with accurate attribution and no unsupported additions.
- Difference from siblings: requires cross-source integration.
- Risk: incomplete synthesis may create a misleading rule or false consensus.
- Overlap: comparisons/applications may often use it but do not require it.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` until multiple real sources are mapped.
- AI recommendation: `RECOMMEND APPROVE` at behavioral level.
- Human decision: `PENDING HUMAN REVIEW`.

### V08 — Partially supported

- Parent: D2 Corpus support.
- Scenario: corpus supports the core request but not a requested detail, example, or extension.
- Expected behavior: separate supported content from the unsupported portion and state the limitation.
- Difference from siblings: neither complete support nor total non-support applies.
- Risk: the unsupported portion may be disguised as grounded content.
- Overlap: multi-intent questions can create partial support, but partiality can also occur in one intent.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for each concrete boundary.
- AI recommendation: `RECOMMEND APPROVE` at behavioral level.
- Human decision: `PENDING HUMAN REVIEW`.

### V09 — Unsupported

- Parent: D2 Corpus support.
- Scenario: no corpus evidence supports the requested information.
- Expected behavior: state non-support and avoid fabricated facts or citations.
- Difference from siblings: no supported answer content is available.
- Risk: fabrication may falsely increase learner trust.
- Overlap: may coincide with D1 out-of-scope but can also be an in-scope corpus gap.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED`; absence cannot be proven without the authoritative corpus.
- AI recommendation: `RECOMMEND APPROVE` at behavioral level.
- Human decision: `PENDING HUMAN REVIEW`.

### V10 — Clear

- Parent: D3 Interaction clarity.
- Scenario: one explicit request identifies the topic and desired operation.
- Expected behavior: answer directly without unnecessary clarification.
- Difference from siblings: no interpretation, decomposition, or referent resolution is required.
- Risk: needless clarification frustrates learners; misreading wastes study time.
- Overlap: none material.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V11 — Ambiguous terminology

- Parent: D3 Interaction clarity.
- Scenario: a term such as “the matrix” plausibly refers to multiple course concepts.
- Expected behavior: ask a targeted clarification or transparently state a bounded assumption.
- Difference from siblings: ambiguity comes from multiple meanings, not a missing prior referent.
- Risk: Tutor confidently explains the wrong concept.
- Overlap: close to V13; preserve the semantic-versus-referential distinction.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V12 — Multi-intent

- Parent: D3 Interaction clarity.
- Scenario: one message requests two or more distinct operations.
- Expected behavior: structure and address each intent or explicitly identify what cannot be addressed.
- Difference from siblings: the issue is multiplicity, not uncertainty about meaning/reference.
- Risk: a silently dropped intent produces an incomplete answer.
- Overlap: can produce D2 partial support; still a distinct interaction structure.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V13 — Referentially underspecified

- Parent: D3 Interaction clarity.
- Scenario: learner refers to “that one” or “the earlier part” without an identifiable antecedent.
- Expected behavior: resolve the referent or state the assumption before answering.
- Difference from siblings: missing antecedent rather than ambiguous terminology.
- Risk: the response attaches to the wrong prior concept.
- Overlap: close to V11; definitions must remain explicit during combination review.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V14 — Valid premise

- Parent: D4 Premise validity.
- Scenario: the learner's stated relationship or assumption is consistent with the available evidence.
- Expected behavior: proceed without unnecessary correction.
- Difference from sibling: no misconception intervention is needed.
- Risk: unwarranted correction can confuse a learner who was already correct.
- Overlap: typically a baseline value across other dimensions.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for any concrete premise.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

### V15 — Misleading or false premise

- Parent: D4 Premise validity.
- Scenario: learner asserts an incorrect guarantee or relationship and asks a follow-on question.
- Expected behavior: correct or qualify the premise using evidence before continuing.
- Difference from sibling: misconception handling is required.
- Risk: Tutor reinforces a systematic misunderstanding.
- Overlap: may combine with D2 partial/unsupported, but premise status is independently meaningful.
- Corpus-specific claim: `UNVERIFIED — CORPUS REQUIRED` for any concrete premise/correction.
- AI recommendation: `RECOMMEND APPROVE`.
- Human decision: `PENDING HUMAN REVIEW`.

## Human decision summary

| ID | Type | Name/Value | AI Recommendation | Main Reason | Human Decision |
| --- | --- | --- | --- | --- | --- |
| D1 | Dimension | Question intent | RECOMMEND APPROVE | Distinct learner goals change response mode and scope handling | PENDING HUMAN REVIEW |
| D2 | Dimension | Corpus support | RECOMMEND APPROVE | Evidence availability changes grounding/synthesis/refusal behavior | PENDING HUMAN REVIEW |
| D3 | Dimension | Interaction clarity | RECOMMEND APPROVE | Clarity changes direct-answer, clarification, and decomposition behavior | PENDING HUMAN REVIEW |
| D4 | Dimension | Premise validity | RECOMMEND APPROVE | False premises require correction before continuation | PENDING HUMAN REVIEW |
| V01 | Value | In-scope concept | RECOMMEND APPROVE | Representative explanation behavior | PENDING HUMAN REVIEW |
| V02 | Value | Comparison | RECOMMEND APPROVE | Requires supported contrast | PENDING HUMAN REVIEW |
| V03 | Value | Application | RECOMMEND APPROVE | Requires contextual transfer with limits | PENDING HUMAN REVIEW |
| V04 | Value | Answer-seeking | RECOMMEND REVISE | Correct behavior depends on unavailable course/integrity policy | PENDING HUMAN REVIEW |
| V05 | Value | Out-of-scope | RECOMMEND APPROVE | Critical product-scope boundary | PENDING HUMAN REVIEW |
| V06 | Value | Fully supported in one source | RECOMMEND APPROVE | Tests direct grounding and citation | PENDING HUMAN REVIEW |
| V07 | Value | Supported across multiple sources | RECOMMEND APPROVE | Tests synthesis and attribution | PENDING HUMAN REVIEW |
| V08 | Value | Partially supported | RECOMMEND APPROVE | Tests supported/unsupported separation | PENDING HUMAN REVIEW |
| V09 | Value | Unsupported | RECOMMEND APPROVE | Tests non-fabrication boundary | PENDING HUMAN REVIEW |
| V10 | Value | Clear | RECOMMEND APPROVE | Necessary direct-answer baseline | PENDING HUMAN REVIEW |
| V11 | Value | Ambiguous terminology | RECOMMEND APPROVE | Tests semantic clarification | PENDING HUMAN REVIEW |
| V12 | Value | Multi-intent | RECOMMEND APPROVE | Tests intent decomposition/completeness | PENDING HUMAN REVIEW |
| V13 | Value | Referentially underspecified | RECOMMEND APPROVE | Tests missing-referent handling | PENDING HUMAN REVIEW |
| V14 | Value | Valid premise | RECOMMEND APPROVE | Baseline without unnecessary correction | PENDING HUMAN REVIEW |
| V15 | Value | Misleading or false premise | RECOMMEND APPROVE | Tests misconception correction | PENDING HUMAN REVIEW |

## Human decision block

Copy this block into your reply and change any line to `REJECTED BY HUMAN` or `REVISE` as needed. The prefilled text is only an input convenience requested for this session; it is not recorded as a decision until you send it back.

```text
D1 = HUMAN APPROVED
D2 = HUMAN APPROVED
D3 = HUMAN APPROVED
D4 = HUMAN APPROVED

V01 = HUMAN APPROVED
V02 = HUMAN APPROVED
V03 = HUMAN APPROVED
V04 = HUMAN APPROVED
V05 = HUMAN APPROVED
V06 = HUMAN APPROVED
V07 = HUMAN APPROVED
V08 = HUMAN APPROVED
V09 = HUMAN APPROVED
V10 = HUMAN APPROVED
V11 = HUMAN APPROVED
V12 = HUMAN APPROVED
V13 = HUMAN APPROVED
V14 = HUMAN APPROVED
V15 = HUMAN APPROVED
```

Combination generation allowed now: **NO**. It becomes allowed only after the human returns explicit decisions and all approved/revised coverage is internally consistent.
