# Kế hoạch làm Lab Day 21 — nhóm 2 người, chỉ 1 máy chạy

## 1. Mô hình làm việc

| Vai trò | Người/máy | Trách nhiệm chính |
|---|---|---|
| **A — Operator & Evidence Engineer** | Nguyễn Quý Dũng — máy đã có `.venv`, API và tracing | Chạy **toàn bộ** lệnh Python/API; quản lý raw evidence, code checks, version các run và tính số liệu |
| **B — Evaluation & PM Lead** | `[Họ tên thành viên 2]` — máy không cần cài thư viện | Lead coverage, review dataset, rubric/routing, soạn judge prompt, phân tích mismatch, scorecard, report và slide nói |

Nguyên tắc cố định:

1. Chỉ máy A chạy `run_eval.py`, `report.py`, `agreement.py`, `code_checks.py`,
   `judge.py` và mọi lệnh tạo evidence.
2. Máy B chỉ cần editor, trình duyệt và Git/kênh chia sẻ file. `report.html` là file
   tĩnh nên B có thể mở và chấm mà không cần Python.
3. Coverage, gold label, routing, threshold và verdict là quyết định chung. Người
   phụ trách soạn không được tự chốt một mình.
4. Mỗi lần chạy phải snapshot output ngay; không ghi đè evidence vòng trước.
5. Không gửi `.env` hoặc API key cho máy B và không commit key lên Git.

> Lab gốc thiết kế cho 3 người. Nhóm chỉ có 2 người phải ghi rõ giới hạn này trong
> REPORT và nên báo coach. Human agreement vẫn đo từ **hai nhãn độc lập**, tuyệt đối
> không tạo nhãn người thứ ba giả.

---

## 2. Phân chia workload 50/50

| Phase | A — Operator & Evidence Engineer | B — Evaluation & PM Lead | Người chốt |
|---|---|---|---|
| P0. Chuẩn bị | 100% setup/runtime, cấu hình trace, test offline | Đọc đề, tạo checklist và cấu trúc sheet quyết định | Cùng kiểm Gate 0 |
| P1. Coverage | Review behavior/risk của từng ô, kiểm format JSONL | Lead Input Grid, candidate bank, Keep/Rewrite/Reject | Cả hai |
| P2. Baseline | Chạy tutor/report, tự chấm độc lập, chạy agreement | Tự chấm độc lập, thống kê note và chuẩn bị case tranh luận | Cả hai chốt gold |
| P3. Formalize | Review tính code-checkable, xác định spec/generalization gap | Lead rubric v1, examples, routing map | Cả hai |
| P4. Calibrate | Code checks, chạy/snapshot judge từng vòng, xuất matrix | Soạn prompt v1/v2, đọc mismatch, đề xuất đúng một thay đổi/vòng | Cả hai chốt lane |
| P5. Gate | Chạy candidate, tính cost/latency/rates/regression | Khóa threshold trước run, phân tích slice và đọc critical failures | Cả hai |
| P6. Verdict | Audit mọi con số với raw evidence, chuẩn bị demo trace | Lead PM report, monitoring/next step, bài nói 2 phút | Cả hai |

Ước lượng công sức: A khoảng **150 phút công việc riêng**, B khoảng **150 phút công
việc riêng**, ngoài các phiên tranh luận/chốt chung. A nặng thao tác kỹ thuật; B nặng
đọc, viết và phân tích nên khối lượng được cân theo thời gian chứ không theo số file.

---

## 3. Timeline thực thi

### P0 — Chuẩn bị và khóa cách làm · 20 phút

#### A — máy chạy

- [ ] Activate `.venv`; chạy `pip check` và offline tests.
- [ ] Điền key thật vào `.env`: provider tutor, provider judge và một tracing backend.
- [ ] Xác nhận tutor và judge dùng model khác nhau; ghi model/version vào worklog.
- [ ] Tạo project Braintrust/LangSmith và kiểm tra trace thử xuất hiện.
- [ ] Tạo quy ước version: `dataset-v1`, `results-v1`, `judge-prompt-v1`,
      `verdicts-v1`.

#### B — máy không chạy

