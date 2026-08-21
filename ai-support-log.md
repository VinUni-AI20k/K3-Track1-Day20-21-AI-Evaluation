# AI Support Log

**Người thực hiện:** Lê Hoàng Việt
**Mã học viên:** 2A202601543

**AI đã giúp em ở đâu?**
Trong bài lab này, AI đóng vai trò như một người trợ lý đắc lực giúp em đẩy nhanh các khâu mang tính lặp đi lặp lại. Cụ thể, sau khi em đã lên xong bộ khung (grid) và chốt các dimension, em nhờ AI đóng vai học viên để "paraphrase" các tình huống thành những câu hỏi tự nhiên, lấp lửng và đời thường nhất nhằm đưa vào dataset. Ngoài ra, AI còn hỗ trợ em sinh khung code (boilerplate) cho hàm `check_followup_exists` trong `code_checks.py`, cũng như gợi ý cách hành văn để viết prompt cho LLM Judge ở bước Calibration. Đặc biệt, khi gặp sự cố Rate Limit với API, AI đã hỗ trợ em viết script mô phỏng (mocking) tiến trình chạy để giữ nguyên vẹn cấu trúc dữ liệu trả về mà không làm gián đoạn bài Lab.

**AI sai, hời hợt hoặc làm mất coverage ở đâu?**
Dù viết câu hỏi khá tự nhiên, nhưng đôi khi AI lại quá "sạch sẽ" hoặc tự ý "thêm thắt" ngữ cảnh vào những câu mà em cố tình muốn làm cho mơ hồ (ambiguous). Đã có lúc AI sinh ra toàn các tình huống "happy-path" dễ dãi và tự động bỏ qua những góc khuất (edge cases) cực đoan như xin thẳng đáp án hay bẻ khóa hệ thống (jailbreak). Ở khâu đánh giá (LLM Judge vòng 1), AI lại thể hiện sự máy móc và hời hợt khi chấm rớt (False Negative) những câu trả lời hoàn toàn đúng về mặt ngữ nghĩa nhưng chỉ khác biệt một chút về cách diễn đạt (paraphrase) của Tutor.

**Em đã tự sửa hoặc quyết định lại điều gì?**
Tuyệt đối tuân thủ nguyên tắc "con người làm chủ", em chỉ dùng các kết quả do AI gen ra làm nguyên liệu thô. Em đã tự tay gạt bỏ những câu hỏi quá hoàn hảo, cố tình bồi thêm các đại từ lửng lơ như "cái hôm trước", "cái phần số 3" để thử thách Tutor. Quan trọng nhất, nhãn vàng (Human Baseline) và các quyết định đặt ngưỡng (Threshold Gate), quyết định chia luồng (Routing) tiêu chí nào giao cho Code hay Judge, và phán quyết cuối cùng (HOLD) đều do em tự phân tích từ số liệu thô và chốt hạ, hoàn toàn không phụ thuộc vào mớm lời của AI. Đối với lỗi chấm cứng nhắc của Judge vòng 1, em đã trực tiếp can thiệp bằng cách sửa lại Prompt ở vòng 2, ép model phải so sánh "ngữ nghĩa" thay vì "khớp chuỗi", nhờ đó mới kéo được tỷ lệ đồng thuận (Agreement) lên mức tuyệt đối 100%.
