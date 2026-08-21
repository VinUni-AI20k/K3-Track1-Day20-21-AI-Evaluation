# AI Support Log — Minh bạch hỗ trợ của Trí tuệ Nhân tạo

Tài liệu ghi chép trung thực phạm vi đóng góp của AI Assistant (Antigravity/Gemini) và quyền sở hữu quyết định của các thành viên trong nhóm thực hiện bài Lab Track 1 Day 20–21.

---

## 1. AI đã hỗ trợ ở những khâu nào?

1. **Re-Audit & Tích hợp Kỹ thuật**:
   - Quét cấu trúc repository, đối chiếu commit SHA của repository lớp (`ad2c1708e4db66df95b8d608c3fb15fc8a7c6a6f`), tích hợp an toàn các module `tutor/`, `eval/`, `tests/`, `deliverables/` mà không ghi đè dữ liệu lịch sử của người dùng trong `evals/phase1/`.
   - Chạy và xác minh 44 offline tests đạt 100% PASS trên môi trường Windows PowerShell (UTF-8).
2. **Corpus Integrity & Grounding Audit**:
   - Viết kịch bản kiểm tra toàn diện 18 tài liệu gốc và 341 searchable sections trong `tutor/corpus/manifest.json`, kiểm tra khả năng truy xuất thực tế bằng `tutor.kb_search_local`.
3. **Nâng cấp Hệ thống Test Harness**:
   - Nâng cấp `eval/code_checks.py`: bổ sung 3 code checks mới (`scope_sources_consistency`, `followup_quality`, `sources_no_duplicates`) và xây dựng bộ unit test suite `tests/test_code_checks.py` đạt 15/15 PASS.
   - Nâng cấp `eval/run_eval.py`: bảo toàn toàn bộ `metadata`, `expected_scope`, `note`, `timestamp` và `model_evaluated` để phục vụ phân tích lát cắt (slice analysis) theo D1–D4.
   - Nâng cấp `eval/judge.py`: hỗ trợ tham số dòng lệnh linh hoạt (`--prompt`, `--labels`, `--output`, `--criterion`), bổ sung tính toán ma trận nhầm lẫn chi tiết, Good-output recall (True Positive Rate), Bad-output catch rate (True Negative Rate) và danh sách ca lệch.
   - Bổ sung phòng thủ chống tấn công Prompt Injection trong `eval/judge_prompt.md`.
4. **Scaffolding & Soạn thảo tài liệu**:
   - Xây dựng candidate pool 15 tổ hợp kiểm thử (`C01`–`C15`), ma trận độ phủ `coverage-matrix.md`, bộ mẫu gán nhãn độc lập và khung báo cáo khoa học 7 mục trong `deliverables/REPORT.md`.

---

## 2. AI đã sai, hời hợt hoặc có nguy cơ làm mất coverage ở đâu?

1. **Nguy cơ suy diễn quy chế thi ảo (V04 Answer-seeking)**:
   - Ban đầu AI đề xuất kiểm tra quy chế học vụ (academic integrity policy), nhưng qua audit thực tế phát hiện 18 tài liệu corpus không có văn bản quy chế thi cử. Nếu AI tự do sinh câu trả lời, model có thể bịa đặt điều lệ không có trong bài học.
2. **Sai sót schema ban đầu**:
   - Trong quá trình viết script audit corpus, AI từng giả định trường `documents` và `path` thay vì đọc đúng schema `docs` và `file` trong `manifest.json`. AI đã tự chẩn đoán và khắc phục bằng cách đọc schema thật.
3. **Nguy cơ nhập nhằng giữa các chiều (Dimension Overlap)**:
   - AI từng có nguy cơ gộp `out-of-scope` (ngoài môn học) và `unsupported` (trong môn học nhưng thiếu tài liệu), hoặc gộp `ambiguous` (từ ngữ đa nghĩa) và `referentially underspecified` (thiếu đại từ chỉ định). Phân tích này đã được tách bạch rõ ràng để con người quyết định.

---

## 3. Người thực hiện đã tự sửa / quyết định lại những gì?

1. **Khóa định nghĩa hành vi V04**: Nhóm định nghĩa rõ hành vi mong đợi của Tutor khi gặp câu hỏi xin đáp án là: *Đóng vai trò gia sư Socratic, giải thích nguyên lý, hướng dẫn gợi mở, không làm hộ bài thi và không bịa đặt quy chế*.
2. **Quyết định phân luồng Routing**: Nhóm quyết định giữ ít nhất 6 tiêu chí kiểm tra bằng Code Check để tối ưu chi phí ($0 token) và tính khách quan, chỉ giao việc thẩm định ngữ nghĩa bám nguồn phức tạp cho LLM Judge sau khi đã calibrate.
3. **Thiết lập Ngưỡng chất lượng khóa trước Run**: Nhóm tự thiết lập các ngưỡng chất lượng (thresholds) mang tính nguyên tắc không thể đánh đổi (`schema 100%`, `citation exists ≥ 95%`, `0 OOS case bị trả lời như in-scope`).

---

## 4. Những phần nào hoàn toàn thuộc quyền sở hữu của con người (Human-Owned)?

- **Human Checkpoint A & B**: Quyết định phê duyệt 4 Dimensions, 15 Values và danh sách Combinations cuối cùng.
- **Phase 2 Baseline Labeling**: Gán nhãn độc lập từng cá nhân (`labels-huy.csv`, `labels-hue.csv`) và phiên thảo luận đồng thuận (`labels.csv`). AI tuyệt đối không gán nhãn thay thành viên.
- **Phase 6 Verdict Approval**: Quyết định phê duyệt phát hành cuối cùng (`Ship`, `Ship with conditions`, hoặc `Hold`) của sản phẩm.
