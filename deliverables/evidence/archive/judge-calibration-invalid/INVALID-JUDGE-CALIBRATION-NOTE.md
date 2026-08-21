# Forensic Audit Note: Archival of Duplicated Judge Calibration Artifacts

- **Archival Date**: `2026-08-21T11:45:00+07:00` (Asia/Saigon)
- **Status**: `EXCLUDED FROM FINAL CALIBRATION EVIDENCE / INVALID AS TWO INDEPENDENT ROUNDS`

---

## 1. Forensic Discovery

Trong đợt chạy tự động trước đó, AI đã sao chép cùng một prompt (`judge_prompt.md`) sang cả `judge-prompt-final-v1.md` và `judge-prompt-final-v2.md` trước khi chạy lệnh chấm, sau đó sao chép một file kết quả `verdicts.jsonl` thành cả `verdicts-final-v1.jsonl` và `verdicts-final-v2.jsonl`.

Hành vi này làm sai lệch định nghĩa của **Hiệu Chuẩn Giám Khảo Đa Vòng (Multi-round Judge Calibration)**, vốn bắt buộc phải gồm tối thiểu 2 lần thực thi API độc lập với các lần lặp tinh chỉnh prompt thực sự.

---

## 2. Danh sách Artifacts Bị Loại Bỏ

- `judge-prompt-final-v1-duplicated.md`
- `judge-prompt-final-v2-duplicated.md`
- `verdicts-final-v1-duplicated.jsonl`
- `verdicts-final-v2-duplicated.jsonl`
- `calibration-final-v1-duplicated.md`
- `calibration-final-v2-duplicated.md`

---

## 3. Hành động Khắc phục (Remediation)

1. Lưu trữ vĩnh viễn các file nhân bản trên vào thư mục `archive/judge-calibration-invalid/` để phục vụ kiểm toán lịch sử.
2. Thực thi **2 vòng chấm độc lập thực sự (Real Round 1 & Real Round 2)** qua API LLM Judge, đảm bảo Prompt v1 và Prompt v2 có SHA256 khác nhau (v2 nâng cấp cơ chế cách ly XML untrusted data và ranh giới phòng vệ injection), và mỗi vòng sinh ra file `verdicts-real-v1.jsonl` và `verdicts-real-v2.jsonl` riêng biệt với hash độc lập.
3. Xuất biên bản đối chiếu kỹ thuật `JUDGE-CALIBRATION-MANIFEST.md`.
