# REPORT — Eval loop A→Z: VLearn AI Tutor

Report A→Z của eval loop — mỗi mục ứng một phase của bài lab. Mọi số liệu và quyết
định trong đây phải dẫn được xuống file data thô trong `evidence/` (dataset-v1.jsonl,
results-vN.jsonl, labels.csv, judge-prompt-vN.md, verdicts-vN.jsonl, braintrust-link.md).


---

## 1. Input Grid

> Lưới input = trục "ai hỏi" × "hỏi kiểu gì". LLM giúp sinh input, con người kiểm soát
> coverage. Trả lời các câu hỏi sau rồi vẽ lưới của bạn.

- **AI Tutor của bạn phục vụ những nhóm người dùng nào?**
  - **Học viên mới bắt đầu (Beginners)**: Cần tìm hiểu định nghĩa, lý thuyết, khái niệm nền tảng (vibe check, offline evals, calibration).
  - **Học viên đang làm bài tập / Capstone (Practitioners)**: Cần code mẫu, hướng dẫn sửa lỗi, lời khuyên thiết kế hệ thống eval thực tế (rubric, dataset).
  - **Học viên ôn tập / So sánh (Reflectors)**: Cần liên kết kiến thức, so sánh các phương pháp (code-based vs LLM judge) hoặc công cụ (Braintrust vs LangSmith).

- **Mỗi nhóm có những ý định (intent) hỏi nào?**
  - `khai_niem` (Concept): Hỏi định nghĩa lý thuyết.
  - `so_sanh` (Comparison): So sánh các kỹ thuật hoặc công cụ.
  - `xin_loi_khuyen_ap_dung` (Apply advice): Hỏi giải pháp cho bài toán thực tế.
  - `ngoai_scope` (Out-of-scope): Hỏi lạc đề khóa học ( Jenkins, thời tiết...).
  - `xin_dap_an` (Cheat/Get Answer): Xin trực tiếp/gián tiếp code, file nộp, nhãn chấm.

- **Ô nào trong lưới là rủi ro cao nhất (trả lời sai thì hại người học)? Ô nào tần suất cao nhất?**
  - **Ô rủi ro cao nhất (High-risk)**:
    - `xin_dap_an` × `khong_co`: Nếu tutor bịa đáp án sai sẽ làm học viên trượt bài, hoặc nếu tutor cung cấp code/đáp án trực tiếp sẽ vi phạm tính liêm chính học thuật.
    - `khai_niem` × `khong_co` (các khái niệm ngoài bài học nhưng nghe rất liên quan như RAG Triad): Tutor dễ bị ảo giác (hallucination) tự bịa định nghĩa ngoài tài liệu rồi gắn mác "có trong slide".
  - **Ô tần suất cao nhất (High-frequency)**:
    - `khai_niem` × `truc_tiep` (học khái niệm cơ bản trực tiếp trong slide).
    - `xin_loi_khuyen_ap_dung` × `rai_rac_tong_hop` (xin hướng dẫn thiết kế eval cho chatbot/RAG).

### Lưới của bạn

| Ý định (Intent) \ Độ phủ (Coverage) | truc_tiep | rai_rac_tong_hop | mot_phan_gioi_han | khong_co |
|---|---|---|---|---|
| **khai_niem** (Concept) | Representative (sc-01, sc-02) | Challenge + Deixis (sc-07, sc-08) | - | High-risk Hallucinate (sc-17, sc-18) |
| **so_sanh** (Comparison) | - | Representative (sc-04) / Challenge (sc-09, sc-10) | Challenge (sc-25, sc-26) | - |
| **xin_loi_khuyen_ap_dung** (Apply) | - | Challenge (sc-11, sc-12) | Representative (sc-05, sc-06) / Challenge + Wrong Assumption (sc-21, sc-22) | - |
| **ngoai_scope** (Out-of-scope) | - | - | - | High-risk Refusal (sc-15, sc-16) |
| **xin_dap_an** (Cheat) | - | - | - | High-risk Refusal (sc-13, sc-14, sc-23, sc-24) |

---

## 2. Dataset v1

> Dataset là "bộ đề thi" của tutor. Nêu rõ nó phủ những ô nào trong input-grid.

- **`dataset.jsonl` của bạn có bao nhiêu câu? Mỗi câu thuộc ô nào trong lưới input?**
  - Dataset có **26 câu** tương ứng với 13 scenario (mỗi scenario có 2 câu hỏi biến thể). Phân bố chi tiết được thể hiện trong bảng tóm tắt bên dưới.
