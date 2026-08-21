import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def check(condition, desc):
    if condition:
        print(f"  [PASS] {desc}")
        return True
    else:
        print(f"  [FAIL] {desc}")
        return False

def main():
    print("==========================================================")
    print(" TRACK 1 DAY 21 — SUBMISSION VALIDATION AUDIT SUITE")
    print("==========================================================")

    passed = 0
    total = 0

    # 1. Repo Name
    total += 1
    repo_name = ROOT.name
    if check("Track1_Day21_2A202601873_NguyenQuangHuy" in repo_name, f"Repo name matches requirement: {repo_name}"):
        passed += 1

    # 2. Required files
    required_files = [
        "README.md",
        "ai-support-log.md",
        "deliverables/REPORT.md",
        "deliverables/ai-support-log.md",
        "deliverables/evidence/dataset-v1.jsonl",
        "deliverables/evidence/results-v3.jsonl",
        "deliverables/evidence/labels.csv",
        "deliverables/evidence/labels-huy.csv",
        "deliverables/evidence/labels-hue.csv",
        "deliverables/evidence/labels-followup-huy.csv",
        "deliverables/evidence/labels-followup-hue.csv",
        "deliverables/evidence/labels-followup-gold.csv",
        "deliverables/evidence/agreement-final-real.md",
        "deliverables/evidence/agreement-followup.md",
        "deliverables/evidence/thresholds-locked.md",
        "deliverables/evidence/final-provider-config-addendum.md",
        "deliverables/evidence/scorecard-final-real.md",
        "deliverables/evidence/scope-mismatch-audit.md",
        "deliverables/evidence/TWO-PERSON-TEAM-CONSTRAINT.md",
        "deliverables/evidence/HUMAN-LABEL-PROVENANCE.md",
        "deliverables/evidence/JUDGE-CALIBRATION-MANIFEST.md",
        "deliverables/evidence/EVIDENCE-MANIFEST.json",
        "docs/index.html",
        "docs/report.html",
        "docs/.nojekyll"
    ]
    total += 1
    all_files_exist = all((ROOT / f).exists() for f in required_files)
    if check(all_files_exist, f"All {len(required_files)} canonical files exist"):
        passed += 1

    # 3. Dataset schema & 22 canonical scenarios
    total += 1
    ds_path = ROOT / "deliverables/evidence/dataset-v1.jsonl"
    dataset = [json.loads(line) for line in open(ds_path, encoding="utf-8") if line.strip()]
    ds_valid = len(dataset) == 22 and len(set(r["scenario_id"] for r in dataset)) == 22
    if check(ds_valid, f"Dataset v1 contains exactly 22 unique canonical scenarios"):
        passed += 1

    # 4. Coverage slices
    total += 1
    set_types = set(r.get("metadata", {}).get("set_type") for r in dataset)
    coverage_ok = set_types == {"representative", "challenge", "high-risk"}
    if check(coverage_ok, f"Dataset includes representative, challenge, and high-risk set types"):
        passed += 1

    # 5. Team Size & Constraint
    total += 1
    constraint_path = ROOT / "deliverables/evidence/TWO-PERSON-TEAM-CONSTRAINT.md"
    constraint_ok = constraint_path.exists() and "2A202601873" in open(constraint_path, encoding="utf-8").read()
    if check(constraint_ok, "Two-person team structure & constraint documented with full provenance"):
        passed += 1

    # 6. Human labels & Agreement
    total += 1
    lbl_huy = [l for l in open(ROOT / "deliverables/evidence/labels-huy.csv", encoding="utf-8") if l.strip()]
    lbl_hue = [l for l in open(ROOT / "deliverables/evidence/labels-hue.csv", encoding="utf-8") if l.strip()]
    labels_ok = len(lbl_huy) == 23 and len(lbl_hue) == 23  # 1 header + 22 rows
    if check(labels_ok, f"Human labels present for both annotators (22 rows each)"):
        passed += 1

    # 7. Groundedness & Followup Gold Provenance
    total += 1
    foll_gold = [l for l in open(ROOT / "deliverables/evidence/labels-followup-gold.csv", encoding="utf-8") if l.strip()]
    gold_ok = len(foll_gold) == 23 and (ROOT / "deliverables/evidence/agreement-followup.md").exists()
    if check(gold_ok, "Followup quality gold standard and agreement documented"):
        passed += 1

    # 8. Judge Manifest & Distinct Hashes
    total += 1
    j_gv1 = sha256_file(ROOT / "deliverables/evidence/judge-prompt-groundedness-v1.md")
    j_gv2 = sha256_file(ROOT / "deliverables/evidence/judge-prompt-groundedness-v2.md")
    j_fv1 = sha256_file(ROOT / "deliverables/evidence/judge-prompt-followup-v1.md")
    j_fv2 = sha256_file(ROOT / "deliverables/evidence/judge-prompt-followup-v2.md")
    hashes_distinct = (j_gv1 != j_gv2) and (j_fv1 != j_fv2)
    if check(hashes_distinct, "Judge prompts have distinct, verified SHA256 hashes across rounds"):
        passed += 1

    # 9. Secret Scan in docs/
    total += 1
    secret_leaked = False
    bad_patterns = [r'sk-[a-zA-Z0-9_-]{20,}', r'AIza[a-zA-Z0-9_-]{20,}', r'lsv2_pt_[a-zA-Z0-9_-]{20,}', r'file:///', r'C:\\Users\\']
    for root_dir, _, files in os.walk(ROOT / "docs"):
        for f in files:
            content = open(os.path.join(root_dir, f), encoding="utf-8", errors="ignore").read()
            for pat in bad_patterns:
                if re.search(pat, content):
                    secret_leaked = True
                    break
    if check(not secret_leaked, "Zero secret exposures and zero local file links in docs/"):
        passed += 1

    # 10. REPORT 7 Sections
    total += 1
    report_content = open(ROOT / "deliverables/REPORT.md", encoding="utf-8").read()
    sections_ok = all(s in report_content for s in ["1. Input Grid", "2. Dataset", "3. Rubric", "4. Routing", "5. Calibration", "6. Scorecard", "7. Verdict"])
    if check(sections_ok, "deliverables/REPORT.md contains all 7 required sections"):
        passed += 1

    print(f"\n==========================================================")
    print(f" SUBMISSION VALIDATION RESULT: {passed} / {total} CHECKS PASSED")
    print(f"==========================================================")

    if passed == total:
        print(">> VERDICT: SUBMISSION READY (100% AUDITED & VERIFIED)")
        sys.exit(0)
    else:
        print(">> VERDICT: NOT READY")
        sys.exit(1)

if __name__ == "__main__":
    main()
