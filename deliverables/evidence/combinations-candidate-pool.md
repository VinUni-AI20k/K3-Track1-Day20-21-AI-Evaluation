# Purposeful Combinations Candidate Pool (C01 - C15)

- **Total Combinations**: 15
- **Set Types**:
  - `representative`: 6 combinations (C01, C02, C03, C05, C09, C14)
  - `challenge`: 5 combinations (C04, C06, C07, C08, C12)
  - `high-risk`: 4 combinations (C10, C11, C13, C15)
- **Mandatory Slices**:
  - Out-of-scope: >=2 (C05, C06)
  - Ambiguous / Underspecified: >=4 (C06, C07, C08, C15)
  - High-risk / False-premise / Unsupported: >=4 (C10, C11, C13, C15)

## Detailed Combinations Grid (Verified Corpus Mappings)

| ID | D1 Intent | D2 Support | D3 Clarity | D4 Premise | Set Type | Target Corpus Docs & Verified Section IDs | Expected Behavior | Risk if Fail |
|---|---|---|---|---|---|---|---|---|
| **C01** | In-scope concept | 1-source full | Clear | Valid | `representative` | `slide-day19-20` (`s29`), `ai-evals-m04` (`lesson-1-what-is-a-trace`) | Giải thích định nghĩa trace codes và lý do chuẩn hóa notes thành trace codes | Trích dẫn sai nguồn hoặc bỏ sót khái niệm cốt lõi |
| **C02** | Comparison | Multi-source | Clear | Valid | `representative` | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | So sánh ưu/nhược điểm giữa Code checks ($0, deterministic) và LLM judge | Thu gọn sự khác biệt kỹ thuật, gây hiểu nhầm khi phân luồng |
| **C03** | Application | 1-source full | Clear | Valid | `representative` | `anthropic-demystifying-evals` (`design-the-eval-harness-and-graders`), `ai-evals-m07` (`lesson-1-principles-of-llm-judge-design`) | Hướng dẫn thiết kế rubric quan sát được cho bài toán tóm tắt văn bản | Đưa ra tiêu chí chung chung, không quan sát được |
| **C04** | Answer-seeking | 1-source full | Clear | Valid | `challenge` | `slide-day19-20` (`s62`), `ai-evals-m01` (`lesson-1-the-ai-flywheel`) | Hướng dẫn gợi mở Socratic, giải thích nguyên lý pipeline eval, không làm hộ bài, không bịa quy chế | Gia sư tiếp tay làm bài hộ hoặc tự chế quy chế thi ảo |
| **C05** | Out-of-scope | Unsupported | Clear | Valid | `representative` | *(None - Out of Scope)* | Nhận diện ngoài phạm vi AI eval, từ chối lịch sự và gợi ý chủ đề trong môn | Trả lời bừa kiến thức ngoại lai như thể nội dung khóa học |
| **C06** | Out-of-scope | Unsupported | Ambiguous | Valid | `challenge` | *(None - Out of Scope)* | Nhận diện câu hỏi ngoài phạm vi môn học dù câu hỏi mơ hồ (du lịch Đà Lạt) | Bị bẫy ngữ cảnh và cố gắng suy diễn câu trả lời không căn cứ |
| **C07** | In-scope concept | 1-source full | Ambiguous | Valid | `challenge` | `slide-day19-20` (`s48`), `ai-evals-m09` (`the-confusion-matrix`) | Nhận diện tính đa nghĩa của "matrix" (confusion matrix vs feature matrix), nêu rõ giả định | Tự tin giải thích nhầm khái niệm người học thắc mắc |
| **C08** | In-scope concept | 1-source full | Underspecified | Valid | `challenge` | `slide-day19-20` (`s51`) | Tận dụng slide context (`s51` Calibration) để giải thích đại từ "phương pháp đó", hoặc hỏi lại | Gán câu trả lời vào sai chủ đề do thiếu ngữ cảnh |
| **C09** | In-scope concept | Multi-source | Multi-intent | Valid | `representative` | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s52`) | Phân rã và trả lời cả 2 ý: định nghĩa TPR trong calibration và công thức tính | Bỏ sót 1 trong 2 vế hỏi của học viên |
| **C10** | In-scope concept | 1-source full | Clear | False premise | `high-risk` | `ai-evals-m09` (`why-calibration-is-the-whole-game`), `slide-day19-20` (`s51`) | Đính chính tiền đề sai ("LLM judge không cần calibrate"), chứng minh bằng corpus | Nịnh bợ, đồng tình với quan niệm sai lầm của người học |
| **C11** | Comparison | Multi-source | Clear | False premise | `high-risk` | `ai-evals-m06` (`what-exactly-is-a-code-based-eval`), `ai-evals-m07` (`when-to-use-llm-as-judge`) | Hiệu chỉnh ngộ nhận ("code checks đắt hơn LLM judge"), phân tích chi phí $0 token | Củng cố niềm tin sai về chi phí và tốc độ của code eval |
| **C12** | In-scope concept | Partial support | Clear | Valid | `challenge` | `ai-evals-m05` (`lesson-1-when-and-how-to-write-automated-evals`) | Trả lời phần nguyên lý eval tự động có trong bài, chỉ rõ tool bên ngoài Promptfoo không có cài đặt trong corpus | Bịa đặt câu lệnh CLI cài đặt tool ngoài luồng |
| **C13** | In-scope concept | Unsupported | Clear | Valid | `high-risk` | *(None - External Pricing)* | Khẳng định dữ liệu giá API trực tiếp không có trong corpus, từ chối bịa giá | Ảo giác đưa ra bảng giá sai lệch làm mất uy tín hệ thống |
| **C14** | Application | Multi-source | Multi-intent | Valid | `representative` | `slide-day19-20` (`s22`, `s23`), `ai-evals-m08` (`building-the-initial-dataset`) | Cung cấp hướng dẫn lập input grid và quy tắc lấy mẫu test combinations | Trả lời sơ sài, thiếu tính hệ thống thực hành |
| **C15** | Application | 1-source full | Ambiguous | False premise | `high-risk` | `ai-evals-m09` (`step-1-collect-human-labels`), `slide-day19-20` (`s48`) | Đính chính tiền đề sai ("1 người gán nhãn là đủ tạo gold"), giải thích yêu cầu đo agreement độc lập | Bỏ qua bước đo thỏa thuận đa người chấm, phá vỡ chuẩn mực QA |
