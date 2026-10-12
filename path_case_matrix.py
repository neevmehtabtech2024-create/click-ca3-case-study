"""Manual regression matrix for Click launch(locate=True) on Windows.

Run in a Windows terminal after installing the Click version to test:
    python path_case_matrix.py

Explorer opens once for each case. Check whether the expected parent folder
opens and the target item is highlighted. This is a manual diagnostic, not an
automated assertion about Explorer behavior.
"""
from pathlib import Path
import click

ROOT = Path(r"C:\Users\Public")
CASES = [
    ("plain", "click-ca3-plain"),
    ("spaces", "click CA3 spaces"),
    ("parentheses", "click-ca3 (parentheses)"),
    ("ampersand", "click-ca3 & symbols"),
    ("unicode", "click-ca3 café"),
]

def main():
    print(f"Click version: {getattr(click, '__version__', 'unknown')}")
    print("For each case, inspect Explorer and record whether the target is selected.")
    for label, folder_name in CASES:
        target = ROOT / folder_name
        target.mkdir(parents=True, exist_ok=True)
        input(f"\nCase: {label}\nTarget: {target}\nPress Enter to launch Explorer...")
        click.launch(str(target), locate=True)
        result = input("Was the target selected correctly? [y/n/skip]: ").strip().lower()
        print(f"RESULT,{label},{target},{result or 'not-recorded'}")

if __name__ == "__main__":
    main()
