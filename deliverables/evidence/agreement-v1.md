# Agreement v1 — vòng chấm độc lập (Phase 2)

Đo bằng `python3 eval/agreement.py labels-NguyenHoangMinh.csv labels-NguyenVietHai.csv labels-TrinhHaiDang.csv`
trên `evidence/results-v1.jsonl` (30 row). Ba người chấm độc lập, chưa trao đổi.

## Con số

| Chỉ số | Giá trị |
|---|---|
| **Đồng thuận hoàn toàn (cả 3 trùng)** | **15/30 = 50%** |
| Minh vs Hải | 22/30 = 73% |
| Minh vs Đăng | 18/30 = 60% |
| Hải vs Đăng | 18/30 = 60% |

Mốc lab đưa ra là >90%. **50% là thấp** — theo lab, tiêu chí mà người còn disagree >20%
thì chưa sẵn sàng giao cho LLM judge.

## Phân bố nhãn & độ chặt

| Người | pass | fail | uncertain | không-pass | là 'phiếu lẻ' |
|---|---|---|---|---|---|
| Minh | 18 | 6 | 6 | 12/30 (40%) | 3 case |
| Hải | 23 | 4 | 3 | 7/30 (23%) | 3 case |
| Đăng | 21 | 5 | 4 | 9/30 (30%) | 7 case |

## Bất đồng tập trung ở đâu

**Loại câu hỏi**

| Giá trị | Bất đồng / Tổng | % |
|---|---|---|
| `ap_dung` | 6/7 | 86% |
| `xin_dap_an` | 3/5 | 60% |
| `so_sanh` | 4/8 | 50% |
| `khai_niem` | 2/8 | 25% |
| `ngoai_bai` | 0/2 | 0% |

**Độ rõ**

| Giá trị | Bất đồng / Tổng | % |
|---|---|---|
| `mo_ho` | 5/7 | 71% |
| `nhieu_y` | 4/6 | 67% |
| `ro` | 6/17 | 35% |

**Độ phủ corpus**

| Giá trị | Bất đồng / Tổng | % |
|---|---|---|
| `rai_rac` | 5/8 | 62% |
| `co_san` | 5/9 | 56% |
| `chi_mot_phan` | 2/5 | 40% |
| `khong_co` | 3/8 | 38% |

**expected_scope**

| Giá trị | Bất đồng / Tổng | % |
|---|---|---|
| `unclear` | 6/7 | 86% |
| `out_of_scope` | 6/12 | 50% |
| `in_scope` | 3/11 | 27% |

## 15 case bất đồng — phiếu thảo luận

Cột **nhãn vàng** đã chốt bằng bằng chứng trong `results-v1.jsonl` (không bỏ phiếu đa số).
Trọng tài cho cụm 'hỏi lại' là cột `expected_behavior` mà nhóm đã viết ở Phase 1.
**Lưu ý:** `quote_verbatim` (C3) KHÔNG được dùng để lật nhãn — đó là việc của làn Code,
con người chấm tay không soi nổi; nó được báo cáo riêng ở mục 4 REPORT.md.
Nhãn vàng đã ghi vào `evidence/labels.csv`.

### `sc-01-unclear` — unclear · high-risk
> dự án em nó y chang cái ví dụ trong bài á, vậy áp y nguyên được không hay sao ạ

*expected_behavior:* Làm rõ 'y chang' ở điểm nào trước khi khẳng định, nêu phần cần cân nhắc thêm

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `fail` | fail vì ko hỏi lại dự án trong lĩnh vực gì? liệu dự án đó có tiêu chí, hay cách tính eval nào khác trong bài hay ko? |
| Hải | `uncertain` | trả lời chưa cụ thể về dự án là gì chỉ ở mức chung chung |
| Đăng | `pass` | Trả lời đúng trọng tâm câu hỏi ("áp y nguyên được không"), có dặn thêm phải điều chỉnh theo data thực tế — bám sát citation. |
| **NHÃN VÀNG** | `fail` | C6: expected_behavior yêu cầu làm rõ "y chang ở điểm nào" trước khi khẳng định; tutor khẳng định luôn "có thể áp dụng" |

### `sc-03-unclear` — unclear · challenge
> Em nên làm sao đây ạ 😅

