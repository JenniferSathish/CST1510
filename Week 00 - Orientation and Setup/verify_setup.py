"""
VERIFY SETUP
==============
Run this in Week 7, after creating your virtual environment and installing
the packages (the Week 7 section of INSTALL.md). From the CST1510 folder, with the
environment turned on:

    python "Week 00 - Orientation and Setup/verify_setup.py"

It checks the things this module actually needs and nothing else. Every
check prints OK or MISSING - if anything is MISSING, fix that one thing and
run this again. It is safe to run as many times as you like.
"""

import shutil
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 10)

REQUIRED_PACKAGES = [
    "ipykernel",
    "pandas",
    "matplotlib",
    "requests",
    "bcrypt",
    "streamlit",
    "openai",
    "pytest",
]

HERE = Path(__file__).resolve().parent

failures = []


def check(label, ok, fix_hint=""):
    status = "OK" if ok else "MISSING"
    print(f"  [{status:7s}] {label}")
    if not ok:
        failures.append((label, fix_hint))


def repo_root():
    """Return the root folder of the Git repository this script is in, or None."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=HERE,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())


print("Python version")
check(
    f"Python {sys.version_info.major}.{sys.version_info.minor} (need {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+)",
    sys.version_info >= MIN_PYTHON,
    "Install a current Python from https://python.org, then redo the Week 7 section of INSTALL.md.",
)

print("\nVirtual environment")
check(
    "virtual environment is turned on",
    sys.prefix != sys.base_prefix,
    "Turn it on (INSTALL.md, Week 7 step 1): .venv\\Scripts\\activate on Windows, "
    "source .venv/bin/activate on macOS. Then run this script again.",
)

print("\nRequired packages")
for package in REQUIRED_PACKAGES:
    try:
        __import__(package)
        check(package, True)
    except ImportError:
        check(
            package,
            False,
            "With the environment turned on, run INSTALL.md Week 7 step 1: "
            'python -m pip install -r "Week 00 - Orientation and Setup/requirements.txt"',
        )

print("\nGit")
git_ok = shutil.which("git") is not None
check(
    "git is on your PATH",
    git_ok,
    "Install Git from https://git-scm.com and restart your terminal / VS Code.",
)

root = repo_root() if git_ok else None
check(
    "this folder is inside your CST1510 repository",
    root is not None,
    "Move the Week 00 folder into the CST1510 folder you cloned (INSTALL.md step 4).",
)

if root is not None:
    check(
        ".gitignore file in the repository folder",
        (root / ".gitignore").is_file(),
        f"Create .gitignore in {root} (INSTALL.md step 5).",
    )

print()
if not failures:
    print("Everything checks out.")
else:
    print(f"{len(failures)} thing(s) still need fixing:\n")
    previous_hint = None
    for label, hint in failures:
        print(f"  - {label}")
        if hint and hint != previous_hint:
            print(f"    fix: {hint}")
        previous_hint = hint
    print("\nFix these, then run this file again.")
    sys.exit(1)
