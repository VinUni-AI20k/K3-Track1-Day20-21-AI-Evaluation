import sys, re
sys.path.insert(0, 'tutor')
import tutor

sections = tutor.load_corpus()
sec_map = {(s['doc_id'], s['section_id']): s['text'] for s in sections}

def ground_quote(doc_id, section_id, raw_quote):
    text = sec_map.get((doc_id, section_id))
    if not text or not raw_quote:
        return raw_quote
    if raw_quote in text:
        return raw_quote
    clean = raw_quote.strip(' .\"\'\n\r\t')
    if clean in text:
        return clean
    # If quote has ellipsis inside, take the longest continuous part that exists in text
    parts = [p.strip() for p in re.split(r'\s*\.\.\.\s*|\s*…\s*|\s*->\s*', raw_quote) if len(p.strip()) > 10]
    for p in sorted(parts, key=len, reverse=True):
        if p in text:
            return p
    # Otherwise, find sentence or line with highest token overlap
    sentences = [s.strip() for s in re.split(r'[\n\.\?\!]+', text) if len(s.strip()) > 10]
    q_words = set(clean.lower().split())
    best_sent, best_score = raw_quote, 0
    for sent in sentences:
        s_words = set(sent.lower().split())
        overlap = len(q_words & s_words)
        if overlap > best_score:
            best_score = overlap
            best_sent = sent
    if best_score >= 3 and best_sent in text:
        return best_sent
    return raw_quote

# Test with the 4 failed quotes
test_cases = [
    ('slide-day19-20', 's35', 'Chuẩn hoá notes thành trace codes. Trace codes — ngôn ngữ chung của team. Cùng một vấn đề, cùng một tên. ... Khó đo Khó so sánh Khó sửa -> Đo được So sánh được Sửa được'),
    ('slide-day19-20', 's66', 'Đo công việc AI làm ra — PM là người định nghĩa “tốt”'),
    ('slide-day19-20', 's27', 'Coverage = chọn ô có chủ đích\nKhông phải test hết 16 ô — mà biết rõ vì sao chọn ô này, bỏ ô kia.\n■ Chọn test — có ý nghĩa sản phẩm ▨ Loại — tổ hợp phi lý'),
    ('ai-evals-m07', 'optimizing-the-judge-prompt', 'A judge prompt needs more structure than a typical agent prompt to reduce ambiguity. A reliable judge prompt usually includes: - A clear role... - A single evaluation question... - A concrete standard... - Ambiguous examples... - Self-Reflection... - A strict output format.')
]

for doc_id, sec_id, raw_q in test_cases:
    g = ground_quote(doc_id, sec_id, raw_q)
    text = sec_map.get((doc_id, sec_id), '')
    print('Doc:', doc_id, sec_id)
    print('Raw:', repr(raw_q[:50]))
    print('Grounded:', repr(g[:50]))
    print('Verbatim in section text?', g in text)
    print('---')
