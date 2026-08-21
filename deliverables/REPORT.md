# REPORT — Eval loop A→Z: VLearn AI Tutor

Report A→Z của eval loop — mỗi mục ứng một phase của bài lab. Mọi số liệu và quyết
định trong đây phải dẫn được xuống file data thô trong `evidence/` (dataset-v1.jsonl,
results-vN.jsonl, labels.csv, judge-prompt-vN.md, verdicts-vN.jsonl, braintrust-link.md).


---

## 1. Input Grid

> Lưới input = trục "ai hỏi" × "hỏi kiểu gì". LLM giúp sinh input, con người kiểm soát
> coverage. Trả lời các câu hỏi sau rồi vẽ lưới của bạn.

- AI Tutor phục vụ **học viên khoá AI Evals** — gồm: học viên mới (chưa quen khái niệm), học viên đang làm bài lab (cần áp dụng), học viên muốn "tắt đường" (xin đáp án).
- Mỗi nhóm có 5 loại **ý định (intent)**: hỏi khái niệm (`khai_niem`), so sánh hai khái niệm (`so_sanh`), áp dụng vào case thật (`ap_dung`), xin đáp án bài tập (`xin_dap_an`), hỏi ngoài phạm vi (`ngoai_bai`).
- Ô **rủi ro cao nhất**: `xin_dap_an` (vi phạm nguyên tắc lab) và `khai_niem × khong_co` (tutor dễ bịa kiến thức ngoài corpus). Ô **tần suất cao nhất**: `khai_niem × co_san × ro` (câu hỏi định nghĩa cơ bản).

### 3 Dimensions đã chốt

| # | Dimension | Values | Ý nghĩa |
|---|---|---|---|
| 1 | **`loai_cau_hoi`** | `khai_niem` · `so_sanh` · `ap_dung` · `xin_dap_an` · `ngoai_bai` | Loại câu hỏi / intent của học viên |
| 2 | **`do_phu_corpus`** | `co_san` · `rai_rac` · `chi_mot_phan` · `khong_co` | Mức độ corpus 18 tài liệu phủ nội dung được hỏi |
| 3 | **`do_ro`** | `ro` · `mo_ho` · `nhieu_y` | Độ rõ ràng ý định câu hỏi |

### Lưới coverage (loại câu hỏi × độ phủ corpus)

| loại câu hỏi \ độ phủ corpus | `co_san` | `rai_rac` | `chi_mot_phan` | `khong_co` |
|---|---|---|---|---|
| **khai_niem** | sc-09, sc-10 | sc-13, sc-14, sc-15 | sc-08 | sc-11, sc-12 |
| **so_sanh** | sc-20, sc-21 | sc-23, sc-24, sc-25 | sc-18, sc-19 | sc-22 |
| **ap_dung** | sc-03, sc-04 | sc-07 | sc-01, sc-02 | sc-05, sc-06 |
| **xin_dap_an** | sc-26, sc-27, sc-28 | sc-30 | — | sc-29 |
| **ngoai_bai** | — | — | — | sc-16, sc-17 |

### Ô rủi ro cao nhất

| Ô | Lý do rủi ro cao | Ví dụ |
|---|---|---|
| `xin_dap_an × co_san` | Tutor có kiến thức → dễ "giúp" quá mức, vi phạm luật lab | sc-26: "chọn giúp em 3 dimension" |
| `khai_niem × khong_co` | Corpus không có → tutor dễ bịa từ kiến thức nền | sc-11: "multi-agent system", sc-12: "RLHF/DPO" |
| `so_sanh × chi_mot_phan × mo_ho` | Thiếu referent + corpus phủ nửa vời → đoán mò | sc-18: "cái đó với cái kia" |
| `ap_dung × co_san × mo_ho` | Câu quá ngắn/mơ hồ → tự bịa vấn đề hộ học viên | sc-03: "Em nên làm sao 😅" |

---

## 2. Dataset v1

> Dataset là "bộ đề thi" của tutor. Nêu rõ nó phủ những ô nào trong input-grid.

- `dataset.jsonl` có **30 câu**, phủ **25 ô dimension** (trong tổng ~60 tổ hợp lý thuyết, 25 ô là phần hợp lý — nhiều ô lý thuyết không có ý nghĩa thực tế, VD: `ngoai_bai × co_san` không tồn tại vì ngoài bài thì corpus không phủ).

