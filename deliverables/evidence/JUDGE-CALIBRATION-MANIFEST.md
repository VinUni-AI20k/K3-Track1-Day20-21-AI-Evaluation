# Judge Calibration Audit Manifest (Programmatically Generated)

Biên bản kiểm toán toàn diện 4 lượt chạy LLM Judge độc lập thực tế cho 2 tiêu chí ngữ nghĩa riêng biệt (`groundedness` & `followup_quality`) với các mã băm SHA256 được tính toán trực tiếp từ raw artifacts:

## 1. Bảng Đối Soát 4 Lượt Chạy API Thực Tế

| Tiêu chí | Vòng (Round) | Prompt File & SHA256 | Verdicts File & SHA256 | Model Thực Thi | Agreement vs Human Gold | TPR | False-Block | Missed-Bad |
|---|---|---|---|---|---|---|---|---|
| **`groundedness`** | Round 1 | [`judge-prompt-groundedness-v1.md`](judge-prompt-groundedness-v1.md)<br>`0a304f7e0108c69783f9410fa7f7f1095d1d29cd13d6c305118b60f5d53078f5` | [`verdicts-groundedness-v1.jsonl`](verdicts-groundedness-v1.jsonl)<br>`885160595a9be4d4012b7a50b0d2be7d5cf0b16837ba206c2d8573c4b149d517` | `gemini/models/gemini-flash-lite-latest` | **21 / 22 (95.45%)** | 95.45% | 1 (`sc-21`) | 0 |
| **`groundedness`** | Round 2 (Final) | [`judge-prompt-groundedness-v2.md`](judge-prompt-groundedness-v2.md)<br>`02cbae5eb72253de3e3eb01b6870a452e024b55e98190c9b98205aae76c9d26c` | [`verdicts-groundedness-v2.jsonl`](verdicts-groundedness-v2.jsonl)<br>`c5bbbd65f50cb3fa975ba75bdb1d8c41bb6cfdc5ae974055b2a92acfa8719180` | `gemini/models/gemini-flash-lite-latest` | **22 / 22 (100.00%)** | 100.00% | **0** | **0** |
| **`followup_quality`** | Round 1 | [`judge-prompt-followup-v1.md`](judge-prompt-followup-v1.md)<br>`ab228ef9ae363c66e86192792ebc6491fb66f59a64f9959c5739c7762be6d465` | [`verdicts-followup-v1.jsonl`](verdicts-followup-v1.jsonl)<br>`3ff6fee2f51a3180bc6631b38ef7db1913c776ea76ea1da1126651d180da8f6e` | `gemini/models/gemini-flash-lite-latest` | **22 / 22 (100.00%)** | 100.00% | **0** | **0** |
| **`followup_quality`** | Round 2 (Final) | [`judge-prompt-followup-v2.md`](judge-prompt-followup-v2.md)<br>`f15d88449ff10a38344bf6e76adca8c57784a5133a661b04b1a903f99135ba26` | [`verdicts-followup-v2.jsonl`](verdicts-followup-v2.jsonl)<br>`e46687d211f0d6971be55bbbd5c21ba4030276f50284e956318078e64c1b1014` | `gemini/models/gemini-flash-lite-latest` | **22 / 22 (100.00%)** | 100.00% | **0** | **0** |

---

## 2. Kiểm Tra Tính Phân Biệt (Collision-Free Verification)

- `judge-prompt-groundedness-v1.md` != `judge-prompt-groundedness-v2.md`: **PROVEN**
- `verdicts-groundedness-v1.jsonl` != `verdicts-groundedness-v2.jsonl`: **PROVEN**
- `judge-prompt-followup-v1.md` != `judge-prompt-followup-v2.md`: **PROVEN**
- `verdicts-followup-v1.jsonl` != `verdicts-followup-v2.jsonl`: **PROVEN**

Toàn bộ 88 traces (22 rows × 4 runs) được ghi nhận độc lập trên LangSmith Cloud Tracing Project `ai-evaluation`.
