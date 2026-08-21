# Phase 1 Human Decision Packet

- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Decision Date**: `2026-08-21`
- **Overall Decision**: `HUMAN APPROVED`
- **Governance State**: `LOCKED BY HUMAN REVIEW`

## 1. Dimensions (D1 - D4)

| ID | Dimension | Why behavior changes | AI recommendation | Human decision |
| --- | --- | --- | --- | --- |
| **D1** | Question intent | The correct response mode changes among explanation, comparison, application, learning-boundary handling, and scope refusal/redirect | RECOMMEND APPROVE | **HUMAN APPROVED** |
| **D2** | Corpus support | The grounding strategy changes among one-source citation, multi-source synthesis, partial-support caveat, and explicit non-support | RECOMMEND APPROVE | **HUMAN APPROVED** |
| **D3** | Interaction clarity | The Tutor must choose among direct response, clarification/assumption disclosure, intent decomposition, and reference resolution | RECOMMEND APPROVE | **HUMAN APPROVED** |
| **D4** | Premise validity | A valid premise permits normal response, while a false/misleading premise requires correction or qualification first | RECOMMEND APPROVE | **HUMAN APPROVED** |

---

## 2. Values (V01 - V15)

| Value ID | Dimension | Value | Expected behavior change | Risk | Human decision |
| --- | --- | --- | --- | --- | --- |
| **V01** | D1 Question intent | In-scope concept | Explain using supported evidence without outside additions | Learner may receive ungrounded course content | **HUMAN APPROVED** |
| **V02** | D1 Question intent | Comparison | Contrast supported differences without collapsing concepts | Learner may apply the wrong technique | **HUMAN APPROVED** |
| **V03** | D1 Question intent | Application | Apply supported principles while disclosing missing-context limits | Advice may rely on invented project facts | **HUMAN APPROVED** |
| **V04** | D1 Question intent | Answer-seeking | Support learning via Socratic guidance without inventing integrity rules | Tutor may undermine learning or fabricate policy | **HUMAN APPROVED** |
| **V05** | D1 Question intent | Out-of-scope | State the scope boundary and redirect rather than use general knowledge | Off-corpus content may be mistaken for official material | **HUMAN APPROVED** |
| **V06** | D2 Corpus support | Fully supported in one source | Ground and cite the identified single source accurately | Wrong citation makes the answer unverifiable | **HUMAN APPROVED** |
| **V07** | D2 Corpus support | Supported across multiple sources | Synthesize necessary evidence with correct attribution | Partial synthesis may create a misleading rule | **HUMAN APPROVED** |
| **V08** | D2 Corpus support | Partially supported | Separate supported claims from unsupported requested details | Unsupported details may appear course-grounded | **HUMAN APPROVED** |
| **V09** | D2 Corpus support | Unsupported | State non-support and avoid facts or citations not in the corpus | Fabrication may falsely increase learner trust | **HUMAN APPROVED** |
| **V10** | D3 Interaction clarity | Clear | Answer the single explicit intent directly | Misreading or needless clarification wastes study time | **HUMAN APPROVED** |
| **V11** | D3 Interaction clarity | Ambiguous terminology | Clarify or disclose a bounded assumption before answering | Tutor may explain the wrong concept confidently | **HUMAN APPROVED** |
| **V12** | D3 Interaction clarity | Multi-intent | Structure and address each intent without silently dropping one | Learner receives an incomplete answer | **HUMAN APPROVED** |
| **V13** | D3 Interaction clarity | Referentially underspecified | Resolve the missing referent or disclose the assumption | Answer may attach to the wrong prior topic | **HUMAN APPROVED** |
| **V14** | D4 Premise validity | Valid premise | Proceed without unnecessary correction | Unwarranted correction may confuse the learner | **HUMAN APPROVED** |
| **V15** | D4 Premise validity | Misleading or false premise | Correct/qualify the premise before addressing the request | Tutor may reinforce a systematic misconception | **HUMAN APPROVED** |

---

## 3. V04 Pedagogical Policy Lock

- **Policy Status**: **`HUMAN APPROVED`**
- **Approved Policy Definition**:
  > *Tutor đóng vai trò Socratic tutor:*
  > - *Giải thích nguyên lý cốt lõi của bài học.*
  > - *Đưa ra gợi ý (hints) và câu hỏi gợi mở.*
  > - *Giúp người học tự tư duy và suy luận ra kết quả.*
  > - *Không giải hộ / làm thay bài thi hoặc bài lab.*
  > - *Không giả mạo quy chế không tồn tại trong corpus.*
  > - *Không tự tuyên bố chính sách trường học khi không có bằng chứng tương ứng trong giáo trình.*
