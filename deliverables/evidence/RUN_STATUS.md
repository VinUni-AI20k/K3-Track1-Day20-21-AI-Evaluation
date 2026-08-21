# Run status

## Đã hoàn thành

- Dataset 24 row, 18 calibration + 6 holdout. V2 sửa expected scope của `sc-23`
  sau khi đọc trace; prompt gửi tutor không đổi.
- Judge prompt v1 được khóa; v2 mới là draft, chưa phải evidence.
- Template nhãn cho ba rater và nhãn vàng.
- 44/44 test offline pass với `PYTHONIOENCODING=utf-8`.

## Đang chờ

- `DEEPSEEK_API_KEY`, `OPENAI_API_KEY`, `LANGSMITH_API_KEY` thật trong `.env`.
- Ba thành viên review dataset và chấm độc lập.
- Output tutor/judge, agreement, metrics và project URL LangSmith.

## Chuỗi lệnh bắt buộc

```powershell
$env:PYTHONIOENCODING='utf-8'
python tests/test_eval_kit.py
python eval/run_eval.py
# Nếu có row lỗi mạng: python eval/run_eval.py --retry-errors
Copy-Item results.jsonl deliverables/evidence/results-v1.jsonl
python eval/code_checks.py | Out-File -Encoding utf8 deliverables/evidence/code-checks-v1.txt
python eval/report.py
```

Mỗi rater export ở root thành `labels-rater-a.csv`, `labels-rater-b.csv`,
`labels-rater-c.csv`. Sau đó:

```powershell
python eval/agreement.py labels-rater-a.csv labels-rater-b.csv labels-rater-c.csv |
  Out-File -Encoding utf8 deliverables/evidence/agreement-v1.txt
```

Thảo luận bất đồng, tạo `labels.csv` ở root và copy bốn file nhãn vào evidence.

### Calibration v1

```powershell
python eval/judge.py --set calibration | Out-File -Encoding utf8 deliverables/evidence/judge-metrics-v1.txt
Copy-Item verdicts.jsonl deliverables/evidence/verdicts-v1.jsonl
```

Chỉ sau khi phân tích mismatch v1 mới chỉnh prompt. Nếu failure theme khớp bản nháp,
áp dụng phần cần thiết từ `eval/judge_prompt_v2.draft.md`, rồi:

```powershell
Copy-Item eval/judge_prompt.md deliverables/evidence/judge-prompt-v2.md
python eval/judge.py --set calibration | Out-File -Encoding utf8 deliverables/evidence/judge-metrics-v2.txt
Copy-Item verdicts.jsonl deliverables/evidence/verdicts-v2.jsonl
```

Khi prompt đã khóa, chạy holdout đúng một lần và không sửa prompt theo kết quả này:

```powershell
python eval/judge.py --set holdout | Out-File -Encoding utf8 deliverables/evidence/judge-metrics-holdout.txt
Copy-Item verdicts.jsonl deliverables/evidence/verdicts-holdout.jsonl
```
