# Scripts for 1-command validation of Track 1 Day 21 AI Evaluation Lab
$env:PYTHONUTF8 = '1'

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Running Full Validation Suite (Offline) " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

Write-Host "`n[1/4] Running Official Eval-Kit Tests (44 tests)..." -ForegroundColor Yellow
python -X utf8 tests\test_eval_kit.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL: Official eval-kit tests failed!" -ForegroundColor Red
    exit 1
}

Write-Host "`n[2/4] Running Extended Code Checks Unit Tests (15 tests)..." -ForegroundColor Yellow
python -X utf8 tests\test_code_checks.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL: Code checks unit tests failed!" -ForegroundColor Red
    exit 1
}

Write-Host "`n[3/4] Validating Dataset v1 Structure & Integrity..." -ForegroundColor Yellow
python evals\validate_dataset.py deliverables\evidence\dataset-v1.jsonl
if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL: Dataset validation failed!" -ForegroundColor Red
    exit 1
}

Write-Host "`n[4/4] Checking Git Diff Formatting..." -ForegroundColor Yellow
git diff --check
if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL: Git diff formatting errors found!" -ForegroundColor Red
    exit 1
}

Write-Host "`n==========================================" -ForegroundColor Green
Write-Host " ALL OFFLINE VALIDATIONS PASSED (100%)    " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
