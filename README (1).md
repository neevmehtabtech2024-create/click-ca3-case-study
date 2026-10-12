# Student contribution: Windows path-case matrix

This small utility extends the original single-path reproduction with a repeatable
manual test matrix for plain names, spaces, parentheses, ampersands, and a Unicode
character. It is intended to be run on Windows with Click 8.2.1 and then 8.4.1.

It opens Explorer for each path and asks the tester to record whether the expected
target is selected. Because Explorer is external and the result is manually observed,
this is not an automated unit test and does not prove all path forms are supported.

Run from a terminal:
```powershell
python -m pip install click==8.2.1
python .\contribution\path_case_matrix.py
```
Repeat after installing Click 8.4.1. Save the terminal output and screenshots as
evidence. Only report outcomes that were actually observed.
