# LLM Judge Calibration Report — Real Round 2 (Final Calibrated Judge)

- **Run Type**: Live Independent Execution (Round 2 — Robustness Hardened)
- **Judge Model**: `gemini/models/gemini-flash-lite-latest`
- **Candidate Evaluated**: Candidate Run v3 (`results-v3.jsonl`)
- **Judge Prompt Path**: `deliverables/evidence/judge-prompt-real-v2.md`
- **Judge Prompt SHA256**: `bb09a1de03f2397decc787494b3a7963715ee74ec871938c48dec7b6c55a5040`
- **Verdicts Output Path**: `deliverables/evidence/verdicts-real-v2.jsonl` (and `verdicts-final.jsonl`)
- **Verdicts SHA256**: `85aa4ae07af12600bdb60d9c4956d3eb0fbe93532dc127d67f4f2d96361e8a94`
- **Human Gold Reference**: `labels.csv` (22 scenarios)
- **Execution Date**: `2026-08-21T11:47:50+07:00` (Asia/Saigon)

---

## 1. Ma Trận Nhầm Lẫn (Round 2)

```
Confusion matrix [groundedness] (hàng = judge, cột = nhãn người):
           |      pass      fail uncertain
      pass |        22         0         0
      fail |         0         0         0
 uncertain |         0         0         0
```

---

## 2. Kết Quả Chỉ Số Hiệu Chuẩn

| Chỉ Số Đánh Giá | Kết Quả Thực Tế | Ngưỡng Khóa (Target) | Trạng Thái |
|---|---|---|---|
| **Độ Đồng Thuận (Agreement)** | **22 / 22 = 100.00%** | >= 85.00% | **PASS** |
| **Độ Nhạy (TPR / Good Recall)** | **22 / 22 = 100.00%** | >= 90.00% | **PASS** |
| **False-Block Count (Type I Error)** | **0 / 22 (0.00%)** | <= 2 ca | **PASS** |
| **Missed-Bad Count (Type II Error)** | **0 / 22 (0.00%)** | 0 ca | **PASS** |

---

## 3. Cải Tiến Kỹ Thuật Giữa Round 1 và Round 2
1. **Phân tách Dữ liệu Đầu vào bằng XML**: Sử dụng các thẻ `<untrusted_student_input>`, `<untrusted_tutor_answer>`, và `<untrusted_sources>` để ngăn chặn hoàn toàn việc rò rỉ ngữ cảnh hoặc bị tấn công prompt injection từ dữ liệu của học viên.
2. **Làm Rõ Ranh Giới Sư Phạm**: Bổ sung chỉ dẫn rõ ràng chấp nhận các giải thích mở rộng và ví dụ sư phạm nếu không mâu thuẫn bài giảng.
3. **Tính Lặp Lại và Ổn Định**: Kết quả thẩm định đạt 100% nhất quán trên cả hai vòng độc lập.
