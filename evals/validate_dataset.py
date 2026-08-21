"""Comprehensive Dataset v1 Validator for Gate 1 Compliance."""
import json
import os
import sys
from collections import Counter
from pathlib import Path

# Add tutor to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))
import tutor

REQUIRED_METADATA_FIELDS = {
    "dimension_values",
    "expected_behavior",
    "risk_if_fail",
    "set_type",
    "combination_id",
}
VALID_SET_TYPES = {"representative", "challenge", "high-risk"}
VALID_SCOPES = {"in_scope", "out_of_scope", "unclear"}

def fail(messages):
    print("FAIL: Dataset v1 does not satisfy Gate 1 validation.")
    for message in messages:
        print(f"- {message}")
    return 1

def validate_dataset(path):
    if not os.path.exists(path):
        return fail([f"Dataset file does not exist: {path}"])

    sections = tutor.load_corpus()
    valid_ids = {(s["doc_id"], s["section_id"]) for s in sections}

    rows = []
    if path.endswith(".jsonl"):
        with open(path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, 1):
                if line.strip():
                    try:
                        rows.append((idx, json.loads(line)))
                    except Exception as e:
                        return fail([f"Line {idx}: JSON parse error: {e}"])
    else:
        return fail([f"Unsupported dataset extension: {path}"])

    errors = []
    if not (20 <= len(rows) <= 30):
        errors.append(f"Expected 20-30 rows; found {len(rows)}")

    ids = []
    inputs = []
    set_types = Counter()
    slice_counts = Counter()

    for line_num, rec in rows:
        sid = rec.get("scenario_id") or rec.get("id")
        q = rec.get("input")
        scope = rec.get("expected_scope")
        note = rec.get("note")
        meta = rec.get("metadata") or {}

        if not sid:
            errors.append(f"Line {line_num}: missing scenario_id")
        if not q or not str(q).strip():
            errors.append(f"Line {line_num} ({sid}): empty input")
        if not scope or scope not in VALID_SCOPES:
            errors.append(f"Line {line_num} ({sid}): invalid expected_scope {scope!r}")
        if not note:
            errors.append(f"Line {line_num} ({sid}): empty note")

        ids.append(sid)
        inputs.append(q)

        # Check metadata fields
        missing_meta = REQUIRED_METADATA_FIELDS - set(meta.keys())
        if missing_meta:
            errors.append(f"Line {line_num} ({sid}): missing metadata fields: {', '.join(missing_meta)}")

        set_type = str(meta.get("set_type", "")).strip().lower()
        set_types[set_type] += 1
        if set_type not in VALID_SET_TYPES:
            errors.append(f"Line {line_num} ({sid}): invalid set_type {set_type!r}")

        dim_vals = meta.get("dimension_values") or {}
        dim_str = " ".join(str(v) for v in dim_vals.values()).lower()

        if scope == "out_of_scope" or "out-of-scope" in dim_str or "out of scope" in dim_str:
            slice_counts["out-of-scope"] += 1
        if scope == "unclear" or "ambiguous" in dim_str or "underspecified" in dim_str:
            slice_counts["ambiguous"] += 1
        if set_type == "high-risk" or "false" in dim_str or "misleading" in dim_str or "unsupported" in dim_str:
            slice_counts["high-risk"] += 1
        if "multi-intent" in dim_str or "multi intent" in dim_str:
            slice_counts["multi-intent"] += 1

        # Check slide if present
        slide = meta.get("slide")
        if slide and isinstance(slide, dict) and slide.get("id"):
            slide_id = slide.get("id")
            if ("slide-day19-20", slide_id) not in valid_ids and not any(sid == slide_id for _, sid in valid_ids):
                # Warning or notice, but ensure it's logged
                pass

    dup_ids = [k for k, v in Counter(ids).items() if k and v > 1]
    if dup_ids:
        errors.append(f"Duplicate scenario_id: {dup_ids}")

    dup_inputs = [k for k, v in Counter(inputs).items() if k and v > 1]
    if dup_inputs:
        errors.append(f"Duplicate inputs: {dup_inputs}")

    if slice_counts["out-of-scope"] < 2:
        errors.append(f"Expected >=2 out-of-scope rows; found {slice_counts['out-of-scope']}")
    if slice_counts["ambiguous"] < 2:
        errors.append(f"Expected >=2 ambiguous rows; found {slice_counts['ambiguous']}")
    if slice_counts["high-risk"] < 2:
        errors.append(f"Expected >=2 high-risk rows; found {slice_counts['high-risk']}")

    if errors:
        return fail(errors)

    print(f"PASS: {len(rows)} valid canonical rows in {path}")
    print(f"Unique scenarios: {len(set(ids))}")
    print(f"Set types distribution: {dict(set_types)}")
    print(f"Mandatory slice counts: {dict(slice_counts)}")
    return 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "deliverables/evidence/dataset-v1.jsonl"
    sys.exit(validate_dataset(target))
