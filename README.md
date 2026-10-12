# Click CA-3 Case Study

**Course:** Open Source Technologies (OST) — CA-3  
**Project:** Investigating Windows folder selection behavior in Click  
**Status:** Local reproduction and version comparison in progress

## Overview
This repository documents a local investigation of `click.launch(..., locate=True)` on Windows when the target path contains a space. It compares Click 8.2.1 with Click 8.4.1. Report local observations separately from upstream claims.

## Upstream references
- Issue: https://github.com/pallets/click/issues/2994
- Pull request: https://github.com/pallets/click/pull/3478

Verify the current issue and pull-request pages before submission and describe their contents accurately.

## Environment
- Operating system: Windows
- Python: 3.13.3
- Initial Click version: 8.2.1
- Comparison Click version: 8.4.1

## Reproduction
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install click==8.2.1
python .\reproduction\click-demo.py
```

For comparison:
```powershell
python -m pip install --upgrade click==8.4.1
python -c "import click; print(click.__version__)"
python .\reproduction\click-demo.py
```

The script creates `C:\Users\Public\click-demo` and `C:\Users\Public\click demo`, then asks Explorer to locate each. Close Explorer windows between runs if needed.

## Observed results
- Click 8.2.1: the single-path test for `C:\Users\Public\click demo` opened Documents rather than selecting the target folder.
- Click 8.4.1: the same single-path test selected `click demo` in `C:\Users\Public`.

These are local observations, not proof of the underlying root cause.

## Evidence
Add genuine, unedited screenshots to `evidence/`, for example:
- `before-click-8.2.1.png`
- `after-click-8.4.1.png`
- `terminal-results.png`

## Submission checklist
- [ ] Add genuine screenshots
- [ ] Verify upstream issue and PR details
- [ ] Complete `report/case-study-report.md`
- [ ] Add any instructor-required presentation or reflection
- [ ] Commit and push the finished files
