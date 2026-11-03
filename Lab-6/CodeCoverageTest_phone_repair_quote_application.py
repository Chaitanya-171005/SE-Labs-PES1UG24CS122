
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# Test Case 1: Valid repair quotations
def test_repair_quotes():
    assert repair_quote("screen", "budget", False, False) == 4600
    assert repair_quote("screen", "flagship", True, True) == 9100
    assert repair_quote("battery", "budget", True, False) == 300
    assert repair_quote("camera", "budget", False, True) == 3300


# Test Case 2: Invalid repair inputs
def test_invalid_repair_inputs():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("speaker", "budget", False, False)

    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "premium", False, False)


# Test Case 3: Repair turnaround time
def test_repair_days():
    assert repair_days("battery", True, 2) == 1
    assert repair_days("screen", False, 0) == 8
    assert repair_days("battery", False, 1) == 3


# Test Case 4: Trade-in valuation
def test_trade_in_value():
    assert trade_in_value(10000, 6, False) == 6000
    assert trade_in_value(10000, 18, True) == 2000
    assert trade_in_value(10000, 36, False) == 2000
    assert trade_in_value(10000, 49, False) == 0

    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 12, False)

