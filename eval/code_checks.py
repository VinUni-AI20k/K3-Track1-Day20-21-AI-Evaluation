"""Code checks — kiểm tra results.jsonl bằng rule thuần Python (không tốn API).

Đây là làn "Code check" của bài lab: những tiêu chí viết được thành rule thì kiểm
bằng code — nhanh, rẻ, khách quan, chạy lại bao nhiêu lần cũng được.

Chạy:  python3 eval/code_checks.py            # in bảng pass/fail từng check từng row
"""
import json
import os
import re
import sys
from pathlib import Path

# tutor.py nằm ở tutor/ (khu vực sản phẩm) — thêm vào sys.path để import được
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))

import tutor  # dùng lại load_corpus

EXPECTED_FIELDS = {"scope", "answer", "sources", "followup_questions"}
VALID_SCOPES = {"in_scope", "out_of_scope"}


def check_schema(rec):
    """Output parse được và đủ 4 field đúng contract."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return False, "JSON không parse được (xem raw_content)"
    missing = EXPECTED_FIELDS - set(out)
    if missing:
        return False, "thiếu field: " + ", ".join(sorted(missing))
    if out.get("scope") not in VALID_SCOPES:
        return False, f"scope không hợp lệ: {out.get('scope')!r} (kỳ vọng in_scope hoặc out_of_scope)"
    return True, None


def check_citation_exists(rec, valid_ids):
    """Mọi doc_id/section_id trong sources phải tồn tại thật trong corpus."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        key = (s.get("doc_id"), s.get("section_id"))
        if key not in valid_ids:
            return False, f'nguồn không tồn tại: {key[0]}#{key[1]}'
    return True, None


def _token_subsequence(needle, haystack):
    """True nếu chuỗi token của needle xuất hiện liên tiếp trong haystack."""
    if not needle:
        return True
    n = len(needle)
    return any(haystack[i:i + n] == needle for i in range(len(haystack) - n + 1))


def check_quote_verbatim(rec, section_tokens):
    """Quote phải nằm trong section đã cite — so theo chuỗi token (bỏ dấu, lowercase,
    bỏ mọi dấu câu/khoảng trắng) nên khác biệt gạch ngang/ngoặc kép không tính là sai."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        tokens = section_tokens.get((s.get("doc_id"), s.get("section_id")), [])
        quote_tokens = tutor.tokens(s.get("quote") or "")
        if quote_tokens and not _token_subsequence(quote_tokens, tokens):
            return False, f'quote không khớp section {s.get("section_id")}: "{(s.get("quote") or "")[:40]}..."'
    return True, None


def check_scope_sources_consistency(rec):
    """Kiểm tra tính nhất quán giữa scope và danh sách sources:
    - out_of_scope: sources phải rỗng (không được bịa trích dẫn).
    - in_scope: sources phải có >= 1 trích dẫn hợp lệ."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    scope = out.get("scope")
    sources = out.get("sources", [])
    if not isinstance(sources, list):
        return False, "sources phải là một list"
    if scope == "out_of_scope":
        if len(sources) > 0:
            return False, f"câu out_of_scope nhưng lại trích dẫn {len(sources)} sources"
    elif scope == "in_scope":
        if len(sources) == 0:
            return False, "câu in_scope nhưng sources bị rỗng"
    return True, None


def check_followup_quality(rec):
    """Kiểm tra cấu trúc câu hỏi gợi ý tiếp theo (followup_questions):
    - Phải là list chứa đúng 3 câu hỏi (cả in_scope và out_of_scope).
    - Mỗi câu hỏi phải là một chuỗi ký tự không rỗng."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    qs = out.get("followup_questions")
    if not isinstance(qs, list):
        return False, "followup_questions phải là một list"
    if len(qs) != 3:
        return False, f"followup_questions phải có đúng 3 câu hỏi (hiện có {len(qs)})"
    for q in qs:
        if not isinstance(q, str) or not q.strip():
            return False, "followup_questions chứa phần tử rỗng hoặc không phải string"
    return True, None


def check_expected_scope_match(rec):
    """Kiểm tra output.scope có khớp với expected_scope của dataset hay không."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    expected = rec.get("expected_scope")
    if expected is None:
        return None, "bỏ qua (không có trường expected_scope)"
    actual = out.get("scope")
    if actual != expected:
        return False, f"lệch scope: actual={actual!r} != expected={expected!r}"
    return True, None


def check_sources_no_duplicates(rec):
    """Đảm bảo không có nguồn trích dẫn trùng lặp (duplicate doc_id + section_id)."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    sources = out.get("sources") or []
    seen = set()
    for s in sources:
        key = (s.get("doc_id"), s.get("section_id"))
        if key in seen:
            return False, f"trùng lặp trích dẫn: {key[0]}#{key[1]}"
        seen.add(key)
    return True, None


CHECKS = [
    ("schema_valid", check_schema),
    ("citation_exists", check_citation_exists),
    ("quote_verbatim", check_quote_verbatim),
    ("expected_scope_match", check_expected_scope_match),
    ("scope_sources_consistency", check_scope_sources_consistency),
    ("followup_quality", check_followup_quality),
    ("sources_no_duplicates", check_sources_no_duplicates),
]


def run_checks_on_record(rec, valid_ids, section_tokens):
    """Chạy toàn bộ code checks trên 1 record, trả về dict kết quả {check_name: (bool|None, reason)}."""
    results = {}
    for name, fn in CHECKS:
        if fn in (check_schema, check_expected_scope_match, check_scope_sources_consistency, check_followup_quality, check_sources_no_duplicates):
            ok, reason = fn(rec)
        elif fn is check_citation_exists:
            ok, reason = fn(rec, valid_ids)
        elif fn is check_quote_verbatim:
            ok, reason = fn(rec, section_tokens)
        else:
            ok, reason = fn(rec)
        results[name] = (ok, reason)
    return results


def main(path="results.jsonl"):
    if not os.path.exists(path):
        raise SystemExit("Không thấy %s — chạy python3 eval/run_eval.py trước." % path)
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]

    sections = tutor.load_corpus()
    valid_ids = {(s["doc_id"], s["section_id"]) for s in sections}
    section_tokens = {(s["doc_id"], s["section_id"]): tutor.tokens(s["text"]) for s in sections}

    totals = {name: [0, 0] for name, _ in CHECKS}  # [pass, fail] (skip không đếm)
    for rec in rows:
        sid = rec.get("scenario_id", "?")
        res = run_checks_on_record(rec, valid_ids, section_tokens)
        line = [sid]
        for name, _ in CHECKS:
            ok, reason = res[name]
            if ok is None:
                line.append(f"{name}: skip")
                continue
            totals[name][0 if ok else 1] += 1
            line.append(f"{name}: {'pass' if ok else 'FAIL — ' + str(reason)}")
        print(" | ".join(line))

    print("\nTổng kết:")
    for name, (p, f) in totals.items():
        print(f"  {name}: {p} pass / {f} fail")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "results.jsonl")
