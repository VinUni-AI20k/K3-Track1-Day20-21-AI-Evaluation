# Baseline Validation Report

- **Timestamp**: 2026-08-21T09:44:36+07:00
- **Branch**: `main`
- **Commit SHA**: `f580eecdcefc6078dc7d6c989b445a53e4d4c602`
- **Python Version**: 3.13.14
- **Operating System**: Windows (PowerShell)
- **Command**: `$env:PYTHONUTF8='1'; python tests\test_eval_kit.py; git diff --check`
- **Exit Code**: `0`
- **Test Results**: `44 PASS / 0 FAIL`
- **Git Diff Check**: Clean (Exit code 0, no trailing whitespace or merge conflict markers)

## Layer-by-Layer Test Breakdown

| Layer | Component Tested | Test Cases | Status |
|---|---|---|---|
| Tầng 1 | Text Utilities (`normalize`, `tokens`, `slugify`) | 3 | PASS |
| Tầng 2 | Corpus & Retrieval (`load_corpus`, 18 docs, slide deck retrieval) | 5 | PASS |
| Tầng 3 | KB Search Local (shape, `max_results`, fields) | 3 | PASS |
| Tầng 4 | JSON Parser (clean JSON, fenced JSON, broken JSON, loose newline) | 6 | PASS |
| Tầng 5 | Slide Context (`None`, full context, no keyword) | 3 | PASS |
| Tầng 5b | Provider Resolution (deepseek, openai, gemini, openrouter, gateway) | 6 | PASS |
| Tầng 6 | Tool Calling Loop Mock (parse, tool record, usage accumulation, max steps) | 9 | PASS |
| Tầng 7 | Judge & Report Helpers (prompt context, cost calculation) | 4 | PASS |
| Tầng 7b | Tracing Backend (`noop`, fallback, warning handling) | 5 | PASS |

## Diagnostic Observations & Warnings

- **LangSmith Tracing Warning**: Warning intercepted gracefully when API key is simulated without active session (`'NoneType' object has no attribute 'setdefault'`). Test verified error is warned and does not raise exception.
- **Braintrust Package Note**: `braintrust` library is optional in offline mode; system gracefully defaults to noop/fallback.
