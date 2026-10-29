# Lab 5 – Static Code Analysis

**Course:** Software Engineering (SE) Lab  
**Name:** Chaitanya Krishna M  
**SRN:** PES1UG24CS122  
**Section:** 5th Semester, Section B  
**Program:** Insurance Premium Calculator (`premium_calculator.py`)  
**Tools:** Pylint, Flake8, Bandit  
**Date of Completion:** 28 October 2026

---

## Objective

Run static analysis tools on a deliberately flawed Python program, document the quality, style and security issues they report, fix them, and confirm the fixes by re-running the tools.

## Links

| Item | Link |
| :--- | :--- |
| Forked Repo (code, commits, reports) | https://github.com/Chaitanya-171005/L5_59-insurance-premium-calculator |

## Overview

An insurance premium calculator that quotes health, motor and life premiums, works out an applicant's age, saves quotes to a log, imports policies from partner XML, downloads rate tables, extracts customer claim archives, splits premiums into instalments and computes renewal dates.

## Results

| Tool | Before | After |
| :--- | :---: | :---: |
| **Bandit** | 10 issues (1 High, 5 Medium, 4 Low) | 0 issues (1 justified `# nosec B310`) |
| **Flake8** | 19 findings (E302, E305, E501, E722) | 0 findings |
| **Pylint** | 5.73 / 10 | **9.78 / 10** |

The remaining Pylint messages are `R0913` / `R0917` (too many arguments) on `calculate_premium`. They were left as is to keep the public function signature stable.

## What I Did

Each tool was run, its findings were fixed, and the result was committed separately.

| Step | Commit message | What changed |
| :---: | :--- | :--- |
| 1 | `fix: resolve Bandit security findings` | Safe `tarfile` extraction, `defusedxml` for XML, verified SSL and `https`-only downloads, localhost binding, secrets moved to environment variables, `secrets` instead of `random`, constant-time token check |
| 2 | `style: fix Flake8 formatting issues` | Blank lines between definitions, long lines wrapped, bare `except` replaced |
| 3 | `refactor: fix Pylint issues, score 9.78/10` | snake_case names, docstrings, mutable default argument, `with open(...)`, `enumerate`, `if __name__ == "__main__"` guard |
| 4 | `docs: add issues.md` | Full issue table with line numbers, types and fix approach |

### Highlights

- **Path traversal (Bandit B202, High):** `tarfile.extractall` is now called with `filter="data"`, so a customer archive cannot write outside `claims_docs`.
- **Mutable default argument (a bug no tool flags as a bug):** `discounts=[]` was shared between calls, so identical quotes returned `6000.0` and then `5500.0`. Now `discounts=None`, and the stray `append(500)` is removed.
- **Secrets and configuration:** the underwriter token and log path now come from environment variables instead of source code and `/tmp`.

## Issues Found but Not Fixed

These were found by running the program and reading its output. No tool flags them. They are documented in [`issues.md`](issues.md) with a proposed fix for each.

| Issue | Effect |
| :--- | :--- |
| `smoker="no"` is treated as a smoker | Any non-empty string is truthy, so the 1.3x loading is applied |
| Age ignores the birthday | DOB 31-12-1990 gives 36 instead of 35 |
| Premium can go negative | Stacked discounts gave `-800.0` |
| Instalments lose paise | `math.floor` means 12 instalments do not add up to the premium |
| Renewal crashes on 29 Feb | `date.replace(year=...)` raises `ValueError` in a non-leap year |

## How to Run

Python 3.12+ is recommended (the `tarfile` `filter` argument).

```bash
git clone https://github.com/Chaitanya-171005/L5_59-insurance-premium-calculator.git
cd L5_59-insurance-premium-calculator
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
python -m pip install pylint bandit flake8 defusedxml
```

Run the program (the token is optional; without it `is_authorised` always returns `False`):

```bash
export UNDERWRITER_TOKEN="uw-7f3a9c2e1b"
export PREMIUM_LOG_FILE="premium_quotes.log"    # optional, this is the default
python premium_calculator.py
```

Re-run the analysis:

```bash
python -m pylint premium_calculator.py
python -m bandit -r premium_calculator.py
python -m flake8 premium_calculator.py
```

## Files in this folder

| File | Description |
| :--- | :--- |
| `premium_calculator.py` | Cleaned version of the program |
| `issues.md` | Issue table (found and fixed, and found but not fixed) |
| `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` | Final reports after the fixes |
| `reports/` | Reports on the original code (`*_before.txt`) |
| `README.md` | This file |
