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

> Rubric = định nghĩa "đủ tốt" mà cả team chấm giống nhau.

**"Đủ tốt" là gì (1 câu):** Tutor trả lời đúng phạm vi câu hỏi, mọi khẳng định — đặc
biệt là con số — truy được về đúng section đã trích nguyên văn, và khi câu hỏi thiếu
ngữ cảnh thì hỏi lại thay vì đoán hộ học viên.

### Rubric v1 — 7 tiêu chí

| ID | Tiêu chí | Pass khi | Fail khi | Blocker? |
|---|---|---|---|---|
| **C1** | `schema_valid` | Output parse được JSON và đủ 4 field `scope/answer/sources/followup_questions` | JSON vỡ, thiếu field | ✅ Blocker |
| **C2** | `citation_exists` | Mọi `doc_id#section_id` trong `sources` tồn tại thật trong manifest | Trích nguồn không có thật | ✅ Blocker |
| **C3** | `quote_verbatim` | Chuỗi `quote` nằm nguyên văn trong section đã cite | Quote ghép 2 đoạn rời bằng "...", hoặc sửa chữ | ✅ Blocker |
| **C4** | `grounded_claims` | Mọi con số/khẳng định cụ thể truy được về section **đã cite** | Bê số từ section khác, hoặc đảo nghĩa nguồn | ✅ Blocker |
| **C5** | `scope_handling` | Câu ngoài corpus → `scope="out_of_scope"`, `sources=[]`, từ chối khéo | Trả lời như in_scope dù corpus không có | ✅ Blocker |
| **C6** | `clarification` | Câu thiếu referent/ngữ cảnh → hỏi lại trước khi trả lời | Tự đoán ý học viên rồi giảng | ✅ Blocker |
| **C7** | `followup_quality` | Đúng 3 câu, dẫn dắt đào sâu bài học | Thiếu/thừa câu, hỏi lệch chủ đề | ➖ Điểm cộng |

**Luật chấm tổng:** bất kỳ blocker nào fail → cả lượt fail. Không blocker nào fail nhưng
còn nghi vấn không kết luận được → uncertain.

**Câu out-of-scope pass khi nào:** `scope="out_of_scope"` + `sources=[]` + từ chối khéo
+ gợi ý 1–2 chủ đề có trong corpus. Riêng câu xin đáp án bài tập: không được đưa đáp án
trực tiếp, kể cả khi corpus có nội dung đó (đây là ràng buộc sản phẩm, không phải ràng
buộc kiến thức).

### Ba tiêu chí sinh ra từ bất đồng Phase 2

Agreement vòng độc lập chỉ **50%** (15/30). Đọc note thì thấy nguyên nhân không phải ai
chấm sai, mà là **ba người soi ba trục khác nhau mà rubric chưa hề ghi**:

| Cụm bất đồng | Ai phát hiện | Thành tiêu chí |
|---|---|---|
| Tutor không hỏi lại khi câu hỏi thiếu ngữ cảnh (sc-01, sc-07, sc-11, sc-24) | Minh, Hải | **C6** |
| Tutor bịa/đảo nghĩa con số (sc-04 "trên 92%", sc-06 "100–300 dòng") | Đăng | **C4** |
| Tutor giảng luôn nội dung bài tập thay vì từ chối (sc-26, sc-27, sc-30) | Minh, Hải | **C5** (mở rộng cho câu xin đáp án) |

**Ai đúng trong tranh cãi C6?** Trọng tài không phải là bỏ phiếu đa số, mà là cột
`expected_behavior` mà chính nhóm đã viết ở Phase 1: **17/30 row** ghi rõ tutor phải
"hỏi lại"/"làm rõ"/"không đoán bừa". Tức tiêu chí của Minh và Hải là thứ nhóm đã chốt
từ trước; Đăng chỉ là không đối chiếu cột đó khi chấm. Ngược lại, ở C4 thì Đăng đúng và
hai người kia bỏ sót ca bịa số thật (sc-06).

### Ví dụ neo cho từng tiêu chí gây tranh cãi

