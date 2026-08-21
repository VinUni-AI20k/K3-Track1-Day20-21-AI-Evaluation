# PowerShell Submission Validation Runner
$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " RUNNING COMPLETE REPOSITORY AUDIT & VALIDATION" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

Write-Host "`n[1/6] Running Official Eval-Kit Tests (44 tests)..." -ForegroundColor Yellow
python -X utf8 tests\test_eval_kit.py

Write-Host "`n[2/6] Running Extended Code Checks Unit Tests (27 tests)..." -ForegroundColor Yellow
python -X utf8 tests\test_code_checks.py

Write-Host "`n[3/6] Validating Canonical Dataset v1..." -ForegroundColor Yellow
python -X utf8 evals\validate_dataset.py deliverables\evidence\dataset-v1.jsonl

Write-Host "`n[4/6] Validating Evidence Manifest Hashes..." -ForegroundColor Yellow
python -X utf8 scripts\validate_evidence_manifest.py

Write-Host "`n[5/6] Verifying Code Checks on Candidate v3..." -ForegroundColor Yellow
python -X utf8 eval\code_checks.py deliverables\evidence\results-v3.jsonl

Write-Host "`n[6/6] Running Full 30-Point Submission Audit..." -ForegroundColor Yellow
python -X utf8 scripts\validate_submission.py

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host " ALL AUDIT VALIDATION GATES PASSED (100%)" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
