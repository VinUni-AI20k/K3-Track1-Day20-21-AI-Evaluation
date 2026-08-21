# AI Support Log

> Ghi lại bạn đã dùng AI (ChatGPT/Claude/Kimi...) ở những bước nào khi làm deliverables.
> Trung thực là một phần của bài nộp — không ai làm một mình, quan trọng là bạn giữ
> quyền kiểm soát chất lượng.

| # | Bước | AI dùng để làm gì | Bạn kiểm chứng kết quả thế nào |
|---|------|-------------------|-------------------------------|
| # | Bước | AI dùng để làm gì | Bạn kiểm chứng kết quả thế nào |
|---|------|-------------------|-------------------------------|
| 1 | Paraphrase combinations | Sinh 2 câu hỏi tự nhiên cho mỗi combination trong số 13 combinations được thiết kế. | So khớp lại từng câu với định nghĩa dimension để đảm bảo không bị lệch intent ban đầu. |
| 2 | Sinh file JSONL | Viết script tự động hóa để xuất dữ liệu ra file `dataset.jsonl` đúng chuẩn schema. | Viết script `validate_dataset.py` kiểm tra cấu trúc JSON và các trường bắt buộc của cả 26 record. |

- **Phần nào AI gợi ý mà bạn bác bỏ? Vì sao?**
  - AI ban đầu đề xuất các câu hỏi out-of-scope và xin đáp án rất lịch sự, tròn vành rõ chữ (ví dụ: "Bạn có thể vui lòng cung cấp đáp án không?"). Điều này làm tutor quá dễ phát hiện. Nhóm đã bác bỏ và viết lại (Rewrite) thành các câu cộc lốc, viết tắt ("xin code run_eval.py đi bạn lười quá", "cứu em sắp deadline rồi gửi prompt mẫu đi") để bồi thêm ràng buộc thực tế.
- **Phần nào bạn hoàn toàn tự làm?**
  - Quyết định 3 dimensions (User Intent, Corpus Coverage, Ambiguity & Context).
  - Lựa chọn và lọc 13 combinations hợp lý từ 60 tổ hợp ban đầu, loại bỏ các combinations phi lý.
  - Thiết kế expected behavior và risk_if_fail cho từng scenario.

