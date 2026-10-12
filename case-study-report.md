# CA-3 Case Study Report: Click on Windows

## Introduction

Click is a Python package for building command-line interfaces. This case study examines a Windows-specific issue involving `click.launch(..., locate=True)` when the target path contains spaces.

- **Upstream issue #2994:** https://github.com/pallets/click/issues/2994
- **Merged upstream fix, PR #3478:** https://github.com/pallets/click/pull/3478
- **Related earlier PR #3440 (closed, not merged):** https://github.com/pallets/click/pull/3440
- **Follow-up changelog PR #3498:** https://github.com/pallets/click/pull/3498

## Project overview and repository investigation

Click is maintained by the Pallets project. Its repository includes implementation code, tests, documentation, and release notes. The relevant implementation is `src/click/_termui_impl.py`, where Windows `locate=True` behavior builds the arguments passed to Explorer.

Project: https://github.com/pallets/click  
Documentation: https://click.palletsprojects.com/  
Contribution entry point: https://github.com/pallets/click/contribute

## Issue investigation

Issue #2994 was opened by **wireddown on July 4, 2025**. GitHub currently marks it **Closed**; the activity records it as completed on **May 19, 2026**, and the milestone is **8.4.1**. The report describes Explorer opening Documents instead of locating a target path containing spaces.

Maintainer discussion includes davidism's July 4, 2025 comment that the `/select` argument needs quoting. Later activity links commits to the issue, and the issue was marked completed after the fix was merged. Source: https://github.com/pallets/click/issues/2994

## Bug investigation and local reproduction

**Environment:** Windows; Python 3.13.3; Click 8.2.1 and 8.4.1; target path `C:\Users\Public\click demo`.

The local test used:

```powershell
python -c "import click; click.launch(r'C:\Users\Public\click demo', locate=True)"
```

**Observed locally:**

| Click version | Result reported in the group's test |
|---|---|
| 8.2.1 | Explorer opened Documents instead of selecting the target folder. |
| 8.4.1 | Explorer opened `C:\Users\Public` and highlighted `click demo`. |

These are observations from one Windows environment. They should not be presented as a guarantee for every system.

## Pull-request investigation

### PR #3478 — the merged fix

PR #3478, “Fix 2994 launch locate files w spaces windows,” was merged by Rowlando13 into the `stable` branch on **May 19, 2026**. GitHub shows **11 checks passed**, **no reviews**, and the **8.4.1 milestone**. The Files changed view shows this one-line change in `src/click/_termui_impl.py`:

Before:
```python
args = ["explorer", f"/select,{url}"]
```

After:
```python
args = ["explorer", "/select,", url]
```

This separates the `/select,` option and path into different arguments. PR page: https://github.com/pallets/click/pull/3478

### PR #3440 — do not confuse it with the merged fix

PR #3440 proposed quoting the path inside a single `/select,"..."` argument and included a proposed test. It was **closed on May 17, 2026, not merged**. On August 8, 2026, it received a “rejected AI” label and was removed from the 8.4.1 milestone. It must not be cited as the accepted upstream contribution. Source: https://github.com/pallets/click/pull/3440

### PR #3498 — changelog follow-up

PR #3498 was merged into `stable` on **May 30, 2026**. Its discussion explicitly lists PR #3478 among the changes missing a changelog reference after the 8.4.1 release, and one commit adds the missing changelog entry. Source: https://github.com/pallets/click/pull/3498

**Release evidence:** PR #3478 and issue #2994 both show milestone **8.4.1**, and the local comparison reported Click 8.4.1 behaving correctly. The merged PR is evidence the fix landed in the 8.4.1 milestone; the local test is evidence only for this machine.

## Contribution process

Click's contribution entry point links to its contribution guidance: https://github.com/pallets/click/contribute. The standard workflow is to read project guidance, inspect existing issues, reproduce the problem, create a focused branch, add tests or documentation, run relevant checks, open a pull request, and respond to review feedback.

The upstream patch was contributed by PlumLariat with collaboration noted from Rowlando13; the student group did not author PR #3478.

## Changes / contribution by the student group

To make our own work visible, the group prepared `contribution/path_case_matrix.py`, a small manual regression matrix that checks path names with:
- plain characters;
- spaces;
- parentheses;
- ampersands;
- a Unicode character.

It asks the tester to record whether Explorer selects each target. This is a **manual diagnostic tool**, not an automated unit test. It has been prepared locally for review and testing; it should only be described as completed, tested, committed, or pushed after the group actually runs it and records the corresponding evidence. It is not an upstream Click change.

## Practical observations and limitations

- The original path-with-spaces case was reproduced locally on Click 8.2.1 and compared with Click 8.4.1.
- The merged PR's actual change differs from the proposed change in PR #3440; citing the correct PR is important.
- The path matrix broadens the experiment, but its cases still require manual execution and observation on Windows.
- A warning about `click.__version__` is a deprecation warning, not the folder-selection result. Use `importlib.metadata.version("click")` to display the installed version without relying on the deprecated attribute.

## GitHub activity and division of work

Use meaningful commits rather than “Add files via upload.” Each member should commit a genuine part they personally worked on, for example:
- repository and project overview;
- issue and reproduction notes;
- pull-request and code-diff investigation;
- path-matrix implementation, evidence, and final review.

Do not fabricate commits or split one person's work among accounts. Record actual authorship and activity. The guidelines state three students per group, while this report currently lists four; confirm the permitted group size with the instructor. The group number and project guide remain blank until confirmed.

## Conclusion

The group investigated Click issue #2994, reproduced the Windows path-with-spaces behavior locally, compared Click 8.2.1 with 8.4.1, and inspected the correct merged fix in PR #3478. PR #3440 was a separate closed proposal and should not be confused with the merged patch. The student-owned path matrix provides a small extension to the practical investigation, but must be run and documented before its results are claimed.

## References

1. Issue #2994: https://github.com/pallets/click/issues/2994
2. Merged PR #3478: https://github.com/pallets/click/pull/3478
3. Closed PR #3440: https://github.com/pallets/click/pull/3440
4. Changelog follow-up PR #3498: https://github.com/pallets/click/pull/3498
5. Click documentation: https://click.palletsprojects.com/
6. Click contribution entry point: https://github.com/pallets/click/contribute
