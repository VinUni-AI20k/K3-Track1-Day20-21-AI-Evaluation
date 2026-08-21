# Run Manifest: Attempt v1 (Invalid)

- **Attempt ID**: 
un-attempt-v1-invalid
- **Execution Timestamp**: 2026-08-21T10:20:18+07:00
- **Model Evaluated**: gemini/gemini-3.6-flash
- **Dataset File**: deliverables/evidence/dataset-v1.jsonl
- **Git Commit**: 4f67684
- **Run Status**: INVALID RUN — INFRASTRUCTURE INCOMPLETE

---

## 1. Outcome Summary

| Metric | Count | Tỷ lệ / Chi tiết |
|---|---|---|
| **Tổng số scenarios** | 22 | 100% dataset |
| **Infrastructure Errors** | 17 | 16 × HTTP 429 (Rate Limit Exceeded), 1 × HTTP 503 (Service Unavailable) |
| **Product Output Parse Errors** | 4 | Bị cắt ngắn / vỡ JSON do nghẽn mạng |
| **Valid Parsed Outputs** | 1 | sc-09-oos-travel-ambiguous |
| **Eligible for Scoring** | **NO** | Infrastructure incomplete (không dùng làm baseline/candidate score) |

---

## 2. Error Taxonomy Analysis

1. **Infrastructure Errors (17/22)**:
   - 16 trường hợp gặp lỗi HTTP 429 Too Many Requests do tài khoản Google AI Studio Free Tier chạm giới hạn Request-Per-Minute (RPM).
   - 1 trường hợp gặp lỗi HTTP 503 Server Error Service Unavailable.
   - *Phân loại*: Lỗi hạ tầng kết nối (Infrastructure failure), không đại diện cho chất lượng suy luận sư phạm của VLearn Tutor, nhưng khiến toàn bộ đợt chạy **KHÔNG ĐỦ ĐIỀU KIỆN TÍNH ĐIỂM (INVALID)**.

2. **Product Parse Failures (4/22)**:
   - Các scenarios sc-01, sc-02, sc-03, sc-04 bị lỗi phân tích cấu trúc phản hồi khi truyền qua mạng.
   - *Quy tắc quản trị*: Giữ nguyên trong file snapshot minh chứng deliverables/evidence/results-attempt-v1-invalid.jsonl, không xóa bỏ hay làm sạch nhân tạo.

---

## 3. Governance Verdict

- **Trạng thái**: REJECTED FOR SCORING
- **Hành động tiếp theo**: Hardening cơ chế retry backoff, cấu hình model chính thức với quota đầy đủ và chạy lại một batch ứng viên hoàn chỉnh (homogeneous candidate run) sau khi có xác nhận tại Checkpoint 0.
