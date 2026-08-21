# Scripts for running live evaluation pipeline once API key is configured
$env:PYTHONUTF8 = '1'

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Starting Live AI Evaluation Pipeline     " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Preflight check
Write-Host "`n[1/5] Preflight Verification..." -ForegroundColor Yellow
python -X utf8 -c "import sys; sys.path.insert(0, 'tutor'); import tutor; print('Model:', tutor.MODEL); print('API Key present:', bool(tutor.get_api_key()))"

# 2. Run Tutor on Dataset
Write-Host "`n[2/5] Running Tutor on dataset.jsonl -> results.jsonl..." -ForegroundColor Yellow
python -X utf8 eval\run_eval.py dataset.jsonl
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error running tutor eval" -ForegroundColor Red
    exit 1
}

# 3. Snapshot results-v1
Copy-Item results.jsonl deliverables\evidence\results-v1.jsonl
Write-Host "Snapshotted results to deliverables\evidence\results-v1.jsonl" -ForegroundColor Green

# 4. Run Code Checks
Write-Host "`n[3/5] Running Deterministic Code Checks on results..." -ForegroundColor Yellow
python -X utf8 eval\code_checks.py deliverables\evidence\results-v1.jsonl

# 5. Generate HTML Report for Human Baseline
Write-Host "`n[4/5] Generating HTML report for human labeling..." -ForegroundColor Yellow
python -X utf8 eval\report.py

Write-Host "`n[5/5] Pipeline ready. Complete human labeling (labels-huy.csv, labels-hue.csv) to proceed with agreement and judge calibration." -ForegroundColor Green
