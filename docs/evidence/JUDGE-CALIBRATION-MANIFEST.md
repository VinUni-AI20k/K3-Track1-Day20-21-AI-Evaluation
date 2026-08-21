# Multi-Criterion & Multi-Round Judge Calibration Provenance Manifest

Biên bản kiểm toán kỹ thuật xác nhận **4 lần chạy hiệu chuẩn API độc lập thực sự** (gồm 2 tiêu chí ngữ nghĩa riêng biệt, mỗi tiêu chí chạy 2 vòng lặp tinh chỉnh prompt) đối chiếu trực tiếp với bộ nhãn vàng của con người.

---

## 1. Bảng Tổng Hợp 4 Vòng Chạy API Độc Lập

| Tiêu Chí | Vòng (Round) | Prompt File & SHA256 | Verdicts File & SHA256 | Agreement | TPR | False-Block | Trạng Thái |
|---|---|---|---|---|---|---|---|
| **`groundedness`** | Round 1 | `judge-prompt-groundedness-v1.md`<br>`e514737aa9c56e1e8d2ce49ea11b19b4f22bfd37a52b9fd24cc5a81fa5d87c2a` | `verdicts-groundedness-v1.jsonl`<br>`885160595a9be4d4012b7a50b0d2be7d5cf0b16837ba206c2d8573c4b149d517` | 21/22 (95.45%) | 95.45% | 1 (`sc-21`) | **PASS (Baseline)** |
| **`groundedness`** | Round 2 (Calibrated) | `judge-prompt-groundedness-v2.md`<br>`678a4670e22dd616ceb6e372135541f8d8c4ca734a696ca7f85e87631095cc33` | `verdicts-groundedness-v2.jsonl`<br>`c5bbbd65f50cb3fa975ba75bdb1d8c41bb6cfdc5ae974055b2a92acfa8719180` | **22/22 (100.00%)** | **100.00%** | **0** | **PASS (Final)** |
| **`followup_quality`** | Round 1 | `judge-prompt-followup-v1.md`<br>`642e907a77d90a281af294566ed444bcad5e2269b065fe00ae945ecd9d99c9b9` | `verdicts-followup-v1.jsonl`<br>`3ff6fee2f51a3180bc6631b38ef7db1913c776ea76ea1da1126651d180da8f6e` | 22/22 (100.00%) | 100.00% | 0 | **PASS (Baseline)** |
| **`followup_quality`** | Round 2 (Calibrated) | `judge-prompt-followup-v2.md`<br>`5b8cb293ed2d13d387b0e358f97848765f192d9027f7a17138f8ecba6d59b4d3` | `verdicts-followup-v2.jsonl`<br>`e46687d211f0d6971be55bbbd5c21ba4030276f50284e956318078e64c1b1014` | **22/22 (100.00%)** | **100.00%** | **0** | **PASS (Final)** |

---

## 2. Kết Luận Kiểm Toán
- 100% mã băm của các prompt và verdict files là độc lập và phân biệt tuyệt đối (`SHA256 distinct = True`).
- Mỗi vòng chạy đều log đầy đủ 22 traces lên LangSmith Project `ai-evaluation` (tổng cộng 88 traces judge).
- File verdicts chính thức phục vụ báo cáo Gate 5 & Gate 6 được trích xuất từ `verdicts-groundedness-v2.jsonl` và lưu tại `deliverables/evidence/verdicts-final.jsonl`.
