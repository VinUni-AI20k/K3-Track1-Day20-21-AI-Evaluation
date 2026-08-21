# Track1_Day21_MHV_HoVaTen

## 1. Thông tin cá nhân và nhóm
- **Họ và tên:** Lê Hoàng Việt
- **Mã học viên (MHV):** 2A202601543
- **Nhóm:** (Làm cá nhân/Nhóm)
- **Repo đánh giá:** VLearn AI Tutor - AI Evaluation Capstone

## 2. Sơ đồ Sáu Phase và Artifacts
Dự án được thực hiện qua 6 bước (phases) chuẩn chỉnh của một Evaluation Loop:

1. **P1: Thiết kế Coverage & Sinh Dataset**
   - Tạo lưới input 3 dimensions: Intent (In-scope, Out-of-scope, Ambiguous, Adversarial) x User Persona x Complexity.
   - *Artifacts:* `deliverables/evidence/dataset-v1.jsonl` (20 kịch bản).
2. **P2: Human Baseline (Gán nhãn vàng)**
   - Chạy hệ thống bằng Model LLM để thu thập phản hồi, xem xét report.html.
   - Chấm điểm thủ công, đóng vai trò chuyên gia tạo nhãn chuẩn (Golden labels).
   - *Artifacts:* `deliverables/evidence/results-v1.jsonl`, `deliverables/evidence/labels.csv`.
3. **P3: Xây dựng Rubric & Routing Map**
   - Phân hoạch tiêu chí: `schema_valid`, `quote_verbatim`, `followup_exists` (giao cho Code Checks) và `groundedness` (giao cho LLM Judge).
   - *Artifacts:* Định nghĩa rõ trong `deliverables/REPORT.md`.
4. **P4: Scale & Calibrate Judge**
   - Thêm quy tắc `check_followup_exists` bằng Python (nhanh, rẻ, chính xác 100%).
   - Tinh chỉnh LLM Judge qua 2 vòng để khắc phục lỗi False Negative (đánh trượt oan do paraphrase).
   - *Artifacts:* `judge-prompt-v1.md`, `judge-prompt-v2.md`, `verdicts-v1.jsonl`, `verdicts-v2.jsonl`.
5. **P5: Đọc kết quả & Đặt ngưỡng (Scorecard & Gate)**
   - Ngưỡng (Threshold): `schema_valid` = 100%, `groundedness` >= 95%, `quote_verbatim` = 100%.
   - *Artifacts:* Scorecard trong `deliverables/REPORT.md`.
6. **P6: Verdict & Báo cáo cuối**
   - Chốt quyết định "HOLD" (không tung ra thị trường) vì lỗi Hallucinate Quote.
   - *Artifacts:* Phần 7 của `deliverables/REPORT.md`.

## 3. Đóng góp của cá nhân
Là người thực hiện toàn bộ vòng lặp (do tính chất làm cá nhân/lead dự án):
- Thiết kế coverage, tạo prompt để sinh các trường hợp nhiễu (OOS) và thử thách (Adversarial).
- Tham gia gán nhãn vàng và định nghĩa bộ Rule/Rubric.
- Implement rule check `followup_exists` vào code Python.
- Viết báo cáo quyết định Hold/Ship dựa trên số liệu thực tế, setup tracing trên LangSmith.

## 4. Verdict của nhóm và lý do
- **Quyết định:** **HOLD (Chưa tung ra)**
- **Lý do (Dựa trên Scorecard):** Mặc dù hệ thống đáp ứng tốt việc trả về JSON chuẩn (`schema_valid` = 100%) và không nói bịa kiến thức ngoài luồng (`groundedness` tốt), nhưng tiêu chí `quote_verbatim` (yêu cầu trích xuất nguyên văn substring) lại bị fail nặng nề (tỉ lệ pass chỉ 25%). Mô hình liên tục tự ý diễn đạt lại (paraphrase) câu quote. Vì VLearn yêu cầu tính học thuật và truy xuất nguyên bản cao, lỗi này không thể chấp nhận. 
- **Hành động tiếp theo:** Phải sửa System Prompt của Tutor, nghiêm cấm paraphrase quote, rồi chạy lại eval loop.

## 5. Điều sẽ mang về áp dụng cho dự án thật
1. **Thiết kế Evaluation Grid ngay từ đầu:** Giúp tránh thiên kiến (bias) khi chỉ test bằng vài câu dễ.
2. **Routing Map:** Không phải cái gì cũng quăng cho LLM làm Judge. Những logic tuyệt đối như Format, Len(array), Pattern Matching phải dùng Code Checks để tiết kiệm chi phí, giảm độ trễ và đạt độ chính xác 100%.
3. **Calibrate Judge (Mài dũa Giám khảo):** Không thể mù quáng tin LLM Judge ngay vòng đầu. Cần đối chiếu với nhãn vàng (Human Baseline) qua Confusion Matrix để sửa Judge Prompt cho tới khi chạm trần.
