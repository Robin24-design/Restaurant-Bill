"""examples/example_script.py

Small example script showing how to use the Restaurant Bill operations
and other mathematical operators. This file is independent and does not
modify the original `Restaurant Bill` script.

Usage:
    python examples/example_script.py

It prints sample outputs for tip calculation, combining bills, splitting
per-person, and demonstrates subtraction, floor division, modulus, and
exponentiation.
"""

from typing import List
import math


def calculate_tip(bill: float, tip_pct: float = 0.15) -> float:
    """Return the tip value for a given bill and tip percentage."""
    return bill * tip_pct


def total_with_tip(bill: float, tip_pct: float = 0.15) -> float:
    """Return the total bill including tip."""
    tip = calculate_tip(bill, tip_pct)
    return bill + tip


def combine_bills(bills: List[float]) -> float:
    """Return the sum of a list of bills."""
    return sum(bills)


def split_bill(total: float, people: int) -> float:
    """Split a total among people and return a rounded per-person share."""
    if people <= 0:
        raise ValueError("people must be > 0")
    return round(total / people, 2)


def main() -> None:
    # Sample values
    bill = 120.00
    tip_pct = 0.18

    tip_value = calculate_tip(bill, tip_pct)
    total = total_with_tip(bill, tip_pct)

    print(f"Bill: R{bill}")
    print(f"Tip ({tip_pct*100:.0f}%): R{round(tip_value, 2)}")
    print(f"Total with tip: R{round(total, 2)}")

    # Split among people
    people = 5
    per_person = split_bill(total, people)
    print(f"Per person (split among {people}): R{per_person}")

    # Combine bills example (addition)
    bills = [45.50, 30.25, 80.00]
    combined = combine_bills(bills)
    print(f"Combined bills: R{round(combined, 2)}")

    # Subtraction (discount)
    discount = 10.00
    after_discount = combined - discount
    print(f"After discount (R{discount} off): R{round(after_discount,2)}")

    # Floor division and modulus (working in cents for clarity)
    total_cents = int(round(after_discount * 100))  # convert to cents
    per_person_cents = total_cents // people
    remainder_cents = total_cents % people
    print(f"Per person (cents, floor division): {per_person_cents} cents")
    print(f"Remainder (cents): {remainder_cents} cents")

    # Exponentiation example
    print(f"3 to the power of 2 is: {3 ** 2}")

    # Using math.floor and math.ceil
    print(f"math.floor(3.9): {math.floor(3.9)}")
    print(f"math.ceil(3.1): {math.ceil(3.1)}")


if __name__ == "__main__":
    main()
