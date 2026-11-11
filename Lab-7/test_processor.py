"""Lab 7 - Hypothesis fuzz tests for processor.py (all three functions).

Two kinds of property per function:
  1. "Never crashes": for ANY input, the function either returns a value or
     raises ValueError -- never TypeError, never an unhandled exception.
  2. "Correct on valid input": for inputs inside the valid domain, the result
     satisfies the business rules.
"""
import pytest
from hypothesis import given, settings, strategies as st

from processor import PART_COST, repair_quote, repair_days, trade_in_value

PARTS = list(PART_COST)
TIERS = ["budget", "flagship"]

# Anything at all: None, bools, ints, floats (nan/inf), text, bytes, lists, dicts...
anything = st.one_of(
    st.none(),
    st.booleans(),
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.text(),
    st.binary(),
    st.lists(st.integers()),
    st.dictionaries(st.text(), st.integers()),
    st.sampled_from(PARTS + TIERS),
)

# Mostly *valid* values mixed with junk, to reach deeper code paths.
partish = st.one_of(st.sampled_from(PARTS), anything)
tierish = st.one_of(st.sampled_from(TIERS), anything)
boolish = st.one_of(st.booleans(), anything)

FUZZ = settings(max_examples=500, deadline=None)


def only_valueerror(fn, *args):
    """Call fn; only a result or ValueError is acceptable."""
    try:
        return fn(*args)
    except ValueError:
        return None


# ---------------------------------------------------------------- repair_quote
@FUZZ
@given(partish, tierish, boolish, boolish)
def test_repair_quote_never_crashes(part, tier, warranty, express):
    result = only_valueerror(repair_quote, part, tier, warranty, express)
    if result is not None:
        assert isinstance(result, int) and not isinstance(result, bool)
        assert result >= 300


@FUZZ
@given(st.sampled_from(PARTS), st.sampled_from(TIERS), st.booleans(), st.booleans())
def test_repair_quote_valid_inputs(part, tier, warranty, express):
    total = repair_quote(part, tier, warranty, express)
    labour = 600 if part == "screen" else 300
    assert total >= labour
    assert total <= PART_COST[part] * 2 + labour + 500
    # express always adds exactly 500
    assert total - repair_quote(part, tier, warranty, False) == (500 if express else 0)
    # flagship never cheaper than budget
    assert repair_quote(part, "flagship", warranty, express) >= repair_quote(part, "budget", warranty, express)


@FUZZ
@given(st.one_of(st.lists(st.integers()), st.dictionaries(st.text(), st.integers()),
                 st.none(), st.integers(), st.text().filter(lambda s: s not in PART_COST)))
def test_repair_quote_rejects_bad_part(part):
    with pytest.raises(ValueError):
        repair_quote(part, "budget", False, False)


# ----------------------------------------------------------------- repair_days
@FUZZ
@given(partish, boolish, anything)
def test_repair_days_never_crashes(part, in_stock, techs):
    result = only_valueerror(repair_days, part, in_stock, techs)
    if result is not None:
        assert 1 <= result <= 8


@FUZZ
@given(st.sampled_from(PARTS), st.booleans(), st.integers(min_value=0, max_value=10**6))
def test_repair_days_valid_inputs(part, in_stock, techs):
    days = repair_days(part, in_stock, techs)
    assert 1 <= days <= 8
    # no free technician is never faster than having one
    assert repair_days(part, in_stock, 0) >= repair_days(part, in_stock, 1)
    # parts out of stock is never faster than in stock
    assert repair_days(part, False, techs) >= repair_days(part, True, techs)


@FUZZ
@given(st.sampled_from(PARTS), st.booleans(), st.integers(max_value=-1))
def test_repair_days_rejects_negative_technicians(part, in_stock, techs):
    with pytest.raises(ValueError):
        repair_days(part, in_stock, techs)


# -------------------------------------------------------------- trade_in_value
@FUZZ
@given(anything, anything, boolish)
def test_trade_in_value_never_crashes(price, age, cracked):
    result = only_valueerror(trade_in_value, price, age, cracked)
    if result is not None:
        # never nan/negative, and never worth more than the original price
        assert isinstance(result, int)
        assert 0 <= result <= price


@FUZZ
@given(st.integers(min_value=1, max_value=10**9), st.integers(min_value=0, max_value=200), st.booleans())
def test_trade_in_value_valid_inputs(price, age, cracked):
    value = trade_in_value(price, age, cracked)
    assert isinstance(value, int)
    assert 0 <= value <= price * 60 // 100
    if age > 48:
        assert value == 0
    # a cracked screen never increases the value
    assert trade_in_value(price, age, True) <= trade_in_value(price, age, False)
    # older phones are never worth more
    assert trade_in_value(price, age + 1, cracked) <= value


@FUZZ
@given(st.one_of(st.floats(), st.integers(max_value=0), st.none(), st.text()),
       st.integers(min_value=0, max_value=100))
def test_trade_in_value_rejects_bad_price(price, age):
    with pytest.raises(ValueError):
        trade_in_value(price, age, False)


@FUZZ
@given(st.integers(min_value=1, max_value=10**6),
       st.one_of(st.integers(max_value=-1), st.floats(), st.none(), st.text()))
def test_trade_in_value_rejects_bad_age(price, age):
    with pytest.raises(ValueError):
        trade_in_value(price, age, False)
