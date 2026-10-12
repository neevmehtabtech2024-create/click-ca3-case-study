# CA-3 Case Study Report: Click on Windows

## 1. Introduction

Click is a Python package used to build command-line interfaces. This case study investigates a Windows-specific issue involving `click.launch(..., locate=True)` when the target file or folder path contains spaces.

**Upstream issue:** https://github.com/pallets/click/issues/2994  
**Related pull request:** https://github.com/pallets/click/pull/3478

This is an investigation and reproduction of an upstream issue and its fix. It is not a claim that the student authored the upstream patch.

## 2. Problem statement

The upstream issue reports unexpected Windows Explorer behavior when Click is asked to locate a path containing spaces. In the local test performed for this case study, the command targeting `C:\Users\Public\click demo` opened Documents with Click 8.2.1 instead of selecting the requested folder.

The upstream pull request is titled “Fix 2994 launch locate files w spaces windows” and was merged into the `stable` branch on May 19, 2026.

## 3. Objective

- Reproduce the reported behavior on Windows.
- Compare the observed result using Click 8.2.1 and Click 8.4.1.
- Inspect the upstream patch and explain the change accurately.
- Record the test environment, steps, results, and limitations.

## 4. Environment

| Item | Value |
|---|---|
| Operating system | Windows |
| Python | 3.13.3 |
| Initial Click version | 8.2.1 |
| Comparison Click version | 8.4.1 |
| Test path | `C:\Users\Public\click demo` |

## 5. Reproduction procedure

Create and activate a virtual environment:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install click==8.2.1
```

Run the script:

```powershell
python .\reproduction\click-demo.py
```

The script creates two folders, `click-demo` and `click demo`, under `C:\Users\Public`, then calls `click.launch(..., locate=True)` for each.

To test the path with spaces directly:

```powershell
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

After recording the result and version, upgrade Click:

```powershell
python -m pip install --upgrade click==8.4.1
python -c "import click; print(click.__version__)"
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

For a fair comparison, use the same target path and command in both versions. Record whether Explorer opens the requested parent folder and whether it highlights the target.

## 6. Observed results

These results reflect the local test reported by the student. The screenshots in `evidence/` should be used to substantiate the observations.

| Click version | Local observation |
|---|---|
| 8.2.1 | The test opened Documents rather than selecting `C:\Users\Public\click demo`. |
| 8.4.1 | The test opened `C:\Users\Public` and highlighted `click demo`. |

The version comparison shows different behavior in this Windows environment. A local test is not, by itself, proof of the cause of the defect.

## 7. Upstream patch analysis

The Files changed view of PR #3478 shows a one-line change in `src/click/_termui_impl.py` in the Windows branch of the `locate` handling.

Before:

```python
args = ["explorer", f"/select,{url}"]
```

After:

```python
args = ["explorer", "/select,", url]
```

The patch changes the argument list passed to `subprocess.call`. The `/select,` option and the target path are supplied as separate list elements rather than combining the option and path into one element. This is the specific code change visible in the upstream diff.

The pull request is marked merged and shows a merge date of May 19, 2026. Refer to the linked upstream issue and pull request for the original discussion, review, and complete project context.

## 8. Discussion

The local comparison is consistent with the reported Windows path-with-spaces issue and the behavior expected after the upstream change. The change to argument construction is directly visible in the pull request diff.

The test is intentionally small and manual. It uses Windows File Explorer as an external application, so the observed result depends on the local operating system and environment. This case study did not independently instrument Explorer or exhaustively test other path forms.

## 9. Limitations

- The test was run in one Windows environment with Python 3.13.3.
- The test covers a small set of paths and does not establish behavior for every Windows path.
- The local before-and-after test demonstrates observed behavior, not a complete automated regression test suite.
- The root-cause explanation is based on the upstream diff; it should not be represented as a code change authored by the student.
- Screenshots document the local experiment but do not replace the upstream issue and pull-request references.

## 10. Conclusion

In the local test, Click 8.2.1 opened Documents instead of selecting a target folder whose path contained a space. With Click 8.4.1, Explorer opened the Public folder and highlighted the target folder. The upstream PR changes the Windows Explorer argument list so that `/select,` and the target path are passed as separate arguments.

This case study demonstrates how to identify an upstream issue, reproduce reported behavior, compare versions, inspect a patch, and document results with evidence.

## 11. References

1. Click issue #2994: https://github.com/pallets/click/issues/2994
2. Click pull request #3478: https://github.com/pallets/click/pull/3478
3. Click documentation: https://click.palletsprojects.com/

## 12. Evidence appendix

See the `evidence/` directory for screenshots supplied from the local test. Keep the screenshots authentic and label them clearly in the final presentation.