- [ ] Tạo sheet/checklist gồm: scenario decision, human labels, disagreements,
      prompt changes, threshold lock và scorecard.
- [ ] Đọc corpus/slide headings để biết tutor có thể trả lời gì; không tự gắn label.
- [ ] Ghi tên hai thành viên, vai trò và kênh bàn giao file.

**Gate P0:** A có `44 pass, 0 fail`, trace thử thành công; cả hai hiểu đường đi của
mọi artifact.

### P1 — Input Grid và Dataset v1 · 60 phút

#### B lead · A review

- [ ] Hai người cùng chọn dimensions/combinations làm behavior thay đổi.
- [ ] B ghi Input Grid và lý do risk/frequency của từng ô.
- [ ] B soạn candidate questions; mọi câu AI paraphrase phải có
      `Keep/Rewrite/Reject` và quyết định của người.
- [ ] Có tối thiểu: in-scope, OOS, ambiguous/deixis, high-risk và adversarial.
- [ ] Mỗi row có `scenario_id`, `input`, `metadata.dimension_values`,
      `expected_behavior`, `risk_if_fail`, `set_type`; gắn `metadata.slide` khi cần.
- [ ] A review JSONL: ID duy nhất, JSON hợp lệ, slide context đúng, không có row chỉ
      là paraphrase trùng coverage.
- [ ] Hai người khóa Dataset v1; sau thời điểm này muốn đổi phải version và ghi lý do.

#### A snapshot

- [ ] Đặt bản làm việc tại `dataset.jsonl`.
- [ ] Copy bản đã khóa sang `deliverables/evidence/dataset-v1.jsonl`.

**Gate 1:** mỗi row đại diện behavior/risk riêng; coverage có OOS + ambiguous +
high-risk; cả hai bảo vệ được vì sao giữ từng row.

### P2 — Tutor run và Human baseline · 50 phút

#### A — chạy và bàn giao

- [ ] Chạy tutor trên Dataset v1 với tracing.
- [ ] Snapshot `results.jsonl` → `deliverables/evidence/results-v1.jsonl`.
- [ ] Chạy `report.py`; gửi **cùng một** `report.html` tĩnh cho B qua kênh nhóm.
- [ ] Không gửi nhãn của mình cho B trước khi cả hai chấm xong.

#### Hai người chấm độc lập

- [ ] A chấm toàn bộ rows trên máy A → export `labels-dung.csv`.
- [ ] B mở `report.html` trên máy B, chấm độc lập → export rồi đổi tên thành
      `labels-thanhvien2.csv`.
- [ ] Mỗi fail phải note tiêu chí: groundedness, citation, follow-up, scope hoặc
      schema; `uncertain` phải có lý do.

#### A — chạy agreement; B — chuẩn bị tranh luận

- [ ] B tổng hợp danh sách case lệch và lý do hai phía, không tự hòa giải trước.
- [ ] A nhận hai CSV rồi chạy:

```powershell
python eval\agreement.py labels-dung.csv labels-thanhvien2.csv
```

- [ ] Lưu con số agreement **trước đồng thuận** và danh sách disagreement.
- [ ] Hai người đọc lại từng output lệch, chốt gold label vào `labels.csv`.
- [ ] Snapshot các labels độc lập và gold labels vào `deliverables/evidence/`.

**Gate 2:** có output thật, hai bộ nhãn độc lập, agreement hai người, disagreement
reasons và gold labels. REPORT phải nêu rõ nhóm 2 người là blind spot của baseline.

### P3 — Rubric v1 và Routing Map · 35 phút

#### B — lead rubric

- [ ] Gom disagreement theo tiêu chí.
- [ ] Mỗi tiêu chí có: định nghĩa một câu, Yes/No quan sát được, một pass, một fail,
      một borderline lấy từ output thật.
- [ ] Xác định blocker; row fail khi bất kỳ blocker nào fail.

#### A — lead routing kỹ thuật

- [ ] Phân loại spec gap hay generalization gap.
- [ ] Chỉ ra tiêu chí deterministic giao Code.
- [ ] Chỉ ra tiêu chí semantic giao Judge/Assist; high-risk/chưa thống nhất giao Expert.
- [ ] Review xem rule code có false fail so với gold label hay không.

