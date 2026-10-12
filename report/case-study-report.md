# CA-3 Case Study Report: Click on Windows

## 1. Project and issue
- Project: Click, a Python package for creating command-line interfaces
- Upstream issue: https://github.com/pallets/click/issues/2994
- Related pull request: https://github.com/pallets/click/pull/3478

Verify the upstream pages and summarize their actual descriptions and code changes before submission.

## 2. Objective
Investigate Windows behavior of `click.launch(..., locate=True)` when a target path contains a space, comparing two Click versions.

## 3. Environment
- OS: Windows
- Python: 3.13.3
- Initial Click version: 8.2.1
- Comparison Click version: 8.4.1

## 4. Reproduction procedure
1. Create and activate a virtual environment.
2. Install `click==8.2.1`.
3. Run `reproduction/click-demo.py`, or run the single-path command below.
4. Record which folder Explorer opens and whether the target is selected.
5. Upgrade to `click==8.4.1`.
6. Repeat the same test and record the result.

```powershell
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

## 5. Results

| Version | Observed result | Evidence |
|---|---|---|
| Click 8.2.1 | Documents opened rather than selecting the requested folder | Add screenshot filename |
| Click 8.4.1 | `click demo` was highlighted in `C:\Users\Public` | Add screenshot filename |

These are local observations. Update this table if a repeated test differs.

## 6. Analysis and limitations
The comparison suggests behavior differed between tested versions in this Windows environment. This experiment alone does not establish the root cause. Use the upstream PR's actual diff and discussion to explain the fix, distinguishing source-based findings from personal observations.

## 7. Conclusion
Summarize what the test demonstrated, what remains uncertain, and how the upstream fix relates to the behavior. Do not claim to have authored or contributed to the upstream fix unless you actually did so.

## 8. References
- https://github.com/pallets/click/issues/2994
- https://github.com/pallets/click/pull/3478
- https://click.palletsprojects.com/

## 9. Evidence appendix
List each screenshot and what it demonstrates. Include genuine screenshots in `evidence/`.
