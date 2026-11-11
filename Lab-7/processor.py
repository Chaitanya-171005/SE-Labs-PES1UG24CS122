"""Phone repair quote module (Lab 6 application, fixed for Lab 7 fuzz-found bugs).

Every function validates its input and raises ValueError for anything
outside its documented domain, instead of crashing with TypeError or
silently returning garbage (negative technicians, NaN/inf prices, ...).
"""

PART_COST = {"screen": 4000, "battery": 1500, "camera": 2500, "charging_port": 800}


def _is_int(value):
    """True for real integers; bool is a subclass of int, so exclude it."""
    return isinstance(value, int) and not isinstance(value, bool)


def _check_part(part):
    # isinstance check first: an unhashable value (list/dict) would make
    # `part in PART_COST` raise TypeError instead of ValueError.
    if not isinstance(part, str) or part not in PART_COST:
        raise ValueError("unknown part")


def _check_bool(value, name):
    if not isinstance(value, bool):
        raise ValueError("invalid " + name)


def repair_quote(part, brand_tier, under_warranty, express):
    _check_part(part)
    if not isinstance(brand_tier, str) or brand_tier not in ("budget", "flagship"):
        raise ValueError("unknown brand tier")
    _check_bool(under_warranty, "under_warranty")
    _check_bool(express, "express")
    cost = PART_COST[part]
    if brand_tier == "flagship":
        cost = cost * 2
    if part == "screen":
        labour = 600
    else:
        labour = 300
    if under_warranty and part != "screen":
        cost = 0
    total = cost + labour
    if express:
        total += 500
    return total


def repair_days(part, parts_in_stock, technicians_free):
    _check_part(part)
    _check_bool(parts_in_stock, "parts_in_stock")
    if not _is_int(technicians_free) or technicians_free < 0:
        raise ValueError("invalid technicians_free")
    if technicians_free == 0:
        days = 3
    else:
        days = 1
    if not parts_in_stock:
        if part == "screen" or part == "camera":
            days += 5
        else:
            days += 2
    return days


def trade_in_value(original_price, age_months, screen_cracked):
    # Whole-number price/age only: floats let NaN, inf and overflow
    # (1e308 * 60 -> inf -> nan) slip through the old `<= 0` checks.
    if not _is_int(original_price) or not _is_int(age_months):
        raise ValueError("invalid input")
    _check_bool(screen_cracked, "screen_cracked")
    if original_price <= 0 or age_months < 0:
        raise ValueError("invalid input")
    if age_months > 48:
        return 0
    if age_months <= 12:
        value = original_price * 60 // 100
    elif age_months <= 24:
        value = original_price * 40 // 100
    else:
        value = original_price * 20 // 100
    if screen_cracked:
        value = value // 2
    return value


if __name__ == "__main__":
    print(repair_quote("screen", "budget", False, False))
    print(repair_days("screen", False, 0))
    print(trade_in_value(50000, 10, False))
