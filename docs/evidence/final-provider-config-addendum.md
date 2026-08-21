# Final Provider & Model Configuration Addendum

- **Tài liệu tham chiếu gốc**: [`thresholds-locked.md`](thresholds-locked.md) (Khóa ngày `2026-08-21T09:47:00+07:00`)
- **Trạng thái Quản trị**: `OFFICIAL FINAL CONFIGURATION ADDENDUM`
- **Mục đích**: Minh bạch cấu hình nhà cung cấp và model thực thi thực tế trong lượt chạy Candidate v3 và 4 vòng Judge Calibration, bảo đảm không thay đổi các ngưỡng chất lượng đã khóa trước run.

---

## 1. Nguyên Tắc Bảo Toàn Ngưỡng (Threshold Preservation Covenant)

1. **Ngưỡng chất lượng không thay đổi**: Toàn bộ các ngưỡng chặn phát hành (100% schema, 95% citation, 90% quote, 100% OOS handling, 0 catastrophic safety failure, >=90% groundedness, >=85% followup, >=80% judge agreement) được giữ nguyên vẹn tuyệt đối như đã cam kết trước khi chạy candidate.
2. **Cập nhật Model thực thi thực tế**: Trong quá trình vận hành kỹ thuật, model thực thi được chuyển sang endpoint `gemini/models/gemini-flash-lite-latest` để đảm bảo quota API ổn định, tránh lỗi HTTP 429 và cho phép xuất toàn bộ telemetry lên LangSmith.

---

## 2. Bảng Đối Chiếu Cấu Hình Model Thực Tế

| Thành phần Hệ thống | Model Trong Bản Dự Thảo Ban Đầu | Model Thực Thi Thực Tế Cuối Cùng (Final Run) | Tracing Backend & Project |
|---|---|---|---|
| **VLearn AI Tutor** | `deepseek/deepseek-v4-flash` | `gemini/models/gemini-flash-lite-latest` | LangSmith (`ai-evaluation`) |
| **Groundedness Judge (R1 & R2)** | `openai/gpt-4o-mini` | `gemini/models/gemini-flash-lite-latest` | LangSmith (`ai-evaluation`) |
| **Follow-up Judge (R1 & R2)** | `openai/gpt-4o-mini` | `gemini/models/gemini-flash-lite-latest` | LangSmith (`ai-evaluation`) |

---

## 3. Xác Thực Tính Nhất Quán (Trace & Telemetry Verification)

- **22 Tutor Candidate traces**: Được log trực tiếp tại `deliverables/evidence/results-v3.jsonl` và LangSmith Project `ai-evaluation`.
- **88 Judge Calibration traces** (22 rows × 2 criteria × 2 rounds): Được log trực tiếp với prompt phân tách XML tại `deliverables/evidence/JUDGE-CALIBRATION-MANIFEST.md`.
