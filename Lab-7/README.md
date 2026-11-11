
# Lab 7 — Fuzz Testing for Input Validation Bugs

## About

This lab applies property-based fuzz testing with **Hypothesis** and **Pytest** to the Lab 6 Phone Repair Quote application (`processor.py`). Fuzz tests found input validation bugs in all three functions (`repair_quote`, `repair_days`, `trade_in_value`), which were then fixed.

## GitHub Repository

**Forked Repository:** [L6_L7_59_phone_repair_quote](https://github.com/Chaitanya-171005/L6_L7_59_phone_repair_quote) (folder `LAB7`)

## Results

| Run | Result |
| :--- | :---: |
| Original code | **6 failed, 4 passed** |
| Corrected code | **10 passed** |

## Bugs Found and Fixed

| Function | Failing Input | Original Behaviour | Fix |
| :--- | :--- | :--- | :--- |
| `repair_quote` | `part=[]` / `{}` | `TypeError: unhashable type` | Check `part` is a `str` before lookup |
| `repair_quote` | non-bool `under_warranty` / `express` | Silently treated as truthy | Require `bool` |
| `repair_days` | `technicians_free=-1` | Accepted | Require `int >= 0` |
| `repair_days` | unknown part, non-bool stock flag | Accepted | Validate part and flag |
| `trade_in_value` | `None` / text price or age | `TypeError` | Require `int`, else `ValueError` |
| `trade_in_value` | `age=0.0`, `nan`, `inf`, `1e308` | Accepted / returns `nan` | Whole-number price and age only |

## Files

| File | Description |
| :--- | :--- |
| `processor.py` | Application with input validation bugs fixed |
| `original/processor.py` | Original Lab 6 code (used for the failing run) |
| `test_processor.py` | Hypothesis fuzz tests for all three functions |
| `Lab7_PES1UG24CS122.pdf` | Lab report with screenshots and source code |
| `Screenshots/` | Original run, failing tests, corrected run, passing tests |
| `README.md` | Lab documentation |

## Run

```bash
pip install pytest hypothesis
pytest -v
```

## Conclusion

Hypothesis fuzzing exposed six failing properties in the original code. After adding input validation, all 10 tests pass.
