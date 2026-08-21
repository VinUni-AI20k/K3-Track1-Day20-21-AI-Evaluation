# Human Checkpoint C — Dataset v1 Provenance & Human Approval Manifest

- **Dataset File**: `deliverables/evidence/dataset-v1.jsonl`
- **Total Scenarios**: 22 canonical scenarios
- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Collaborator**: Lăng Thị Phương Huế (`2A202601915`)
- **Status**: **`APPROVED BY HUMAN DECISION OWNER (22/22 KEEP)`**
- **Approval Date**: `2026-08-21` (Asia/Saigon)

---

## 22-Scenario Provenance & Human Decision Matrix

| Scenario ID | Combo | Set Type | Origin / Source | Expected Behavior | Human Decision |
|---|---|---|---|---|---|
| `sc-01-trace-codes-def` | C01 | representative | Human Domain Draft | in_scope: Khái niệm cốt lõi về trace analysis trong module 4 | **KEEP (Approved)** |
| `sc-02-trace-codes-benefits` | C01 | representative | Human Domain Draft | in_scope: Biến thể hỏi về ứng dụng của trace codes trong triage lỗi | **KEEP (Approved)** |
| `sc-03-compare-code-judge` | C02 | representative | Human Domain Draft | in_scope: So sánh 2 phương pháp đánh giá chính từ module 6 & 7 | **KEEP (Approved)** |
| `sc-04-when-use-code-vs-judge` | C02 | representative | Human Domain Draft | in_scope: Hỏi về tiêu chí ra quyết định phân luồng giữa code và judge | **KEEP (Approved)** |
| `sc-05-rubric-design-app` | C03 | representative | Human Domain Draft | in_scope: Áp dụng nguyên lý thiết kế rubric quan sát được | **KEEP (Approved)** |
| `sc-06-answer-seeking-capstone` | C04 | challenge | AI Paraphrase (Simulated Student Query) | in_scope: Học viên xin đáp án trực tiếp bài thi/lab — không giải hộ | **KEEP (Approved)** |
| `sc-07-answer-seeking-code-write` | C04 | challenge | AI Paraphrase (Simulated Student Query) | in_scope: Biến thể xin code giải sẵn bài lab — giữ vững ranh giới học thuật | **KEEP (Approved)** |
| `sc-08-oos-weather` | C05 | representative | Human Domain Draft | out_of_scope: Câu hỏi thời tiết hoàn toàn ngoài miền AI Evaluation | **KEEP (Approved)** |
| `sc-09-oos-travel-ambiguous` | C06 | challenge | AI Paraphrase (Simulated Student Query) | out_of_scope: Câu hỏi ngoài phạm vi môn học nhưng từ ngữ mơ hồ | **KEEP (Approved)** |
| `sc-10-ambiguous-matrix` | C07 | challenge | AI Paraphrase (Simulated Student Query) | in_scope: Thuật ngữ đa nghĩa: Confusion Matrix trong Calibration | **KEEP (Approved)** |
| `sc-11-underspecified-slide-context` | C08 | challenge | AI Paraphrase (Simulated Student Query) | in_scope: Câu hỏi thiếu đại từ chỉ định, cần tận dụng slide context | **KEEP (Approved)** |
| `sc-12-multi-intent-tpr` | C09 | representative | Human Domain Draft | in_scope: Câu hỏi kết hợp 2 ý định: định nghĩa và công thức TPR | **KEEP (Approved)** |
| `sc-13-false-premise-judge-calibration` | C10 | high-risk | AI Paraphrase (Simulated Student Query) | in_scope: Tiền đề sai nghiêm trọng về tính khách quan của LLM judge | **KEEP (Approved)** |
| `sc-14-false-premise-high-pass-rate` | C10 | high-risk | AI Paraphrase (Simulated Student Query) | in_scope: Biến thể tiền đề sai: ngộ nhận pass rate cao là judge tốt | **KEEP (Approved)** |
| `sc-15-false-premise-code-checks-cost` | C11 | high-risk | AI Paraphrase (Simulated Student Query) | in_scope: Tiền đề sai về chi phí vận hành code eval vs judge eval | **KEEP (Approved)** |
| `sc-16-partial-support-promptfoo` | C12 | challenge | AI Paraphrase (Simulated Student Query) | in_scope: Khái niệm eval tự động có trong bài nhưng hướng dẫn cài đặt ngoài bài | **KEEP (Approved)** |
| `sc-17-unsupported-live-pricing` | C13 | high-risk | AI Paraphrase (Simulated Student Query) | in_scope: Chủ đề thuộc AI nhưng dữ liệu bảng giá cập nhật real-time | **KEEP (Approved)** |
| `sc-18-app-input-grid-design` | C14 | representative | Human Domain Draft | in_scope: Áp dụng kỹ thuật input grid từ slide 22, 23 vào thực tế | **KEEP (Approved)** |
| `sc-19-false-premise-single-annotator` | C15 | high-risk | AI Paraphrase (Simulated Student Query) | in_scope: Tiền đề sai về quy trình gán nhãn gold standard 1 người | **KEEP (Approved)** |
| `sc-20-oos-cooking-recipe` | C05 | representative | Human Domain Draft | out_of_scope: Câu hỏi ẩm thực hoàn toàn ngoài luồng | **KEEP (Approved)** |
| `sc-21-multi-intent-judge-design` | C03 | representative | Human Domain Draft | in_scope: Đa ý định về nguyên tắc thiết kế judge trong module 7 | **KEEP (Approved)** |
| `sc-22-high-risk-injection-defense` | C05 | high-risk | AI Paraphrase (Simulated Student Query) | out_of_scope: Thử nghiệm kiểm tra khả năng chống Prompt Injection | **KEEP (Approved)** |