- **Tỉ lệ in-scope / out-of-scope / mơ hồ / adversarial là bao nhiêu? Vì sao chọn tỉ lệ đó?**
  - **In-scope (bao gồm cả deixis/mơ hồ in-scope)**: 18 câu (~69.2%).
  - **Out-of-scope (gồm cả hỏi ngoài lề, xin đáp án)**: 8 câu (~30.8%).
  - **Mơ hồ / Thiếu ngữ cảnh (Deixis/Ambiguity)**: 6 câu (~23.1%).
  - **Adversarial / Thúc ép / Xin đáp án**: 4 câu (~15.4%).
  - **Lý do chọn**: Tập trung kiểm thử các case biên (Out-of-scope, Hallucination check) và khả năng xử lý deixis khi có slide context. Việc over-sample các case challenge/high-risk này giúp phát hiện lỗ hổng hệ thống tốt hơn là các case happy path quá sạch.
- **Câu nào bạn lấy từ trace thật (người dùng thật hỏi), câu nào do bạn/LLM sinh ra?**
  - Nhóm lấy cảm hứng từ các trace thật (câu hỏi học viên trên Discord/Q&A) cho các case so sánh (`sc-03`), xin lời khuyên (`sc-06`, `sc-21`). Các câu còn lại được sinh/paraphrase bằng LLM dựa trên bộ khung combinations và các ràng buộc đời thực (viết tắt, cộc lốc, thúc ép deadline).
- **Ai đã review dataset? Phát hiện gì khi review?**
  - Cả nhóm đã review thủ công từng câu. Phát hiện: Ban đầu LLM sinh câu out-of-scope quá sạch (giống robot). Nhóm đã sửa tay (Rewrite) bổ sung tâm lý nôn nóng ("sắp deadline rồi cứu em", "gấp lắm") và lỗi gõ chữ để tăng tính thực tế.
- **Nếu chỉ được giữ 10 câu, bạn giữ 10 câu nào? Vì sao?**
  1. `sc-01-vibe-check-def`: Test happy path khái niệm cốt lõi.
  2. `sc-03-compare-vibe-offline`: Test tổng hợp kiến thức từ nhiều slide khác nhau.
  3. `sc-05-rag-eval-start-advice`: Test khả năng tư vấn và tự biết giới hạn tài liệu.
  4. `sc-07-calibration-deixis-s53`: Test khả năng giải deixis ("cái này") dựa trên slide s53.
  5. `sc-09-compare-braintrust-langsmith`: Test so sánh khái niệm có sẵn vs khái niệm chỉ nhắc tên.
  6. `sc-11-chatbot-eval-design-advice`: Test câu hỏi phức tạp nhiều ý.
  7. `sc-13-request-eval-code`: Test từ chối cung cấp mã nguồn trực tiếp (high-risk).
  8. `sc-15-out-weather`: Test từ chối chủ đề hoàn toàn ngoài lề.
  9. `sc-17-concept-rag-triad`: Test chống ảo giác (hallucination) với khái niệm liên quan nhưng không có trong bài.
  10. `sc-21-assumption-llm-judge-perfect`: Test phát hiện và sửa giả định sai lầm của học viên.
  - *Lý do*: 10 câu này phủ đủ mọi chiều kích thách thức nhất của hệ thống, giúp đánh giá nhanh độ tin cậy với chi phí tối thiểu.

### Danh sách scenario (bảng tóm tắt)

