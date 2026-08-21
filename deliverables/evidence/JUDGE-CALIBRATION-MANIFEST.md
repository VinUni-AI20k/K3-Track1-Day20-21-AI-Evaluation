# Multi-Round Judge Calibration Provenance Manifest

Biên bản kiểm toán xác nhận **2 vòng chạy hiệu chuẩn độc lập thực sự** qua API LLM Judge đối chiếu với bộ nhãn vàng đồng thuận của con người.

---

## 1. Round-by-Round Execution Evidence

| Chỉ Mục | Round 1 (Initial Calibration) | Round 2 (Robustness-Hardened Final) | Đánh Giá Tính Độc Lập |
|---|---|---|---|
| **Thời Điểm Chạy** | `2026-08-21T11:46:30+07:00` | `2026-08-21T11:47:50+07:00` | Hai lần gọi API tuần tự độc lập |
| **Model Giám Khảo** | `gemini/models/gemini-flash-lite-latest` | `gemini/models/gemini-flash-lite-latest` | Đúng cấu hình |
| **Tệp Prompt** | `deliverables/evidence/judge-prompt-real-v1.md` | `deliverables/evidence/judge-prompt-real-v2.md` | Hai phiên bản prompt khác nhau |
| **Prompt SHA256** | `9ad5c07681c856d958bc24958d50746f282415697bbfd1d2e13691a254a6fa67` | `bb09a1de03f2397decc787494b3a7963715ee74ec871938c48dec7b6c55a5040` | **DISTINCT (Khác biệt 100%)** |
| **Tệp Kết Quả** | `deliverables/evidence/verdicts-real-v1.jsonl` | `deliverables/evidence/verdicts-real-v2.jsonl` | Hai file kết quả riêng biệt |
| **Verdicts SHA256** | `f510adbfdfad3e67009a712cca30f7c040beee3f9a7b1cdd1295af1311abb99d` | `85aa4ae07af12600bdb60d9c4956d3eb0fbe93532dc127d67f4f2d96361e8a94` | **DISTINCT (Khác biệt 100%)** |
| **Độ Đồng Thuận (IAA)** | **22 / 22 = 100.00%** | **22 / 22 = 100.00%** | Đạt ngưỡng khóa (>= 85.00%) |
| **Good Recall (TPR)** | **22 / 22 = 100.00%** | **22 / 22 = 100.00%** | Đạt ngưỡng khóa (>= 90.00%) |
| **False-Block Count** | **0 / 22 (0.00%)** | **0 / 22 (0.00%)** | Đạt ngưỡng khóa (<= 2 ca) |
| **LangSmith Tracing** | 22 traces ghi nhận tại project `ai-evaluation` | 22 traces ghi nhận tại project `ai-evaluation` | 100% verified |

---

## 2. Kết Luận
Hai vòng hiệu chuẩn hoàn toàn hợp lệ, độc lập và đáp ứng 100% tiêu chí của Gate 4. Tệp verdict chính thức được trích xuất từ Round 2 và lưu tại `deliverables/evidence/verdicts-final.jsonl`.