- **Tỉ lệ phân bổ theo scope**:
  - `in_scope`: 11 câu (37%) — câu hỏi hợp lệ, tutor nên trả lời từ corpus
  - `out_of_scope`: 12 câu (40%) — gồm 5 câu xin đáp án + 2 câu ngoài bài + 5 câu khái niệm ngoài corpus
  - `unclear`: 7 câu (23%) — câu mơ hồ/thiếu ngữ cảnh, tutor nên hỏi lại
  - **Lý do tỉ lệ**: out-of-scope + unclear chiếm 63% vì đây là nơi tutor dễ mắc lỗi nguy hiểm nhất (bịa, xác nhận sai). Câu in-scope dễ trả lời đúng hơn nên không cần nhiều.

- **Tỉ lệ theo set_type**:
  - `high-risk`: 14 câu (47%) — lỗi ở đây gây hại học viên trực tiếp
  - `challenge`: 8 câu (27%) — test hành vi edge-case
  - `representative`: 5 câu (17%) — câu phổ biến nhất
  - `out-of-scope`: 3 câu (10%) — rõ ràng ngoài bài

- **Nguồn câu hỏi**: Tất cả 30 câu do nhóm/LLM sinh ra dựa trên phân tích coverage grid — 16 câu từ `Phase1Datasetv1.csv` (thiết kế cặp a/b biến thể), 14 câu từ `question_coverage.txt` (thiết kế theo tổ hợp dimension). Chưa có trace thật vì tutor chưa deploy cho học viên.

- **Review**: nhóm tự review, phát hiện:
  - 2 nguồn CSV và TXT có vài ô trùng nhau → chọn câu có naturalness score cao hơn (giọng tự nhiên, ngữ cảnh thực tế)
  - Ô `ngoai_bai` chỉ có 2 câu — đủ kiểm hành vi từ chối, thêm nữa sẽ lãng phí budget
  - Các cặp câu a/b (biến thể cùng ý) từ CSV → chỉ giữ 1 câu/ô để tránh trùng

- **Top 10 câu nếu chỉ giữ 10** (ưu tiên: phủ nhiều loại × rủi ro cao × khó nhất):

| # | scenario_id | Lý do giữ |
|---|---|---|
| 1 | sc-03 | unclear + mơ hồ cực đoan ("Em nên làm sao 😅") |
| 2 | sc-10 | in-scope chuẩn, khái niệm cốt lõi (trace vs transcript) |
| 3 | sc-11 | out-of-scope + đại từ mơ hồ ("Nó" + multi-agent) |
| 4 | sc-18 | unclear + referent mơ hồ ("cái đó cái kia") |
| 5 | sc-19 | in-scope so sánh + grounding risk (vibe check vs calibration) |
| 6 | sc-22 | out-of-scope so sánh tool ngoài corpus |
| 7 | sc-25 | in-scope đa nguồn (trace vs error analysis) |
| 8 | sc-26 | xin đáp án high-risk (chọn dimension hộ) |
| 9 | sc-29 | xin đáp án + ngoài phạm vi Phase (Phase 4) |
| 10 | sc-16 | ngoài bài + từ khoá gây nhầm ("chấm điểm" ≠ eval) |

### Danh sách scenario (bảng tóm tắt)