| Tiêu chí | Pass rõ | Fail rõ | Borderline |
|---|---|---|---|
| **C4** | `sc-10` — giải thích trace vs transcript, mọi ý đều nằm trong section đã cite | `sc-06` — nguồn nói "300 examples is the absolute minimum", tutor viết "chấm 100 đến 300 dòng là hợp lý" (biến sàn thành trần), và số 100/300 **không** có trong 2 section đã cite | `sc-04` — số 92% có thật trong corpus nhưng ở s22, PRD của sản phẩm khác; section đã cite (s49) ghi >90% |
| **C6** | — (không row nào đạt) | `sc-03` — user chỉ viết "Em nên làm sao đây ạ 😅", tutor giảng luôn định nghĩa offline eval | `sc-14` — tutor trả lời ý 1, bỏ ý 2 của user; thiếu chứ không bịa → uncertain |
| **C5** | `sc-17` — từ chối đúng, `sources=[]` | `sc-26` — đưa thẳng 3 dimension cho bài Phase 1 | `sc-27` — không đưa đáp án trực tiếp nhưng cũng không từ chối, vẫn trả `in_scope` |

---

## 4. Routing Map

> Cái gì kiểm bằng code, cái gì cần LLM judge, cái gì phải đến tay expert.

### Chẩn đoán spec gap vs generalization gap

| Lỗi quan sát được | Chẩn đoán | Vì sao |
|---|---|---|
| Không hỏi lại khi thiếu ngữ cảnh (**0/7** câu `unclear`) | **Spec gap** | `SYSTEM_PROMPT` không có một chữ nào về việc hỏi lại. Nó chỉ cho 2 lựa chọn: `in_scope` hoặc `out_of_scope`. Model không thể làm điều chưa ai bảo nó làm → **sửa prompt trước, chưa cần eval** |
| Câu ngoài corpus vẫn trả in_scope (**8/12**) | **Generalization gap** | Prompt đã ghi rõ "corpus không có thông tin → xem là out_of_scope", model vẫn không nhất quán → **ứng viên cho eval tự động** |
| Quote ghép 2 đoạn rời bằng "..." (**12/30**) | **Spec gap** | Prompt nói "trích NGUYÊN VĂN" nhưng không cấm dấu lược "..." → siết prompt |
| Bê số từ section khác (sc-04, sc-06) | **Generalization gap** | Prompt đã cấm bịa số rất rõ, model vẫn vi phạm → **eval tự động + audit người** |

Ba lỗi lớn nhất hiện là **spec gap** — nghĩa là đòn bẩy rẻ nhất lúc này là sửa
`SYSTEM_PROMPT`, không phải thêm eval.

### Bảng routing

| Tiêu chí | Code | LLM judge | LLM assist | Expert | Lý do (dựa trên số liệu) |
|---|---|---|---|---|---|
| **C1** `schema_valid` | ✅ | | | | Rule thuần: parse JSON + so set field. **30/30 pass**, chi phí $0. Giao cho LLM là lãng phí |
| **C2** `citation_exists` | ✅ | | | | Tra `(doc_id, section_id)` trong manifest — nhị phân, không cần ngữ nghĩa. **30/30 pass** |
| **C3** `quote_verbatim` | ✅ | | | | So chuỗi token, deterministic. **Bắt được 12/30 lỗi mà cả 3 người chấm tay đều bỏ sót** — bằng chứng mạnh nhất cho làn Code |
| **C4** `grounded_claims` | | ✅ | | audit 20% | Cần đọc ngữ nghĩa: "trên 92%" vs ">90%" chỉ sai khi hiểu nguồn. Code không làm được. Giữ audit vì đây là lỗi hại người học nhất |
| **C5** `scope_handling` | ⚠️ một phần | ✅ | | | Code kiểm được ràng buộc cứng (`out_of_scope` thì `sources` phải rỗng); còn "câu này corpus có phủ không" cần judge |
| **C6** `clarification` | | | ✅ | ✅ | **Người còn disagree 86% ở nhóm `unclear`** → theo luật lab, chưa đủ chín để giao judge. Máy gom nghi vấn, người quyết. Xét lại sau khi sửa prompt |
| **C7** `followup_quality` | ✅ đếm | ✅ chất lượng | | | Code đếm đủ 3 câu (**30/30 pass**); chất lượng dẫn dắt thì cần judge |

**Tiêu chí tưởng cần LLM nhưng code rẻ hơn:** C3 `quote_verbatim`. Ban đầu nhóm định
gộp vào groundedness cho judge chấm, nhưng nó chỉ là so chuỗi token — và hoá ra đây là
check bắt được nhiều lỗi nhất (12/30) với chi phí $0.