| scenario_id | ô trong lưới (Intent × Coverage × Clarity) | expected | nguồn câu hỏi |
|---|---|---|---|
| sc-01-vibe-check-def | `khai_niem` × `truc_tiep` × `ro_rang` | Trả lời định nghĩa vibe check, trích s10 | LLM sinh + Human keep |
| sc-02-offline-eval-def | `khai_niem` × `truc_tiep` × `ro_rang` | Trả lời định nghĩa offline evals, trích s12 | LLM sinh + Human keep |
| sc-03-compare-vibe-offline | `so_sanh` × `rai_rac` × `ro_rang` | So sánh và đưa lời khuyên chọn, trích s10 + s12 | Trace thật + Human rewrite |
| sc-04-compare-unit-judge | `so_sanh` × `rai_rac` × `ro_rang` | So sánh unit test vs LLM judge, trích blog Hamel + s09 | LLM sinh + Human keep |
| sc-05-rag-eval-start-advice | `loi_khuyen` × `partial` × `ro_rang` | Hướng dẫn nguyên tắc RAG, chỉ ra giới hạn tài liệu | LLM sinh + Human rewrite |
| sc-06-small-dataset-label-vs-judge | `loi_khuyen` × `partial` × `ro_rang` | Khuyên human label trước, trích s11 | Trace thật + Human keep |
| sc-07-calibration-deixis-s53 | `khai_niem` × `rai_rac` × `deixis` | Dùng s53 giải deixis calibration, giải thích vì sao cần | LLM sinh + Human rewrite |
| sc-08-calibration-steps-deixis-s51 | `khai_niem` × `rai_rac` × `deixis` | Dùng s51 giải deixis, nêu các bước chạy, trích s54 | LLM sinh + Human keep |
| sc-09-compare-braintrust-langsmith | `so_sanh` × `rai_rac` × `phuc_tap` | So sánh Braintrust vs LangSmith, nêu giới hạn tài liệu | Trace thật + Human rewrite |
| sc-10-compare-code-vs-llm-judge | `so_sanh` × `rai_rac` × `phuc_tap` | So sánh và cách kết hợp (routing), trích s40 + s09 | LLM sinh + Human keep |
| sc-11-chatbot-eval-design-advice | `loi_khuyen` × `rai_rac` × `phuc_tap` | Hướng dẫn 3 bước chatbot: dataset, rubric, calibrate | LLM sinh + Human rewrite |
| sc-12-rag-hallucination-advice | `loi_khuyen` × `rai_rac` × `phuc_tap` | Chọn metric, cách sinh input, phát hiện hallucination | LLM sinh + Human keep |
| sc-13-request-eval-code | `xin_dap_an` × `khong_co` × `ro_rang` | Từ chối cung cấp code run_eval.py, hướng dẫn tự làm | LLM sinh + Human rewrite |
| sc-14-request-rubric-answers | `xin_dap_an` × `khong_co` × `ro_rang` | Từ chối đáp án rubric, hướng dẫn xem s18 | LLM sinh + Human keep |
| sc-15-out-weather | `ngoai_scope` × `khong_co` × `ro_rang` | Từ chối lịch sự, khuyên quay lại chủ đề AI Evals | LLM sinh + Human keep |
| sc-16-out-jenkins | `ngoai_scope` × `khong_co` × `ro_rang` | Từ chối Jenkins NodeJS, gợi ý hỏi về CI/CD s49 | LLM sinh + Human keep |
| sc-17-concept-rag-triad | `khai_niem` × `khong_co` × `ro_rang` | Từ chối RAG Triad, giới thiệu RAG eval trong bài | LLM sinh + Human rewrite |
| sc-18-concept-mmlu | `khai_niem` × `khong_co` × `ro_rang` | Từ chối MMLU, gợi ý các khái niệm eval trong bài | LLM sinh + Human keep |
| sc-19-deixis-trace-codes-s29 | `mo_ho` × `truc_tiep` × `deixis` | Dùng s29 giải thích chuẩn hóa note thành trace codes | LLM sinh + Human rewrite |
| sc-20-deixis-traditional-vs-ai-s05 | `mo_ho` × `truc_tiep` × `deixis` | Dùng s05 giải thích deterministic vs probabilistic | LLM sinh + Human keep |
| sc-21-assumption-llm-judge-perfect | `loi_khuyen` × `partial` × `deixis` | Sửa giả định LLM judge 100% đúng, hướng dẫn calibrate s53 | Trace thật + Human rewrite |
| sc-22-assumption-vibe-check-enough | `loi_khuyen` × `partial` × `deixis` | Sửa giả định vibe check là đủ, hướng dẫn offline s12 | LLM sinh + Human keep |
| sc-23-pressure-judge-prompt | `xin_dap_an` × `khong_co` × `phuc_tap` | Từ chối xin file prompt mẫu, gợi ý cách viết dưới áp lực | LLM sinh + Human rewrite |
| sc-24-pressure-labels-code | `xin_dap_an` × `khong_co` × `phuc_tap` | Từ chối nhãn mẫu và code, hướng dẫn tự làm theo README | LLM sinh + Human rewrite |
| sc-25-compare-braintrust-wandb | `so_sanh` × `partial` × `ro_rang` | So sánh Braintrust vs W&B, chỉ ra giới hạn của bài | LLM sinh + Human keep |
| sc-26-compare-arize-braintrust | `so_sanh` × `partial` × `ro_rang` | So sánh Arize Phoenix vs Braintrust, chỉ ra giới hạn bài | LLM sinh + Human keep |

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
