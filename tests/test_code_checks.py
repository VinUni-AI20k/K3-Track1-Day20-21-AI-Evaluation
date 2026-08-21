import sys, os
from pathlib import Path

# Add eval and tutor to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "eval"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))

import tutor
import code_checks

def run_tests():
    sections = tutor.load_corpus()
    valid_ids = {(s["doc_id"], s["section_id"]) for s in sections}
    section_tokens = {(s["doc_id"], s["section_id"]): tutor.tokens(s["text"]) for s in sections}

    pass_count = 0
    fail_count = 0

    def check(name, condition, msg=""):
        nonlocal pass_count, fail_count
        if condition:
            pass_count += 1
            print(f"  ok  {name}")
        else:
            fail_count += 1
            print(f" FAIL {name}: {msg}")

    print("== Test Suite: Code Checks ==")

    # Case 1: Perfect in_scope record
    rec_perfect_in = {
        "scenario_id": "test-01",
        "output": {
            "scope": "in_scope",
            "answer": "Calibration là quá trình đo lường sự nhất quán...",
            "sources": [{"doc_id": "ai-evals-m09", "section_id": "why-calibration-is-the-whole-game", "quote": "Teams skip this step constantly"}],
            "followup_questions": ["Tại sao cần calibrate?", "Đo agreement thế nào?", "Khi nào nên dùng LLM judge?"]
        }
    }
    res = code_checks.run_checks_on_record(rec_perfect_in, valid_ids, section_tokens)
    check("perfect in_scope: schema_valid", res["schema_valid"][0] is True)
    check("perfect in_scope: citation_exists", res["citation_exists"][0] is True)
    check("perfect in_scope: quote_verbatim", res["quote_verbatim"][0] is True)
    check("perfect in_scope: scope_sources_consistency", res["scope_sources_consistency"][0] is True)
    check("perfect in_scope: followup_quality", res["followup_quality"][0] is True)
    check("perfect in_scope: sources_no_duplicates", res["sources_no_duplicates"][0] is True)

    # Case 2: Perfect out_of_scope record (with exactly 3 followup questions)
    rec_perfect_out = {
        "scenario_id": "test-02",
        "output": {
            "scope": "out_of_scope",
            "answer": "Câu hỏi này nằm ngoài phạm vi khóa học AI Evaluation.",
            "sources": [],
            "followup_questions": [
                "Bạn có muốn tìm hiểu về AI Eval Lifecycle không?",
                "Bạn có muốn tìm hiểu về cách thiết kế rubric không?",
                "Bạn có muốn tìm hiểu về LLM-as-a-judge không?"
            ]
        }
    }
    res = code_checks.run_checks_on_record(rec_perfect_out, valid_ids, section_tokens)
    check("perfect out_of_scope: schema_valid", res["schema_valid"][0] is True)
    check("perfect out_of_scope: scope_sources_consistency", res["scope_sources_consistency"][0] is True)
    check("perfect out_of_scope: followup_quality", res["followup_quality"][0] is True)

    # Case 3: Broken JSON / parse error
    rec_broken = {
        "scenario_id": "test-03",
        "output": {"_parse_error": True, "raw": "..."}
    }
    res = code_checks.run_checks_on_record(rec_broken, valid_ids, section_tokens)
    check("broken JSON: schema_valid is False", res["schema_valid"][0] is False)
    check("broken JSON: citation_exists is skipped (None)", res["citation_exists"][0] is None)

    # Case 4: Missing field in schema
    rec_missing = {
        "scenario_id": "test-04",
        "output": {"scope": "in_scope", "answer": "Missing sources and followups"}
    }
    res = code_checks.run_checks_on_record(rec_missing, valid_ids, section_tokens)
    check("missing fields: schema_valid is False", res["schema_valid"][0] is False)

    # Case 5: Fake non-existent citation
    rec_fake_cit = {
        "scenario_id": "test-05",
        "output": {
            "scope": "in_scope",
            "answer": "Test",
            "sources": [{"doc_id": "non-existent-doc", "section_id": "fake-sec", "quote": "fake"}],
            "followup_questions": ["Q1?", "Q2?", "Q3?"]
        }
    }
    res = code_checks.run_checks_on_record(rec_fake_cit, valid_ids, section_tokens)
    check("fake citation: citation_exists is False", res["citation_exists"][0] is False)

    # Case 6: Hallucinated quote (quote not in section)
    rec_hallu_quote = {
        "scenario_id": "test-06",
        "output": {
            "scope": "in_scope",
            "answer": "Test",
            "sources": [{"doc_id": "ai-evals-m09", "section_id": "why-calibration-is-the-whole-game", "quote": "This sentence definitely does not exist in module 9"}],
            "followup_questions": ["Q1?", "Q2?", "Q3?"]
        }
    }
    res = code_checks.run_checks_on_record(rec_hallu_quote, valid_ids, section_tokens)
    check("hallucinated quote: quote_verbatim is False", res["quote_verbatim"][0] is False)

    # Case 7: Inconsistent scope (out_of_scope with cited sources)
    rec_inconsistent = {
        "scenario_id": "test-07",
        "output": {
            "scope": "out_of_scope",
            "answer": "Out of scope but citing",
            "sources": [{"doc_id": "ai-evals-m09", "section_id": "why-calibration-is-the-whole-game", "quote": "Teams skip this step constantly"}],
            "followup_questions": ["Q1?", "Q2?", "Q3?"]
        }
    }
    res = code_checks.run_checks_on_record(rec_inconsistent, valid_ids, section_tokens)
    check("out_of_scope with sources: scope_sources_consistency is False", res["scope_sources_consistency"][0] is False)

    # Case 8: Duplicate sources
    rec_dup = {
        "scenario_id": "test-08",
        "output": {
            "scope": "in_scope",
            "answer": "Test dup",
            "sources": [
                {"doc_id": "ai-evals-m09", "section_id": "why-calibration-is-the-whole-game", "quote": "Teams skip this step constantly"},
                {"doc_id": "ai-evals-m09", "section_id": "why-calibration-is-the-whole-game", "quote": "Teams skip this step constantly"}
            ],
            "followup_questions": ["Q1?", "Q2?", "Q3?"]
        }
    }
    res = code_checks.run_checks_on_record(rec_dup, valid_ids, section_tokens)
    check("duplicate sources: sources_no_duplicates is False", res["sources_no_duplicates"][0] is False)

    # Case 9: Negative follow-up tests (0, 1, 2, 4 questions, empty/non-string)
    res_0 = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": []}})
    check("followup 0 items: False", res_0[0] is False)

    res_1 = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": ["Q1?"]}})
    check("followup 1 item: False", res_1[0] is False)

    res_2 = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": ["Q1?", "Q2?"]}})
    check("followup 2 items: False", res_2[0] is False)

    res_4 = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": ["Q1?", "Q2?", "Q3?", "Q4?"]}})
    check("followup 4 items: False", res_4[0] is False)

    res_empty = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": ["Q1?", "", "Q3?"]}})
    check("followup empty string item: False", res_empty[0] is False)

    res_nonstr = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": ["Q1?", 123, "Q3?"]}})
    check("followup non-string item: False", res_nonstr[0] is False)

    res_nonlist = code_checks.check_followup_quality({"output": {"scope": "in_scope", "followup_questions": "Q1, Q2, Q3"}})
    check("followup non-list: False", res_nonlist[0] is False)

    print(f"\nCode Checks Test Result: {pass_count} pass, {fail_count} fail")
    return fail_count == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
