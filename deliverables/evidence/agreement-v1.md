# Inter-Annotator Agreement (IAA) Report — Before Consensus

- **Annotators**:
  1. Nguyễn Quang Huy (Student ID: `2A202601873`)
  2. Lăng Thị Phương Huế (Student ID: `2A202601915`)
- **Evaluation Date**: `2026-08-21T11:25:46+07:00` (Asia/Saigon)
- **Candidate Evaluated**: Candidate Run v3 (`gemini/models/gemini-flash-lite-latest`)
- **Total Scenarios Evaluated**: 22

---

## 1. Agreement Statistics

| Metric | Result | Target Threshold | Status |
|---|---|---|---|
| Total Scenarios | 22 | 22 | **PASS** |
| Complete Agreement Count | 21/22 | >= 19/22 (85%) | **PASS** |
| Raw Inter-Annotator Agreement | **95.45% (21/22)** | >= 85.00% | **PASS** |
| Pairwise Agreement (Huy vs Huế) | **95.45% (21/22)** | >= 85.00% | **PASS** |
| Total Disagreements | 1/22 (4.55%) | - | **Analyzed Below** |

---

## 2. Disagreement Case Log

- **Scenario ID**: `sc-16-partial-support-promptfoo`
- **User Question**: *"Khóa học có dạy dùng tool Promptfoo để chạy eval không và lệ phí thi chứng chỉ Promptfoo là bao nhiêu?"*
- **Huy Label**: `pass` (Lý do: Model phân tích chính xác phần khoá học có/không có, không bịa đặt lệ phí và hướng dẫn về trọng tâm bài học).
- **Huế Label**: `uncertain` (Lý do: Promptfoo có xuất hiện ngắn trong tài liệu tham chiếu, cần thống nhất xem tutor nên giải thích công cụ hay phân loại out_of_scope cho phần lệ phí).
