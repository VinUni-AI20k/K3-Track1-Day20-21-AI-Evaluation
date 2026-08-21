# Eval Pack — quy cách bài nộp capstone AI Evaluation (Day 20–21)

"Chiếc hộp" chứa toàn bộ minh chứng eval loop của nhóm cho VLearn AI Tutor.

**Nguyên tắc bắt buộc:** mỗi bước của eval loop phải nộp đủ ba thứ —
**đầu vào** (bạn cho gì vào), **đầu ra** (hệ thống trả gì ra — file data thô),
và **quyết định** (bạn kết luận/lựa chọn gì ở bước đó, VÌ SAO). Thiếu một trong ba,
bước đó coi như chưa làm.

## Cấu trúc repo nộp (tên thư mục/file cố định)

```text
Track1_Day21_MHV_HoVaTen/
├── README.md                  # thông tin cá nhân + nhóm, đóng góp của tôi, verdict tóm tắt
├── deliverables/              # bài nộp report A→Z + DATA THÔ
│   ├── REPORT.md                  # 7 mục QUYẾT ĐỊNH theo phase (1 Input Grid … 7 Verdict) — viết bằng ngôn ngữ PM
│   └── evidence/                  # DATA THÔ — input/output thật của từng bước chạy
│       ├── dataset-v1.jsonl       # dataset nhóm chốt (đầu vào mọi lần chạy)
│       ├── results-v1.jsonl       # output tutor (mỗi row: input, output JSON, tool_calls, tokens, cost)
│       ├── labels.csv             # nhãn người của 3 thành viên (vòng chấm độc lập)
│       ├── judge-prompt-v1.md     # judge prompt vòng 1
│       ├── judge-prompt-v2.md     # judge prompt vòng 2 (diff với v1 phải giải thích trong mục 5 của REPORT.md)
│       ├── verdicts-v1.jsonl      # output judge vòng 1
│       ├── verdicts-v2.jsonl      # output judge vòng 2
│       └── braintrust-link.md     # link project Braintrust/LangSmith — trace mọi run
└── ai-support-log.md          # bạn dùng AI ở đâu, AI sai ở đâu, bạn quyết lại gì
```

Quy ước phiên bản: mỗi lần chạy lại là một version mới — `results-v2.jsonl`,
`verdicts-v3.jsonl`... Không ghi đè file cũ; calibration report cần đối chiếu được
từng vòng.

## Cho thành viên chấm nhãn (Phase 2)

Cả nhóm phải chấm trên **cùng một** `results.jsonl` — nếu mỗi người tự chạy
`run_eval.py` thì output tutor sẽ khác nhau và con số agreement trở nên vô nghĩa
(model đi qua OpenRouter, cùng `temperature=0` vẫn có thể ra kết quả khác vì
request được định tuyến sang nhà cung cấp khác nhau).

Bản có thẩm quyền là `evidence/results-v1.jsonl`. Sau khi `git pull origin dev`:

```bash
cp deliverables/evidence/results-v1.jsonl results.jsonl   # report.py chỉ đọc ở ROOT
python3 eval/report.py && open report.html                # gán nhãn + note, rồi Export
mv ~/Downloads/labels.csv labels-<tên-mình>.csv           # KHÔNG đè labels.csv
```

Chấm xong thì copy file của mình vào `evidence/` rồi commit:

```bash
cp labels-<tên-mình>.csv deliverables/evidence/
python3 eval/agreement.py labels-*.csv                    # cần đủ 2-3 file mới chạy được
```

Lưu ý: `report.html` lưu nhãn trong localStorage của **từng trình duyệt trên từng
máy** — đổi máy hoặc đổi browser là mất nhãn, nên Export ngay khi chấm xong.
`labels.csv` (không có tên) dành riêng cho **nhãn vàng sau đồng thuận**, đừng dùng
cho nhãn cá nhân.

## Checklist trước khi nộp

- [ ] `deliverables/REPORT.md` đủ 7 mục (1 Input Grid … 7 Verdict); mục nào cũng có phần **quyết định + vì sao**
- [ ] `deliverables/evidence/` có đủ data thô của mọi bước: dataset, results, labels, judge prompts
      từng vòng, verdicts từng vòng, link Braintrust/LangSmith (trace mọi run)
- [ ] Số liệu trong REPORT.md khớp với data trong deliverables/evidence/ (kiểm chứng được)
- [ ] Verdict có đủ 5 phần report và một quyết định rõ ràng
- [ ] `ai-support-log.md` là của chính người nộp

## Gợi ý

- Mỗi mục trong `deliverables/REPORT.md` đã có sẵn khung câu hỏi dẫn — trả lời ngắn, dẫn chứng
  bằng số/file thật trong `evidence/`, đừng viết chung chung.
- Chạy xong một vòng là copy file ngay vào `evidence/` — để cuối buổi mới gom là mất.