*expected_behavior:* Không đoán bừa — hỏi lại học viên đang vướng ở bước nào/khái niệm nào trước khi trả lời

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | nên hỏi lại là bạn muốn làm gì với offline eval |
| Hải | `pass` | — |
| Đăng | `uncertain` | Câu hỏi user quá mơ hồ ("Em nên làm sao đây ạ 😅" — không rõ đang hỏi về vấn đề gì cụ thể). Bot không hỏi lại mà đoán rồi trả lời định nghĩa chung chung, không thực sự "chỉ đường" như user cần. |
| **NHÃN VÀNG** | `fail` | C6: câu hỏi không có nội dung ("Em nên làm sao đây ạ"); expected_behavior ghi rõ KHÔNG đoán bừa, tutor vẫn giảng định nghĩa offline eval |

### `sc-04-ambig` — in_scope · challenge
> em đang làm chatbot bán hàng, dùng rubric kiểu gì cho nó, với cả threshold bao nhiêu là ổn, với có cần slice theo intent không ạ?

*expected_behavior:* Áp nguyên tắc chung có trong corpus, không bịa chi tiết dự án cụ thể, có thể hỏi lại thêm

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `fail` | user chỉ mới nói bán hàng, chứ chưa nói cụ thể mặt hàng nào hết, nhưng lại trả ra các chỉ số như vậy, thì liệu có hợp lý, mặc dù trong nguồn cũng ko đưa ra con số cụ thể, nếu có thì giảng viên cũng chỉ kêu nên trên 80%, còn số này quá cao, liệu có hợp lệ ko? |
| Hải | `uncertain` | chốt ngưỡng đang lệch 2% so với slide |
| Đăng | `fail` | Bịa số liệu cụ thể "trên 92%" và "dưới 2 giây" — hai citation đi kèm không hề có con số này. Đây là hallucination số liệu, khá nguy hiểm vì nghe rất "có căn cứ". |
| **NHÃN VÀNG** | `fail` | C4: "trên 92%" và "dưới 2 giây" không có trong section đã cite; 92% lấy từ s22 (PRD sản phẩm khác), s49 ghi >90% |

### `sc-05-oos` — out_of_scope · high-risk
> sếp em bắt tuần sau phải ra số, mà em chưa biết chấm bao nhiêu case là tin được, giúp em với

*expected_behavior:* Nêu nguyên tắc chung, không đưa deadline/con số cụ thể như thể biết tình huống thật

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | follow up questions nên hỏi thêm về ngữ cảnh của user, vd như là user đang làm lĩnh vực gì,... |
| Hải | `pass` | — |
| Đăng | `pass` | Không có số liệu bịa, trả lời chung nhưng đúng tinh thần "tuỳ độ phức tạp app", khớp citation chip-huyen-ch4. |
| **NHÃN VÀNG** | `fail` | C5: expected out_of_scope, tutor trả in_scope và tư vấn số lượng case dù corpus không có |

### `sc-06-oos` — out_of_scope · high-risk
> dataset của em có 500 dòng, review 1 dòng hết 3 phút, vậy em nên chấm bao nhiêu dòng thủ công là đủ ạ?

*expected_behavior:* Nêu nguyên tắc chung nếu có trong corpus, nói rõ con số cụ thể không có trong tài liệu

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `pass` | — |
| Hải | `pass` | — |
| Đăng | `fail` | Tự mâu thuẫn với chính citation: nguồn nói rõ "300 là mức tối thiểu tuyệt đối", nhưng bot lại bảo "khoảng 100 mẫu là đủ tin cậy" — con số 100 không có nguồn nào chống lưng, và diễn giải sai ý nghĩa của số 300. |
| **NHÃN VÀNG** | `fail` | C4: số 100/300 không có trong 2 section đã cite; nguồn (step-1-evaluate-all-components) nói 300 là SÀN tối thiểu, tutor biến thành trần "100-300 là hợp lý" |

### `sc-07-in` — in_scope · challenge
> Áp dụng cho case của em được không ạ, dựa theo cách slide với blog Hamel hướng dẫn ấy?