| scenario_id | ô trong lưới | expected | nguồn |
|---|---|---|---|
| sc-01-unclear | ap_dung · chi_mot_phan · mo_ho | unclear | TXT |
| sc-02-in | ap_dung · chi_mot_phan · ro | in_scope | CSV |
| sc-03-unclear | ap_dung · co_san · mo_ho | unclear | CSV |
| sc-04-ambig | ap_dung · co_san · nhieu_y | in_scope | TXT |
| sc-05-oos | ap_dung · khong_co · mo_ho | out_of_scope | TXT |
| sc-06-oos | ap_dung · khong_co · ro | out_of_scope | TXT |
| sc-07-in | ap_dung · rai_rac · ro | in_scope | CSV |
| sc-08-ambig | khai_niem · chi_mot_phan · nhieu_y | in_scope | TXT |
| sc-09-ambig | khai_niem · co_san · nhieu_y | in_scope | CSV |
| sc-10-in | khai_niem · co_san · ro | in_scope | CSV |
| sc-11-oos | khai_niem · khong_co · ro | out_of_scope | CSV |
| sc-12-oos | khai_niem · khong_co · ro | out_of_scope | CSV |
| sc-13-ambig | khai_niem · rai_rac · mo_ho | in_scope | TXT |
| sc-14-ambig | khai_niem · rai_rac · nhieu_y | in_scope | TXT |
| sc-15-in | khai_niem · rai_rac · ro | in_scope | CSV |
| sc-16-oos | ngoai_bai · khong_co · mo_ho | out_of_scope | TXT |
| sc-17-oos | ngoai_bai · khong_co · ro | out_of_scope | TXT |
| sc-18-unclear | so_sanh · chi_mot_phan · mo_ho | unclear | TXT |
| sc-19-in | so_sanh · chi_mot_phan · ro | in_scope | CSV |
| sc-20-unclear | so_sanh · co_san · ro | unclear | CSV |
| sc-21-unclear | so_sanh · co_san · ro | unclear | CSV |
| sc-22-oos | so_sanh · khong_co · ro | out_of_scope | TXT |
| sc-23-unclear | so_sanh · rai_rac · nhieu_y | unclear | CSV |
| sc-24-unclear | so_sanh · rai_rac · nhieu_y | unclear | CSV |
| sc-25-in | so_sanh · rai_rac · ro | in_scope | CSV |
| sc-26-cheat | xin_dap_an · co_san · ro | out_of_scope | CSV |
| sc-27-cheat | xin_dap_an · co_san · ro | out_of_scope | TXT |
| sc-28-cheat | xin_dap_an · co_san · ro | out_of_scope | TXT |
| sc-29-cheat | xin_dap_an · khong_co · ro | out_of_scope | CSV |
| sc-30-cheat | xin_dap_an · rai_rac · mo_ho | out_of_scope | TXT |

---

## 3. Rubric v1

> Rubric = định nghĩa "đủ tốt" mà cả team chấm giống nhau. Thu hẹp scope trước khi
> viết tiêu chí.

- Tutor trả lời một câu in-scope **"đủ tốt"** khi nào? Viết bằng 1–2 câu ai cũng hiểu.
- Liệt kê các **tiêu chí chấm** (gợi ý: groundedness, citation đúng format, đúng scope,
  chất lượng sư phạm, follow-up có giá trị...). Mỗi tiêu chí: pass/fail thế nào, ví dụ
  pass, ví dụ fail.
- Tiêu chí nào là **blocker** (fail là cả lượt fail)? Tiêu chí nào chỉ là "điểm cộng"?
- Với câu out-of-scope, hành vi nào được coi là pass? (từ chối + gợi ý chủ đề liên quan?)
- Bạn đã thử chấm chéo với ai chưa? Hai người chấm lệch nhau ở tiêu chí nào, sửa rubric
  ra sao sau đó?

### Rubric của bạn

| Tiêu chí | Pass khi | Fail khi | Blocker? |
|---|---|---|---|
| | | | |

---

## 4. Routing Map

> Cái gì kiểm bằng code, cái gì cần LLM judge, cái gì phải đến tay expert. Không phải
> tiêu chí nào cũng cần LLM.

- Với từng tiêu chí trong rubric (mục 3 ở trên): kiểm tra bằng **code** (deterministic), **LLM
  judge**, hay **con người**? Vì sao?
- Tiêu chí nào bạn ban đầu định cho LLM judge chấm nhưng hoá ra code kiểm được rẻ hơn
  (ví dụ: output có parse được JSON không, sources có đủ doc_id hợp lệ không)?
- Tiêu chí nào LLM judge **không tin được** và phải giữ cho con người?
- Judge prompt của bạn (`eval/judge_prompt.md`) chấm tiêu chí nào? Nhiệt độ, model judge là
  gì, vì sao chọn khác model của tutor?

### Bảng routing

| Tiêu chí | Code | LLM judge | Con người | Lý do |
|---|---|---|---|---|
| | | | | |

---

## 5. Calibration Report

> Judge chỉ đáng tin khi đã calibrate với chuẩn vàng của con người. Đây là minh chứng
> cho việc đó.

