import os
import sys
import pytest

# Ensure repository root is on sys.path so we can import examples.example_script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from examples.example_script import (
    calculate_tip,
    total_with_tip,
    combine_bills,
    split_bill,
)


def test_calculate_tip():
    assert calculate_tip(100.0, 0.15) == pytest.approx(15.0)
    assert calculate_tip(0.0, 0.20) == pytest.approx(0.0)


def test_total_with_tip():
    assert total_with_tip(100.0, 0.15) == pytest.approx(115.0)
    assert total_with_tip(50.0, 0.10) == pytest.approx(55.0)


def test_combine_bills():
    bills = [10.0, 20.0, 30.5]
    assert combine_bills(bills) == pytest.approx(60.5)
    assert combine_bills([]) == pytest.approx(0.0)


def test_split_bill_exact_division():
    # exact division
    assert split_bill(100.0, 4) == 25.00


def test_split_bill_rounding():
    # result will be rounded to 2 decimal places
    result = split_bill(100.0, 3)
    assert result == round(100.0 / 3, 2)


def test_split_bill_invalid_people():
    with pytest.raises(ValueError):
        split_bill(100.0, 0)
