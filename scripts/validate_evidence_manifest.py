import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def main():
    manifest_path = ROOT / "deliverables/evidence/EVIDENCE-MANIFEST.json"
    if not manifest_path.exists():
        print(f"FAIL: {manifest_path} not found")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    artifacts = data.get("artifacts", {})
    failed = 0
    passed = 0

    print("== Evidence Manifest Validation ==")
    for rel_path, meta in artifacts.items():
        full_path = ROOT / rel_path
        if not full_path.exists():
            print(f"  FAIL: File missing: {rel_path}")
            failed += 1
            continue

        actual_hash = sha256_file(full_path)
        expected_hash = meta.get("sha256")
        if actual_hash != expected_hash:
            print(f"  FAIL: Hash mismatch for {rel_path}:\n    Expected: {expected_hash}\n    Actual:   {actual_hash}")
            failed += 1
        else:
            print(f"  ok  {rel_path}")
            passed += 1

    print(f"\nManifest Validation Summary: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
    print("ALL EVIDENCE MANIFEST HASHES VERIFIED (100%)")

if __name__ == "__main__":
    main()