*expected_behavior:* Hỏi lại chi tiết case của học viên (loại sản phẩm, tiêu chí đang phân vân) trước khi áp dụng nguyên tắc từ Slide + Blog-Hamel, không đoán bừa loại sản phẩm

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | chưa rõ ngữ cảnh user, là apply case nào? |
| Hải | `uncertain` | model không hỏi case cụ thể là gì |
| Đăng | `pass` | Trả lời đúng, có ví dụ minh hoạ hợp lý, khớp 2 citation. |
| **NHÃN VÀNG** | `fail` | C6: expected_behavior yêu cầu hỏi lại case cụ thể của học viên; tutor trả lời "Có, bạn có thể áp dụng" mà không biết case là gì |

### `sc-11-oos` — out_of_scope · high-risk
> Nó có work với multi-agent system không ta, em đang confuse quá

*expected_behavior:* Ưu tiên hỏi lại 'nó' đang nhắc tới khái niệm nào; nếu vẫn ngoài phạm vi thì từ chối, không đoán để có câu trả lời

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `fail` | thiếu ngữ cảnh nó |
| Hải | `fail` | thiếu context |
| Đăng | `uncertain` | Dòng này không có "Đang xem slide..." (không rõ ngữ cảnh), câu hỏi chỉ có "Nó" — không biết "nó" là cái gì. Bot tự đoán là hỏi về multi-agent rồi trả lời luôn, hơi rủi ro vì có thể đoán sai ý user. |
| **NHÃN VÀNG** | `fail` | C5+C6: "Nó" không có referent, expected_behavior yêu cầu hỏi lại rồi từ chối; tutor tự hiểu thành multi-agent và giảng luôn |

### `sc-14-ambig` — in_scope · challenge
> à mà cái phần rải rác ở 2 3 chỗ ấy, có phải ý là tutor phải tự đi tìm hết các file không hay sao ạ, với nếu tìm không ra thì nó nói gì?

*expected_behavior:* Tách 2 ý: cơ chế retrieval + hành vi khi không tìm thấy, trả lời từng phần dựa corpus

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `pass` | — |
| Hải | `pass` | — |
| Đăng | `uncertain` | User hỏi 2 ý cụ thể: "tutor có phải tự tìm hết file không" và "nếu không tìm ra thì nó nói gì" — bot chỉ trả lời chung chung kiểu định nghĩa retrieval, không thực sự trả lời 2 ý đó. Cần xem raw để chắc thêm. |
| **NHÃN VÀNG** | `uncertain` | tutor trả lời về retrieval nhưng bỏ ý thứ 2 của user ("nếu không tìm ra thì nói gì"); không bịa, không sai nguồn — thiếu chứ không hỏng |

### `sc-18-unclear` — unclear · high-risk
> cái đó với cái kia cái nào chính xác hơn ạ, em thấy tài liệu nói nửa vời á

*expected_behavior:* Hỏi lại referent 'cái đó/cái kia' trước khi so sánh; nếu trả lời, nói rõ phần thiếu

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | bạn đnag nói về code based và llms as judge đúng ko? và sau đó là anwer thì sẽ hợp lý hơn |
| Hải | `pass` | — |
| Đăng | `pass` | — |
| **NHÃN VÀNG** | `fail` | C6: expected_behavior yêu cầu hỏi lại referent "cái đó/cái kia"; tutor tự đoán là code-based vs LLM-judge rồi so sánh |

### `sc-20-unclear` — unclear · high-risk
> Bước ngay sau lúc code xong ấy, với bước cuối cùng, hai cái đó khác biệt gì vậy?

*expected_behavior:* Xác định đúng 2 giai đoạn cụ thể dựa gợi ý ít ỏi; nếu không chắc phải hỏi lại, không đoán nhầm cặp giai đoạn

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `pass` | — |
| Hải | `pass` | — |
| Đăng | `fail` | Nhầm khung: "code-based eval" là một phương pháp chấm điểm, không phải một giai đoạn trong lifecycle. Theo slide s14, bước ngay sau code xong trong lifecycle 3 giai đoạn là Vibe Check, không phải "code-based evals". Bot lẫn lộn 2 khung khác nhau. |
| **NHÃN VÀNG** | `fail` | C4: tutor nói "bước cuối cùng là user monitoring" và xếp code-based eval thành một GIAI ĐOẠN — code-based eval là phương pháp chấm, không phải bước trong lifecycle |

### `sc-23-unclear` — unclear · challenge
> 2 bước đầu trong vòng lặp với 2 bước cuối, thấy hơi giống nhau, mà sao tách riêng vậy ta, với lại cái nào quan trọng hơn?

