"""Read-only structural and mandatory-slice validation for Dataset v1."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


DATASET = Path(__file__).with_name("dataset_v1.csv")
REQUIRED = {
    "scenario_id",
    "user_input",
    "dimension_values",
    "expected_behavior",
    "risk_if_fail",
    "set_type",
}
VALID_SET_TYPES = {"representative", "challenge", "high-risk"}


def fail(messages: list[str]) -> int:
    print("FAIL: Dataset v1 does not satisfy Gate 1 validation.")
    for message in messages:
        print(f"- {message}")
    return 1


def main() -> int:
    errors: list[str] = []
    if not DATASET.exists():
        return fail([f"Missing dataset: {DATASET}"])

    with DATASET.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        rows = list(reader)

    missing_columns = sorted(REQUIRED - fieldnames)
    if missing_columns:
        errors.append(f"Missing required columns: {', '.join(missing_columns)}")

    if not 20 <= len(rows) <= 30:
        errors.append(f"Expected 20-30 rows; found {len(rows)}")

    ids: list[str] = []
    inputs: list[str] = []
    set_types: Counter[str] = Counter()
    slice_counts: Counter[str] = Counter()

    for number, row in enumerate(rows, start=2):
        for column in REQUIRED:
            if column in fieldnames and not (row.get(column) or "").strip():
                errors.append(f"CSV row {number}: empty {column}")

        scenario_id = (row.get("scenario_id") or "").strip()
        user_input = (row.get("user_input") or "").strip()
        set_type = (row.get("set_type") or "").strip().lower()
        dimensions = (row.get("dimension_values") or "").lower()

        ids.append(scenario_id)
        inputs.append(user_input)
        set_types[set_type] += 1

        if set_type not in VALID_SET_TYPES:
            errors.append(f"CSV row {number}: invalid set_type {set_type!r}")
        if "out-of-scope" in dimensions or "out of scope" in dimensions:
            slice_counts["out-of-scope"] += 1
        if "ambiguous" in dimensions or "referentially underspecified" in dimensions:
            slice_counts["ambiguous"] += 1
        if "multi-intent" in dimensions or "multi intent" in dimensions:
            slice_counts["multi-intent"] += 1
        if "unsupported" in dimensions:
            slice_counts["unsupported"] += 1

    duplicate_ids = sorted(key for key, count in Counter(ids).items() if key and count > 1)
    duplicate_inputs = sorted(key for key, count in Counter(inputs).items() if key and count > 1)
    if duplicate_ids:
        errors.append(f"Duplicate scenario_id values: {duplicate_ids}")
    if duplicate_inputs:
        errors.append(f"Duplicate exact user_input values: {duplicate_inputs}")

    for slice_name in ("out-of-scope", "ambiguous"):
        if slice_counts[slice_name] < 2:
            errors.append(f"Expected >=2 {slice_name} rows; found {slice_counts[slice_name]}")
    if set_types["high-risk"] < 2:
        errors.append(f"Expected >=2 high-risk rows; found {set_types['high-risk']}")

    if errors:
        return fail(errors)

    print(f"PASS: {len(rows)} valid rows")
    print(f"Unique scenarios: {len(set(ids))}")
    print(f"Set types: {dict(set_types)}")
    print(f"Mandatory slices: {dict(slice_counts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
