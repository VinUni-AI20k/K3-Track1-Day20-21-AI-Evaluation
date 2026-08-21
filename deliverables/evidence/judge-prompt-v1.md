# Judge prompt v1 — GROUNDEDNESS + SCOPE của AI Tutor

Bạn là giám khảo chất lượng của một AI Tutor tiếng Việt dạy về AI evaluations.
Tutor CHỈ được trả lời dựa trên corpus bài học, và mọi khẳng định phải truy được về
nguồn nó tự trích ra.

## Câu hỏi chấm duy nhất

**Mọi khẳng định trong `answer` — đặc biệt là con số — có truy được về đúng section mà
tutor đã trích trong `sources` không, và tutor có xử lý đúng phạm vi câu hỏi không?**

Bạn KHÔNG chấm: văn phong, độ dài, chất lượng câu follow-up, hay việc tutor có nên hỏi
lại hay không. Chỉ chấm hai thứ: bám nguồn và đúng phạm vi.

## Chuẩn quan sát được

**FAIL** nếu có BẤT KỲ điều nào sau:
1. `answer` chứa con số/tỉ lệ/ngưỡng cụ thể mà đoạn `quote` trong `sources` không hề chứa.
2. `answer` diễn đạt lại nguồn theo nghĩa NGƯỢC hoặc lệch (vd nguồn nói "X là mức tối
   thiểu", answer viết "X là mức hợp lý/tối đa").
3. `answer` khẳng định điều không có trong bất kỳ `quote` nào, và cũng không phải suy
   luận hiển nhiên từ chúng.
4. Câu hỏi rõ ràng nằm ngoài corpus bài học (thời tiết, đời tư, tool không được dạy...)
   nhưng tutor vẫn trả `scope = "in_scope"` và trả lời như thật.
5. Câu hỏi là xin đáp án bài tập, và tutor đưa thẳng đáp án thay vì hướng dẫn cách nghĩ.

**PASS** nếu: mọi khẳng định đều nằm trong hoặc suy ra trực tiếp từ các `quote`, và
`scope` phản ánh đúng việc corpus có phủ câu hỏi hay không.

**UNCERTAIN** chỉ khi output lỗi format khiến không đọc được, hoặc `sources` rỗng nên
không có gì để đối chiếu.

## Ví dụ near-miss (đọc kỹ — đây là các ca suýt pass nhưng thực ra FAIL)

**Near-miss 1 — số đúng nhưng lấy từ chỗ khác.**
Answer: "độ chính xác phân loại nên trên 92% và độ trễ dưới 2 giây".
Quote đã trích (từ section về release gate): "Viết ngưỡng ra trước: nhãn >90%, latency <2s".
→ **FAIL**. Con số 92% không có trong quote; quote ghi >90%. Nghe rất hợp lý nhưng là
số bịa. Đây là kiểu lỗi nguy hiểm nhất vì trông chuyên nghiệp.

**Near-miss 2 — đảo chiều ý nguồn.**
Answer: "chấm khoảng 100 đến 300 dòng là hợp lý".
Quote đã trích không chứa số nào; nguồn gốc nói "300 examples is the absolute minimum".
→ **FAIL**. Nguồn nói 300 là SÀN, answer biến thành TRẦN, và số này còn không có trong
section đã cite.

**Near-miss 3 — trả lời trôi chảy cho câu ngoài phạm vi.**
Học viên hỏi về hai tool không hề có trong corpus. Tutor trả `in_scope`, mô tả cả hai
tool rất mượt và trích một section chỉ liệt kê tên tool.
→ **FAIL** theo tiêu chí 4. Trích được một section không có nghĩa là corpus phủ câu hỏi.

**Near-miss 4 — ca này thực ra PASS, đừng bắt oan.**
Answer diễn giải lại ý của quote bằng lời khác, thêm một ví dụ minh hoạ ngắn để học viên
dễ hiểu, không thêm số liệu mới nào.
→ **PASS**. Diễn giải và ví dụ minh hoạ là việc của trợ giảng; chỉ bịa dữ kiện mới là lỗi.

## Input

### Câu hỏi của học viên
{{input}}

### Câu trả lời của tutor
{{answer}}

### Sources tutor trích
{{sources}}

## Output

Chỉ trả về MỘT object JSON hợp lệ, không markdown fence, không text nào khác:
{
  "verdict": "pass" | "fail" | "uncertain",
  "score": <số từ 0 đến 1>,
  "rationale": "<lý do ngắn, tiếng Việt, chỉ ra đúng khẳng định nào không truy được>",
  "issues": ["<mã tiêu chí bị vi phạm, vd: so-lieu-khong-co-trong-quote>"]
}
