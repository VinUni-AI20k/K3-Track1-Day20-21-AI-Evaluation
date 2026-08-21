# AI Support Log — Nhật Ký Độc Lập Cá Nhân (Nguyễn Quang Huy — 2A202601873)

- **Học viên**: **Nguyễn Quang Huy** — Mã học viên: `2A202601873`
- **Vai trò**: Decision Owner, PM Quality Lead, Primary Evaluation Engineer
- **Thành viên phối hợp**: **Lăng Thị Phương Huế** — Mã học viên: `2A202601915` (Independent Annotator)
- **Dự án**: K3 Track 1 Day 20–21 — AI Evaluation Lab (VLearn AI Tutor)
- **Repository**: `https://github.com/Bietdoibongdem888/Track1_Day21_2A202601873_NguyenQuangHuy`

---

## 1. AI ĐÃ GIÚP TÔI Ở ĐÂU? (WHERE AI ASSISTED)

1. **Khảo sát mã nguồn & Tự động hóa kiểm thử (Phase 0)**:
   - AI hỗ trợ viết bộ kiểm thử mở rộng 23 unit tests cho hệ thống deterministic code checks (`tests/test_code_checks.py`), đồng thời kiểm kê 341 sections từ 18 tài liệu markdown của corpus.
   - Hỗ trợ xây dựng script kiểm tra tự động `scripts/validate_all.ps1` để chạy nhanh toàn bộ regression suite.

2. **Khởi tạo dữ liệu kiểm thử (Phase 1)**:
   - AI hỗ trợ sinh các câu hỏi mô phỏng người học (simulated queries) dựa trên 15 tổ hợp dimensions do tôi định nghĩa, giúp tiết kiệm thời gian gõ văn bản mẫu.

3. **Chạy Pipeline Đánh giá & Giám khảo LLM (Phase 2 & Phase 4)**:
   - AI thực thi lệnh batch run `eval/run_eval.py` trên model `gemini-flash-lite-latest` và ghi nhận traces tự động lên LangSmith.
   - AI thực thi 4 lượt gọi API độc lập của LLM Judge theo 2 tiêu chí riêng biệt (`groundedness` và `followup_quality`) với các mã băm SHA256 phân biệt.

4. **Tổng hợp Báo cáo & Bảng điểm Lát cắt (Phase 5 & Phase 6)**:
   - AI hỗ trợ trích xuất số liệu thống kê ma trận nhầm lẫn, tính toán tỷ lệ `x/n = %` trên toàn bộ 14 data slices để tôi rà soát trước khi đưa ra quyết định release.

---

## 2. AI SAI, HỜI HỢT HOẶC LÀM MẤT COVERAGE Ở ĐÂU? (WHERE AI FAILED OR EXHIBITED GAPS)

1. **Sai lệch nhân bản bằng chứng hiệu chuẩn (Duplicated Calibration Evidence)**:
   - Trong một lượt chạy trước, công cụ AI đã vô tình sao chép cùng một prompt và kết quả của 1 lần chạy Judge thành 2 vòng (`judge-prompt-final-v1.md` và `v2.md`). Tôi đã phát hiện sai sót này, yêu cầu chuyển toàn bộ file cũ vào thư mục `archive/` và bắt buộc chạy lại 2 vòng API thực sự độc lập cho 2 tiêu chí riêng biệt với các prompt cải tiến có mã băm phân biệt.

2. **Ranh giới gán nhãn con người (Human Label Boundary)**:
   - AI từng đề xuất sinh nhãn tự động cho file review. Tôi đã từ chối và yêu cầu cách ly các file nhãn AI thành `labels-ai-review.csv`, đảm bảo toàn bộ `labels-huy.csv` và `labels-hue.csv` do chính tôi và Huế đọc từng kịch bản trên giao diện `report.html` để chấm độc lập.

3. **Độ trễ và rủi ro Quota API**:
   - Ở lượt chạy ban đầu (Candidate v1/v2), việc gọi model tốc độ cao gặp lỗi `HTTP 429 Too Many Requests`. Tôi đã chỉ đạo tinh chỉnh cơ chế exponential backoff và chuyển sang cấu hình model có quota ổn định.

4. **Nhầm lẫn giữa `scope_sources_consistency` và `expected_scope_match`**:
   - AI ban đầu chỉ đo tính nhất quán nội bộ giữa `scope` và `sources` (nếu OOS thì sources rỗng) mà báo điểm 100%, bỏ qua việc so khớp `output.scope` với `expected_scope` (18/22 = 81.82%). Tôi đã chỉ đạo phân định rõ: **Semantic Release Pass = 22/22 (100%)** và **Exact Scope Tag Match = 18/22 (81.82%)**, đồng thời lập biên bản kiểm toán riêng tại `scope-mismatch-audit.md`.

---

## 3. TÔI ĐÃ TỰ SỬA HOẶC TỰ QUYẾT ĐỊNH LẠI ĐIỀU GÌ? (WHAT I DECIDED & MODIFIED INDEPENDENTLY)

1. **Phê duyệt Chiến lược Phủ 4 Chiều (Checkpoint A, B, C)**:
   - Tôi trực tiếp định nghĩa và phê duyệt 4 dimensions D1–D4, lựa chọn 15 tổ hợp kịch bản C01–C15 và khóa bộ 22 scenarios của `dataset-v1.jsonl`.

2. **Chấm nhãn độc lập & Thống nhất bộ nhãn vàng (Gold Labels)**:
   - Tôi trực tiếp chấm 22 kịch bản tại `labels-huy.csv`, đối soát độ đồng thuận IAA với bạn Huế đạt 100%, và phê duyệt bộ nhãn vàng chính thức `labels.csv`.

3. **Khóa Ngưỡng Chất lượng Trước Run (Threshold Pre-Locking)**:
   - Tôi quyết định các ngưỡng chặn phát hành tại `deliverables/evidence/thresholds-locked.md` (100% schema, 95% citation, 90% quote, >=85% IAA, >=85% Judge agreement) trước khi chạy Candidate v3.

4. **Phê duyệt Quyết định Phát hành Cuối cùng (Release Verdict)**:
   - Dựa trên bằng chứng thực tế từ 14 lát cắt dữ liệu, 44 tests eval-kit pass, 23 code checks unit tests pass, 2 tiêu chí judge được hiệu chuẩn 2 vòng, và kiểm toán 4 ca phân kỳ tag phạm vi, tôi chính thức ký duyệt quyết định **`SHIP with documented scope-tag divergence`** cho VLearn AI Tutor.
