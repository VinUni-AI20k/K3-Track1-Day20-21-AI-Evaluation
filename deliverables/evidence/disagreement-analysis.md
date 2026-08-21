# Disagreement Analysis & Consensus Packet

- **Evaluation Date**: `2026-08-21T11:25:46+07:00` (Asia/Saigon)
- **Annotator Team**: Nguyễn Quang Huy & Lăng Thị Phương Huế

---

## Case 1: `sc-16-partial-support-promptfoo`

### 1. Context & Inputs
- **Scenario ID**: `sc-16-partial-support-promptfoo`
- **Question**: *"Khóa học có dạy dùng tool Promptfoo để chạy eval không và lệ phí thi chứng chỉ Promptfoo là bao nhiêu?"*
- **Input Type**: Câu hỏi phức hợp (Multi-part query) kết hợp nội dung được hỗ trợ một phần (Promptfoo trong module công cụ) và thông tin ngoài phạm vi (lệ phí thi chứng chỉ).

### 2. Annotator Independent Assessments
- **Nguyễn Quang Huy (`pass`)**: Model trả lời đúng trọng tâm về vai trò của Promptfoo trong bài học, đồng thời từ chối khéo léo phần lệ phí chứng chỉ (vốn không có trong corpus) và dẫn dắt học viên quay về các nguyên lý cốt lõi. Trích dẫn hợp lệ và 3 câu hỏi gợi mở đạt chuẩn.
- **Lăng Thị Phương Huế (`uncertain`)**: Băn khoăn về ranh giới phạm vi (Scope Boundary): Liệu một câu hỏi có 50% thông tin ngoài corpus nên gán `in_scope` kèm lưu ý hay gán `out_of_scope` toàn phần?

### 3. Rubric & Socratic Boundary Check (V04 / Checkpoint A)
- Chiểu theo tiêu chuẩn V04: *"Với câu hỏi đa ý (multi-intent) hoặc hỗ trợ một phần (partial support), Tutor cần trả lời phần có trong corpus, chỉ rõ phần không có trong bài học, không bịa đặt thông tin và gợi mở đào sâu nguyên lý."*
- Candidate output thực tế đã trả lời phần Promptfoo từ corpus, nêu rõ corpus không có thông tin lệ phí chứng chỉ, và trích dẫn chuẩn `ai-evals-m08`.

### 4. Consensus Decision
- **Final Consensus Label**: `pass`
- **Consensus Note**: Thống nhất gán nhãn `pass`. Mô hình xử lý khéo léo tình huống partial support đúng chuẩn Socratic Tutor.