#### Chốt chung

- [ ] Điền rubric vào REPORT mục 3 và routing map vào mục 4.
- [ ] Chọn đúng hai tiêu chí judge để calibrate; khuyến nghị groundedness và
      follow-up quality nếu disagreement cho phép.

**Gate 3:** ít nhất một tiêu chí ở Code; không có routing choice nào thiếu lý do;
người ngoài nhóm có thể dùng rubric mà không hỏi lại.

### P4 — Code checks và Judge calibration · 90 phút

#### Luồng Code — A sở hữu

- [ ] Chạy ba check có sẵn.
- [ ] Thêm 1–2 check của nhóm chỉ khi rule thật sự deterministic.
- [ ] So code result với gold labels; nếu code false fail, sửa rule chứ không sửa
      human label để hợp máy.
- [ ] Ghi pass/fail theo check và case bất thường cho B.

#### Luồng Judge — B viết, A chạy

Với **mỗi tiêu chí**, lặp quy trình sau:

1. B soạn prompt v1: role, đúng một câu hỏi chấm, chuẩn quan sát được, 2–3 near-miss,
   JSON output.
2. A snapshot prompt → `evidence/judge-prompt-<criterion>-v1.md`.
3. A đặt prompt vào `eval/judge_prompt.md`, chạy judge, snapshot raw verdicts.
4. A gửi confusion matrix + false pass/false fail IDs cho B.
5. B đọc mismatch, ghi hypothesis và đề xuất **đúng một thay đổi tối thiểu**.
6. A snapshot prompt v2, chạy lại, snapshot verdicts v2.
7. Hai người so với human–human agreement và chốt Judge / Assist / Expert.

Tên file gợi ý để không lẫn hai tiêu chí:

```text
judge-prompt-grounded-v1.md
judge-prompt-grounded-v2.md
verdicts-grounded-v1.jsonl
verdicts-grounded-v2.jsonl
judge-prompt-followup-v1.md
judge-prompt-followup-v2.md
verdicts-followup-v1.jsonl
verdicts-followup-v2.jsonl
```

**Gate 4:** hai vòng/tiêu chí, confusion matrix từng vòng, rate nhận đúng output tốt,
rate bắt đúng output xấu, prompt diff, pattern lệch và evaluator verdict.

### P5 — Threshold, candidate run và scorecard · 45 phút

#### B — khóa threshold trước

- [ ] Soạn ngưỡng từng critical criterion và trade-off được phép.
- [ ] Hai người ký/xác nhận, ghi timestamp **trước khi A chạy candidate**.
- [ ] Commit/snapshot threshold lock để chứng minh thứ tự thời gian.

#### A — chạy candidate và tính số

- [ ] Chạy code checks rồi judge đã calibrate.
- [ ] Snapshot mọi raw output theo version, model và timestamp.
- [ ] Tính tổng token, cost, latency trung bình, pass rate từng criterion.
- [ ] So baseline/candidate để tìm regression.

#### B — phân tích sản phẩm

- [ ] Đọc overall và breakdown theo `dimension_values`, `set_type`, OOS,
      ambiguous và high-risk.
- [ ] Đánh dấu critical slice thấp nhất; không dùng overall để che regression.
- [ ] Đọc tay ba trace fail quan trọng nhất, ghi nguyên nhân chứ không chỉ đếm.

**Gate 5:** threshold có timestamp trước số; scorecard có slice; regression và ba
critical failures đã được đọc tay.

### P6 — Verdict và đóng gói bài nộp · 20 phút

#### B — lead PM report

- [ ] Viết report một trang đủ 5 phần: dataset/blind spot, human agreement,
      calibration, routing, verdict + next step.
- [ ] Nếu Ship/conditions: monitoring, sample rate, ba drift signals, alert threshold.
- [ ] Nếu Hold: đòn bẩy tiếp theo theo prompt → model → architecture và metric exit.

#### A — evidence audit

- [ ] Đối chiếu từng số trong REPORT với raw file.
- [ ] Kiểm đủ input → output → decision cho mỗi phase.
- [ ] Kiểm version không ghi đè và link Braintrust/LangSmith mở được.
- [ ] Chạy offline tests lần cuối và `git status` trước commit.

