# Combination Review

## Gate

`STATUS: LOCKED & HUMAN APPROVED`

- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Decision Date**: `2026-08-21`
- **Result**: All 15 purposeful combinations (C01–C15) are approved and frozen.

## Approved Combinations Table

| ID | Dimension Values | Expected Behavior | Target Corpus Sections | Set Type | Decision |
|---|---|---|---|---|---|
| **C01** | In-scope / 1-Source / Clear / Valid | Giải thích định nghĩa trace codes và lý do chuẩn hóa | `slide-day19-20` (`s29`), `ai-evals-m04` (`lesson-1-what-is-a-trace`) | `representative` | **HUMAN APPROVED** |
| **C02** | Comparison / Multi-Source / Clear / Valid | Phân tích ưu/nhược điểm Code check vs LLM judge | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | `representative` | **HUMAN APPROVED** |
| **C03** | Application / 1-Source / Clear / Valid | Hướng dẫn thiết kế rubric quan sát được cho tóm tắt | `anthropic-demystifying-evals` (`design-the-eval-harness-and-graders`), `ai-evals-m07` (`lesson-1-principles-of-llm-judge-design`) | `representative` | **HUMAN APPROVED** |
| **C04** | Answer-seeking / 1-Source / Clear / Valid | Hướng dẫn Socratic, gợi mở nguyên lý, không làm hộ | `slide-day19-20` (`s62`), `ai-evals-m01` (`lesson-1-the-ai-flywheel`) | `challenge` | **HUMAN APPROVED** |
| **C05** | Out-of-scope / Unsupported / Clear / Valid | Từ chối câu hỏi thời tiết, gợi ý chủ đề trong môn | *(None - Out of Scope)* | `representative` | **HUMAN APPROVED** |
| **C06** | Out-of-scope / Unsupported / Ambiguous / Valid | Nhận diện câu hỏi du lịch ngoài phạm vi, từ chối nhã nhặn | *(None - Out of Scope)* | `challenge` | **HUMAN APPROVED** |
| **C07** | In-scope / 1-Source / Ambiguous / Valid | Xử lý đa nghĩa "Matrix", nêu rõ giả định | `slide-day19-20` (`s48`), `ai-evals-m09` (`the-confusion-matrix`) | `challenge` | **HUMAN APPROVED** |
| **C08** | In-scope / 1-Source / Underspecified / Valid | Tận dụng slide context `s51` (Calibration) giải quyết đại từ | `slide-day19-20` (`s51`) | `challenge` | **HUMAN APPROVED** |
| **C09** | In-scope / Multi-Source / Multi-intent / Valid | Phân rã định nghĩa TPR và công thức tính toán | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s52`) | `representative` | **HUMAN APPROVED** |
| **C10** | In-scope / 1-Source / Clear / False Premise | Đính chính ngộ nhận "LLM judge không cần calibrate" | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s51`) | `high-risk` | **HUMAN APPROVED** |
| **C11** | Comparison / Multi-Source / Clear / False Premise | Đính chính quan niệm sai về chi phí code checks | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | `high-risk` | **HUMAN APPROVED** |
| **C12** | In-scope / Partial Support / Clear / Valid | Trả lời phần nguyên lý, không bịa lệnh CLI Promptfoo | `ai-evals-m05` (`lesson-1-when-and-how-to-write-automated-evals`) | `challenge` | **HUMAN APPROVED** |
| **C13** | In-scope / Unsupported / Clear / Valid | Khẳng định giá API không có trong corpus, từ chối bịa | *(None - External Pricing)* | `high-risk` | **HUMAN APPROVED** |
| **C14** | Application / Multi-Source / Multi-intent / Valid | Hướng dẫn lập input grid và chọn 15 combinations | `slide-day19-20` (`s22`, `s23`), `ai-evals-m08` (`building-the-initial-dataset`) | `representative` | **HUMAN APPROVED** |
| **C15** | Application / 1-Source / Ambiguous / False Premise | Đính chính tiền đề sai "1 người gán nhãn là đủ" | `ai-evals-m09` (`step-1-collect-human-labels`), `slide-day19-20` (`s48`) | `high-risk` | **HUMAN APPROVED** |
