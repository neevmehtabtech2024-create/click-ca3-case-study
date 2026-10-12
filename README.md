# Click CA-3 Case Study

**Course:** Open Source Technologies (OST) — CA-3  
**Project:** Investigating Windows folder selection behavior in Click

## Overview

This repository documents a local investigation of `click.launch(..., locate=True)` on Windows when the target path contains a space. It compares Click 8.2.1 with Click 8.4.1 and examines the upstream fix.

## Upstream references

- Issue: https://github.com/pallets/click/issues/2994
- Pull request: https://github.com/pallets/click/pull/3478

PR #3478 changes the Windows Explorer argument list in `src/click/_termui_impl.py`: `/select,` and the target path are passed as separate arguments. The pull request was merged on May 19, 2026.

## Environment

- Windows
- Python 3.13.3
- Click 8.2.1 (initial test)
- Click 8.4.1 (comparison test)

## Reproduction

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install click==8.2.1
python .\reproduction\click-demo.py
```

Single-path test:

```powershell
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

For the comparison:

```powershell
python -m pip install --upgrade click==8.4.1
python -c "import click; print(click.__version__)"
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

## Local observations

- Click 8.2.1: Documents opened instead of selecting the target folder.
- Click 8.4.1: `click demo` was highlighted in `C:\Users\Public`.

These are observations from one local Windows environment, not proof of behavior on every system.

## Repository contents

- `reproduction/` — minimal reproduction script
- `evidence/` — screenshots from the local tests
- `report/` — case-study report draft
- `requirements.txt` — initial Click version for reproducing the first test

See `report/case-study-report.md` for the detailed methodology, observed results, upstream patch analysis, limitations, and references.

This repository documents an existing upstream fix; it does not claim authorship of the upstream patch.