#### Cả hai

- [ ] Chốt Ship / Ship with conditions / Hold bằng evidence.
- [ ] Mỗi người tự viết AI Support Log và reflection; không dùng chung nguyên văn.
- [ ] Tập bài nói 2 phút; đổi vai hỏi vặn một dimension, label và threshold.

**Gate 6:** verdict có coverage, slice, calibration evidence và điều kiện/next step;
cả hai đều bảo vệ được quyết định lõi.

---

## 4. Quy tắc bàn giao file giữa hai máy

| A tạo/gửi | B dùng để làm gì | B gửi lại |
|---|---|---|
| `dataset-v1.jsonl` đã validate | review ngôn ngữ và coverage cuối | danh sách Keep/Rewrite/Reject |
| `report.html` từ cùng một run | chấm độc lập trong browser | `labels-thanhvien2.csv` |
| agreement output + disagreement IDs | phân tích rubric gap | rubric examples/borderline |
| matrix + mismatch IDs mỗi judge run | tìm pattern và sửa đúng một điểm | judge prompt version tiếp theo |
| raw scorecard + regression IDs | phân tích slice/critical failures | phần PM interpretation |
| evidence checklist cuối | review tính đầy đủ | REPORT/verdict draft |

Quyền sở hữu file để tránh conflict:

- A sở hữu: `eval/code_checks.py`, scratch files ở root và mọi file raw trong
  `deliverables/evidence/`.
- B sở hữu trong lúc soạn: `deliverables/REPORT.md`.
- Mỗi người sở hữu AI Support Log cá nhân trong repo fork của mình.
- `dataset.jsonl`, rubric, routing, threshold và verdict chỉ merge sau khi cả hai
  xác nhận qua message/commit note.

---

## 5. Các lệnh chỉ được chạy trên máy A

```powershell
# Kích hoạt môi trường
.\.venv\Scripts\Activate.ps1

# Kiểm tra offline
python -m pip check
python tests\test_eval_kit.py

# P2 — tutor + report
python eval\run_eval.py
Copy-Item results.jsonl deliverables\evidence\results-v1.jsonl
python eval\report.py

# Agreement hai người
python eval\agreement.py labels-dung.csv labels-thanhvien2.csv

# P4/P5 — evaluators
python eval\code_checks.py
python eval\judge.py
```

Sau mỗi `judge.py`, A phải đổi tên/copy prompt và verdicts trước lần chạy kế tiếp.
Không dùng `results.jsonl` hoặc `verdicts.jsonl` chưa snapshot làm evidence duy nhất.

---

## 6. Checklist chống tắc việc

- Nếu B chưa xong coverage: A chỉ test bằng dataset example, không chạy candidate
  rồi dùng kết quả đó làm bài nộp.
- Nếu API lỗi: A lưu error, model/provider/timestamp; không để B bịa output để viết
  tiếp report.
- Nếu tracing không thấy run: chưa chạy batch chính thức; sửa trace trước.
- Nếu hai người disagreement trên 20% ở một criterion: giữ Expert/Assist, siết rubric
  trước khi calibrate judge.
- Nếu judge hai vòng không cải thiện: ghi nhận ceiling và chuyển lane, không sửa nhiều
  thứ một lúc.
- Nếu threshold chưa có timestamp: A không chạy candidate final.
- Nếu số REPORT không truy xuống raw evidence: xóa số đó hoặc chạy/tính lại.

## 7. Definition of Done

- [ ] `deliverables/REPORT.md` đủ 7 mục, không còn placeholder quan trọng.
- [ ] Evidence có dataset, results, hai nhãn độc lập, gold labels, judge prompt và
      verdicts từng vòng, confusion matrices và tracing link.
- [ ] Human agreement ghi đúng là agreement của nhóm 2 người.
- [ ] Threshold được khóa trước candidate result.
- [ ] Mọi kết luận có slice breakdown và critical trace đã đọc tay.
- [ ] README ghi đóng góp riêng của từng người.
- [ ] Mỗi người có AI Support Log riêng khi fork nộp cá nhân.
- [ ] A và B đều bảo vệ được verdict, một label bất đồng và một routing choice.
