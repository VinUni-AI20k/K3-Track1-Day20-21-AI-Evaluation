# Routing Table & Decision Matrix

- **Purpose**: Phân luồng từng tiêu chí đánh giá vào đúng làn thực thi (Code Check vs LLM Judge vs Con người).
- **Core Principle**: 
  - Tiêu chí mang tính định danh, cấu trúc, cú pháp deterministic hoặc chi phí $0 -> **Code Check**.
  - Tiêu chí ngữ nghĩa, bám sát nội dung, phát hiện ảo giác phức tạp -> **LLM Judge** (sau khi đã calibrate).
  - Tiêu chí chính sách biên, tranh chấp rubric, quyết định release -> **Con người (Human/Expert)**.

## Routing Decision Matrix

| Tiêu chí | Primary Lane | Supporting Lane | Lý do & Căn cứ kỹ thuật |
|---|---|---|---|
| **`schema_valid`** | **Code Check** | Không | 100% deterministic, kiểm tra sự tồn tại của 4 trường bắt buộc (`scope`, `answer`, `sources`, `followup_questions`) và tính hợp lệ JSON không tốn token API. |
| **`citation_exists`** | **Code Check** | Không | So khớp trực tiếp `(doc_id, section_id)` với 341 sections thực tế trong corpus. Không cần LLM đoán mò. |
| **`quote_verbatim`** | **Code Check** | Không | So sánh chuỗi token chuẩn hóa của trích dẫn với section text trong corpus. Phát hiện ngay quote bịa đặt. |
| **`scope_sources_consistency`** | **Code Check** | Không | Kiểm tra ràng buộc logic: `out_of_scope` thì sources phải rỗng; `in_scope` thì sources phải >= 1. |
| **`followup_quality`** | **Code Check** | LLM Judge | Code check kiểm tra số lượng (1–3 câu), định dạng chuỗi không rỗng. LLM Judge hỗ trợ đánh giá tính gợi mở sư phạm. |
| **`sources_no_duplicates`** | **Code Check** | Không | Kiểm tra không có nguồn trích dẫn trùng lặp trong danh sách `sources`. |
| **`answer_groundedness`** | **LLM Judge** | Human Audit (10%) | Đánh giá ngữ nghĩa: liệu mọi luận điểm trong `answer` có thực sự được chứng minh bởi `sources` hay không; phát hiện bẫy nịnh bợ (sycophancy) khi gặp tiền đề sai. Cần calibrate >= 2 vòng. |
| **`scope_handling`** | **LLM Judge** | Code Check | Đánh giá câu trả lời out-of-scope có lịch sự từ chối và định hướng đúng chủ đề môn học hay không. |
| **`academic_integrity_boundary`** | **Human Policy / Socratic** | LLM Judge | Xử lý các tình huống xin đáp án trực tiếp; hướng dẫn gợi mở Socratic không làm thay bài. |
| **`final_release_verdict`** | **Human / PM** | Scorecard | Quyết định Ship / Ship with conditions / Hold dựa trên scorecard định lượng và phân tích lỗi trọng yếu. |