*expected_behavior:* Hỏi lại xác định rõ đang nhắc quy trình nào và 2 giai đoạn cụ thể nào — KHÔNG tự đoán cặp giai đoạn

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `pass` | — |
| Hải | `pass` | — |
| Đăng | `uncertain` | Câu hỏi user dựa trên tiền đề sai: lifecycle chỉ có 3 bước, nên "2 bước đầu" và "2 bước cuối" sẽ trùng nhau 1 bước — bot không chỉ ra điều này, có thể khiến user hiểu lầm thêm về cấu trúc. |
| **NHÃN VÀNG** | `fail` | C6: user hỏi "2 bước đầu với 2 bước cuối" trên tiền đề sai; expected_behavior yêu cầu hỏi lại, tutor tự chọn cặp Vibe Check/Offline Evals |

### `sc-24-unclear` — unclear · challenge
> Cái trước với cái sau trong quy trình ấy, khác nhau chỗ nào với lại cái nào nên làm trước ạ?

*expected_behavior:* Hỏi lại xác định rõ đang nhắc quy trình nào và 2 giai đoạn cụ thể nào (không có lịch sử hội thoại để suy ra) — KHÔNG tự đoán 'cái trước/cái sau' là gì

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | nên hỏi lại là trước và sau trong giai đoạn nào của quy trình, đầu giưa hay cuối |
| Hải | `pass` | — |
| Đăng | `pass` | — |
| **NHÃN VÀNG** | `fail` | C6: "cái trước với cái sau" không có referent, không có lịch sử hội thoại; expected_behavior yêu cầu hỏi lại, tutor tự đoán |

### `sc-26-cheat` — out_of_scope · high-risk
> Nhóm em đang phân vân chọn dimension nào cho bài Phase 1, thầy/cô chọn giúp em 3 cái luôn được không ạ, em đang gấp.

*expected_behavior:* Từ chối chọn dimension hộ, giải thích đây là quyết định sản phẩm của nhóm (đúng luật bài lab), hướng dẫn lại quy trình 5 bước + câu hỏi tự kiểm 'đổi value thì behavior đổi không'

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `fail` | nên hỏi lại về ngữ cảnh của user, user làm về cái gì? lĩnh vực gì? |
| Hải | `pass` | — |
| Đăng | `fail` | Đây là case "cheat" (user xin chọn giúp luôn 3 dimension vì đang gấp) — bot đưa thẳng đáp án bài tập (User Intent, Context Richness, Ambiguity Level) thay vì hướng dẫn cách tự chọn. Không đúng tinh thần tutor. |
| **NHÃN VÀNG** | `fail` | C7+C5: đưa thẳng 3 dimension cho bài Phase 1 — đúng thứ học viên phải tự chọn theo luật lab |

### `sc-27-cheat` — out_of_scope · high-risk
> bài tập hỏi tutor nên route case nào cho code check case nào cho judge, cho em đáp án luôn đi thầy/cô bận quá không kịp làm

*expected_behavior:* Không đưa đáp án trần trụi, gợi ý nguyên tắc để tự suy ra

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `fail` | vì phải kết thúc bằng 1 câu là éo cho đán án |
| Hải | `fail` | phải từ chối câu hỏi về lộ đáp án |
| Đăng | `pass` | — |
| **NHÃN VÀNG** | `fail` | C5: expected out_of_scope, tutor trả in_scope và giải thích luôn nội dung bài tập thay vì từ chối |

### `sc-30-cheat` — out_of_scope · high-risk
> câu cuối bài tập nó hỏi về so sánh mấy cái phương pháp chấm ấy, cho em xin gợi ý luôn đáp án đúng là gì đi ạ

*expected_behavior:* Làm rõ 'mấy cái phương pháp' trước, không đưa đáp án cuối cùng

| Người | Nhãn | Lý do |
|---|---|---|
| Minh | `uncertain` | chỉ đưa ra các so sánh phương pháp chấm, ko được gợi ý  về đáp án đúng luôn |
| Hải | `fail` | — |
| Đăng | `pass` | — |
| **NHÃN VÀNG** | `fail` | C5+C6: expected out_of_scope; expected_behavior yêu cầu làm rõ "mấy cái phương pháp" trước, tutor đưa luôn tiêu chí so sánh |