**Tiêu chí không tin được judge:** C6 `clarification`. Ba người còn chấm lệch nhau 86%
ở nhóm câu `unclear` thì không thể kỳ vọng judge chấm ổn định hơn — judge sẽ chỉ học lại
sự mơ hồ của rubric.

**Judge prompt:** hiện `eval/judge_prompt.md` mới chấm **groundedness** (gộp C4 + một
phần C5). Model judge `openrouter/openai/gpt-4o-mini`, `temperature=0`, khác model tutor
(`openrouter/deepseek/deepseek-v4-flash`) để tránh model tự chấm bài của chính mình —
model có xu hướng ưu ái output do chính kiến trúc nó sinh ra.

---

## 5. Calibration Report

> Judge chỉ đáng tin khi đã calibrate với chuẩn vàng của con người.

### Phần A — Human baseline (Phase 2, đã xong)

- **Gán nhãn tay: 30/30 row**, ba thành viên chấm độc lập trên cùng
  `evidence/results-v1.jsonl` (không ai xem nhãn của nhau).
  File: `labels-NguyenHoangMinh.csv`, `labels-NguyenVietHai.csv`, `labels-TrinhHaiDang.csv`.
- **Human–human agreement vòng độc lập: 15/30 = 50%** (đo trước khi đồng thuận).

| Cặp | Agreement |
|---|---|
| Minh vs Hải | 22/30 = 73% |
| Minh vs Đăng | 18/30 = 60% |
| Hải vs Đăng | 18/30 = 60% |
| **Cả 3 trùng nhau** | **15/30 = 50%** |

Mốc lab đưa ra là >90% — nhóm còn cách rất xa, và đó là thông tin có giá trị chứ không
phải lỗi cần che: theo luật lab, **tiêu chí mà người còn disagree >20% thì chưa sẵn sàng
giao cho LLM judge**.

**Bất đồng tập trung ở đâu** (không rải đều):

| Slice | Bất đồng | Đọc ra điều gì |
|---|---|---|
| `expected_scope = unclear` | **6/7 = 86%** | Rubric chưa định nghĩa tutor phải làm gì khi câu hỏi mơ hồ |
| `loai_cau_hoi = ap_dung` | **6/7 = 86%** | Câu "áp vào case của em" — không rõ chấm theo kiến thức hay theo hành vi hỏi lại |
| `do_ro = mo_ho` | 5/7 = 71% | |
| `khai_niem` | 2/8 = 25% | Câu hỏi khái niệm rõ ràng thì nhóm chấm rất giống nhau |
| `ngoai_bai` | **0/2 = 0%** | Câu ngoài bài quá hiển nhiên, không ai lệch |

**Độ chặt từng người** — cùng một dataset, ba mức khắt khe khác nhau:

| Người | pass | fail | uncertain | Là "phiếu lẻ" |
|---|---|---|---|---|
| Minh | 18 | 6 | 6 | 3 case |
| Hải | 23 | 4 | 3 | 3 case |
| Đăng | 21 | 5 | 4 | **7 case** |

Đăng lệch nhóm gấp đôi hai người kia — không phải vì chấm ẩu, mà vì Đăng là người
duy nhất soi **tính đúng đắn của nội dung** (C4), trục mà hai người kia không kiểm.

**Mâu thuẫn lớn nhất:** `sc-07` — cùng một output, Đăng cho `pass` ("khớp 2 citation"),
Minh và Hải cho `uncertain` ("model không hỏi case cụ thể là gì"). Hai bên đều đúng theo
trục của mình; rubric v1 cũ không có trục nào trong hai.

**Nhóm xử lý bằng cách nào:** không hoà giải bằng bỏ phiếu. Tách trục ẩn thành hai tiêu
chí tường minh (**C4 grounded_claims** và **C6 clarification**), rồi phân xử từng case
bằng bằng chứng trong `results-v1.jsonl` + cột `expected_behavior` của dataset Phase 1.
Chi tiết 15 case: `evidence/agreement-v1.md`.

**Nhãn vàng sau đồng thuận** (`evidence/labels.csv`): **15 fail · 14 pass · 1 uncertain**.
Trùng khớp với nhãn cá nhân: Minh 67%, Hải 60%, Đăng 67% — không thành viên nào được
ưu tiên làm chuẩn.

### Phần B — Judge calibration (Phase 4, CHƯA CHẠY)

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
