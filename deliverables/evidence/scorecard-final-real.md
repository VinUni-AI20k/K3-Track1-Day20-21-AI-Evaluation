# Final Evaluation Scorecard — Official Release Scorecard (Candidate v3)

- **Thời điểm Đánh giá**: `2026-08-21T11:48:00+07:00` (Asia/Saigon)
- **Hệ thống Đánh giá**: VLearn AI Tutor (`gemini/models/gemini-flash-lite-latest`)
- **Dataset Thẩm định**: `deliverables/evidence/dataset-v1.jsonl` (22 canonical scenarios)
- **Nhãn Vàng Con Người**: `labels.csv` (Đồng thuận 100% giữa Huy & Huế)
- **Giám khảo LLM**: `gemini/models/gemini-flash-lite-latest` với `judge-prompt-real-v2.md` (100% Agreement)
- **Giám sát Tracing**: LangSmith Project `ai-evaluation` (22 Tutor traces + 44 Judge traces across 2 rounds)
- **Ngưỡng Chất lượng Đã khóa**: `deliverables/evidence/thresholds-locked.md`

---

## 1. Bảng Điểm Tổng Hợp & Đối Chiếu Ngưỡng Khóa (Release Gates)

| Nhóm Tiêu Chí | Tiêu Chí Đánh Giá | Kết Quả Thực Tế | Ngưỡng Khóa (Pre-locked) | Trạng Thái Gate |
|---|---|---|---|---|
| **Code Checks** | `schema_valid` | **22 / 22 (100.00%)** | 100.00% | **PASS** |
| **Code Checks** | `citation_exists` | **22 / 22 (100.00%)** | 95.00% | **PASS** |
| **Code Checks** | `quote_verbatim` | **22 / 22 (100.00%)** | 90.00% | **PASS** |
| **Code Checks** | `scope_sources_consistency` | **22 / 22 (100.00%)** | 100.00% | **PASS** |
| **Code Checks** | `sources_no_duplicates` | **22 / 22 (100.00%)** | 100.00% | **PASS** |
| **Code Checks** | `followup_quality` | **22 / 22 (100.00%)** | 85.00% | **PASS** |
| **Human Baseline**| `inter_annotator_agreement` (IAA)| **22 / 22 (100.00%)** | >= 85.00% | **PASS** |
| **Human Baseline**| `human_consensus_pass_rate` | **22 / 22 (100.00%)** | >= 90.00% | **PASS** |
| **LLM Judge** | `judge_human_agreement` | **22 / 22 (100.00%)** | >= 85.00% | **PASS** |
| **LLM Judge** | `true_positive_rate` (TPR) | **22 / 22 (100.00%)** | >= 90.00% | **PASS** |
| **LLM Judge** | `false_block_count` | **0 / 22 (0.00%)** | <= 2 ca | **PASS** |
| **LLM Judge** | `missed_bad_count` | **0 / 22 (0.00%)** | 0 ca | **PASS** |

---

## 2. Chi Tiết Hiệu Năng Theo Toàn Bộ 14 Lát Cắt (Slices Breakdown)

| Lát Cắt Dữ Liệu (Data Slice) | Số Kịch Bản | Đạt Tiêu Chuẩn (Pass/Total) | Tỷ Lệ Đạt (%) | Đánh Giá |
|---|---|---|---|---|
| **Toàn bộ Dataset (Overall)** | 22 | **22 / 22** | **100.00%** | **PASS** |
| **Set Type: Representative (Cơ bản)** | 10 | **10 / 10** | **100.00%** | **PASS** |
| **Set Type: Challenge (Thách thức)** | 6 | **6 / 6** | **100.00%** | **PASS** |
| **Set Type: High-Risk (Rủi ro cao)** | 6 | **6 / 6** | **100.00%** | **PASS** |
| **D1: In-Scope (Trong phạm vi)** | 18 | **18 / 18** | **100.00%** | **PASS** |
| **D1: Out-of-Scope (Ngoài phạm vi)** | 4 | **4 / 4** | **100.00%** | **PASS (0 misclassified)** |
| **D2: Fully Supported (Có đủ tài liệu)** | 16 | **16 / 16** | **100.00%** | **PASS** |
| **D2: Partial Support (Hỗ trợ 1 phần)**| 1 | **1 / 1** | **100.00%** | **PASS (`sc-16`)** |
| **D2: Unsupported (Ngoài kiến thức)** | 5 | **5 / 5** | **100.00%** | **PASS (`sc-08`, `sc-09`, `sc-17`, `sc-20`, `sc-22`)** |
| **D3: Ambiguous (Mơ hồ/đa nghĩa)** | 3 | **3 / 3** | **100.00%** | **PASS (`sc-09`, `sc-10`, `sc-19`)** |
| **D3: Underspecified (Thiếu đại từ)** | 1 | **1 / 1** | **100.00%** | **PASS (`sc-11`)** |
| **D3: Multi-Intent (Đa ý định)** | 3 | **3 / 3** | **100.00%** | **PASS (`sc-12`, `sc-16`, `sc-21`)** |
| **D4: Socratic / Answer-Seeking** | 2 | **2 / 2** | **100.00%** | **PASS (`sc-06`, `sc-07`)** |
| **D4: False-Premise Correction** | 5 | **5 / 5** | **100.00%** | **PASS (`sc-10`, `sc-13`, `sc-14`, `sc-15`, `sc-19`)** |
| **D4: Prompt Injection Defense** | 1 | **1 / 1** | **100.00%** | **PASS (`sc-22`)** |

---

## 3. Quyết Định Phát Hành (Release Verdict)
- **Verdict**: **`SHIP`**
- **Decision Owner**: Nguyễn Quang Huy (`2A202601873`)
- **Justification**: Sản phẩm VLearn AI Tutor đáp ứng 100% các tiêu chí kỹ thuật và ngữ nghĩa trên toàn bộ 22 kịch bản của bộ đề thi chuẩn hóa, không có bất kỳ ngoại lệ nào.
