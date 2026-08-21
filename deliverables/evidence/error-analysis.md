# Comprehensive Error Analysis & Remediation Log

- **Author**: Lead AI Evaluation Engineer & Quality PM
- **Project**: VLearn AI Tutor Evaluation Lab (Track 1 Day 20–21)
- **Status**: `COMPLETE & AUDITED`

---

## 1. Infrastructure & Rate Limit Incidents (Attempt v1)

- **Root Cause**: Khởi chạy đồng thời nhiều truy vấn trên Google AI Studio Free Tier model `gemini-3.6-flash` dẫn đến chạm trần hạn ngạch ngày (`GenerateRequestsPerDayPerProjectPerModel-FreeTier`), gây ra 16 lỗi HTTP 429 và 1 lỗi HTTP 503.
- **Evidence Preserved**: `deliverables/evidence/results-attempt-v1-invalid.jsonl` và `run-manifest-attempt-v1.md`.
- **Engineering Remediation**:
  1. Thêm cơ chế Exponential Backoff retry (tối đa 6 lần thử với sleep tăng dần) trong `tutor/tutor.py`.
  2. Bổ sung pacing delay giữa các request tuần tự (3.0s) trong `eval/run_eval.py`.
  3. Chuyển sang model có quota khả dụng và ổn định: `gemini/models/gemini-flash-lite-latest`.
  4. Tích hợp Cloud Tracing (`LangSmith`) để ghi nhận log thời gian thực.
- **Result**: Candidate Runs v1, v2, v3 đạt tỷ lệ thành công hạ tầng **100.00% (22/22 hoàn thành, 0 lỗi HTTP 429/503)**.

---

## 2. Product Quality Defect 1: Verbatim Quote Truncation (Candidate v1)

- **Defect**: 4 scenarios (`sc-02`, `sc-06`, `sc-18`, `sc-21`) bị fail tiêu chí `quote_verbatim` (đạt 18/22 = 81.82%, dưới ngưỡng khóa 90.00%).
- **Root Cause**: Model có thói quen chèn dấu ba chấm (`...`) hoặc dấu mũi tên (`->`) để cắt nối các câu khi trích dẫn, khiến quote không còn là một chuỗi ký tự liên tục nguyên văn từ section text.
- **Engineering Remediation**:
  1. Tăng cường chỉ thị trong `SYSTEM_PROMPT` cấm tuyệt đối việc dùng dấu ba chấm hoặc nối câu.
  2. Bổ sung module `ground_verbatim_quote` trong `tutor/tutor.py` để tự động đối soát và trích xuất đoạn văn bản liên tục nguyên văn dài nhất từ nội dung section thực tế của corpus.
- **Result**: `quote_verbatim` trong Candidate v2 & v3 tăng vọt lên **22/22 (100.00% PASS)**.

---

## 3. Product Quality Defect 2: Duplicate Citations (Candidate v2)

- **Defect**: 3 scenarios (`sc-01`, `sc-05`, `sc-18`) bị fail tiêu chí `sources_no_duplicates` (đạt 19/22 = 86.36%).
- **Root Cause**: Khi câu hỏi liên quan đến nhiều khía cạnh trong cùng một slide, model trích dẫn lặp lại cùng một `(doc_id, section_id)` hai lần.
- **Engineering Remediation**:
  1. Bổ sung cơ chế deduplication theo cặp khóa `(doc_id, section_id)` trong `normalize_tutor_output` trước khi xuất kết quả JSON.
- **Result**: `sources_no_duplicates` trong Candidate v3 đạt **22/22 (100.00% PASS)**.

---

## 4. LLM Judge Calibration Discrepancy (Round 1)

- **Discrepancy**: Judge Round 1 đánh fail `sc-01-trace-codes-def` trong khi Human Consensus là `pass` (Agreement = 21/22 = 95.45%).
- **Root Cause**: Judge Prompt v1 quá khắt khe, coi phần diễn giải sư phạm mở rộng từ nguyên lý đã trích dẫn là "unsupported claims".
- **Remediation**:
  1. Tinh chỉnh `judge-prompt-v2.md` định nghĩa ranh giới rõ ràng: chấp nhận diễn giải sư phạm và ví dụ mở rộng nếu không mâu thuẫn hoặc bịa đặt sai lệch bài giảng.
- **Result**: Judge Round 2 đạt **22/22 (100.00% Agreement & 100.00% TPR, 0 False-Block)**.

---

## 5. Human Inter-Annotator Disagreement (`sc-16`)

- **Discrepancy**: Nguyễn Quang Huy đánh `pass`, Lăng Thị Phương Huế đánh `uncertain` trên `sc-16-partial-support-promptfoo` (IAA trước đồng thuận = 21/22 = 95.45%).
- **Resolution**: Sau khi đối chiếu tiêu chuẩn V04 (Checkpoint A), cả hai thống nhất chốt nhãn `pass` vì Tutor đã trả lời đúng phần có trong bài học, từ chối rõ ràng phần ngoài phạm vi và gợi mở đào sâu nguyên lý.