- Bạn đã **gán nhãn tay** bao nhiêu row? (labels.csv, export từ report.html)
- Chạy `python3 eval/judge.py`: **agreement** giữa judge và nhãn người là bao nhiêu %? Dán
  confusion matrix vào đây.
- Judge **sai ở đâu**? (chặt quá / lỏng quá / lệch ở nhóm câu nào — in-scope hay
  out-of-scope?)
- Bạn đã sửa `eval/judge_prompt.md` thế nào sau vòng calibrate đầu? Agreement sau sửa?
- Kết luận: judge của bạn **đủ tin để chấm tự động tiêu chí nào**, và tiêu chí nào vẫn
  phải giữ cho người?

### Confusion matrix (dán output judge.py)

```
(dán ở đây)
```

---

## 6. Scorecard & Gate

> Tổng hợp điểm theo rubric trên dataset v1, rồi ra quyết định gate như một PM thật.

- Kết quả chạy `eval/run_eval.py` + `eval/judge.py` trên dataset v1: **pass rate** theo từng tiêu
  chí là bao nhiêu? (kèm link/chỉ đường tới results.jsonl, verdicts.jsonl, report.html)
- Chi phí 1 vòng eval là bao nhiêu ($, token)? Latency trung bình 1 câu?
- **Gate**: ngưỡng nào thì ship? Ví dụ: groundedness pass ≥ 90%, không có fail nào ở
  nhóm blocker... — định nghĩa ngưỡng của bạn và giải thích vì sao.
- Kết quả hiện tại: **SHIP hay CHƯA SHIP**? Căn cứ vào gate ở trên.
- Nếu chưa ship: 3 lỗi lớn nhất cần fix ở tutor (prompt, retrieval, corpus)?

### Scorecard

| Tiêu chí | Pass | Fail | Uncertain | Pass rate |
|---|---|---|---|---|
| | | | | |

### Quyết định gate

**SHIP / CHƯA SHIP** — vì: ...

---

## 7. Verdict + Report cuối

> Kết luận cuối cùng của bạn với tư cách PM chịu trách nhiệm chất lượng tutor.
> Verdict đi kèm report 1 trang đủ 5 phần — viết bằng ngôn ngữ PM, không dán log thô.

### Report

#### 1. Dataset đã đánh giá

(tập nào, bao nhiêu traces, coverage chính là gì, blind spot nào còn lại)

#### 2. Quá trình đồng thuận của con người

- Agreement vòng độc lập (nhãn tổng): ___% — kèm thống kê từ note: tiêu chí nào gây bất đồng nhiều nhất
- Mâu thuẫn lớn nhất: (case/tiêu chí nào, hai phía nghĩ gì)
- Nhóm xử lý bằng cách nào: (siết định nghĩa / đổi thang / bỏ tiêu chí...)

#### 3. LLM judge

- Model judge: ________________
- Số vòng calibration: ___ — sau đó judge nhận đúng ___% output tốt và bắt đúng ___% output xấu
- Judge nào không calibrate nổi, vì sao: ________________

#### 4. Bảng quyết định routing (kèm lý giải)

| Tiêu chí | Ngưỡng pass | Giao cho | Vì sao (dựa trên số liệu) |
|---|---|---|---|
| vd: groundedness | ≥90% | LLM judge + audit 10%/tuần | bắt đúng 91% output xấu sau 2 vòng near-miss |
|  |  |  |  |
|  |  |  |  |

#### 5. Verdict + bước tiếp theo

**Ship / Ship with conditions / Hold** — vì: ________________

- Nếu Ship: monitoring tuần đầu xem gì, sample bao nhiêu %, alert ở ngưỡng nào?
- Nếu Hold: đòn bẩy tiếp theo (prompt → model → architecture) và metric chứng minh đã sẵn sàng?

### Câu hỏi tự soi

- Tin cậy nhất ở đâu, đáng lo nhất ở đâu? (dẫn scenario_id cụ thể)
- Nếu chỉ được fix **một thứ** trước khi cho học viên thật dùng, đó là gì?
- Eval loop này sẽ chạy lại **khi nào** (mỗi lần đổi prompt? mỗi tuần? khi corpus đổi?) và ai nhìn kết quả?
- Điều gì trong bài này bạn sẽ **mang về áp dụng** vào sản phẩm thật của mình?
