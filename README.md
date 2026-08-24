# Restaurant Bill

This repository contains a small Python script named `Restaurant Bill` that demonstrates basic numeric input, tip calculation, rounding, and simple arithmetic operations.

Below is an explanation of what the script does (without changing the original code) and examples showing how to use other mathematical operators in Python.

## What the script does

- The script asks the user to enter a restaurant bill amount (a floating-point number).
- It sets a tip percentage (15% in the script) and calculates the tip value as `bill * tip`.
- It computes the total cost as `bill + val_tip`.
- It prints the tip and total cost, including rounded values using Python's built-in `round()` function.
- The script also demonstrates adding two bills together (simple addition).

In the file named `Restaurant Bill` the key lines correspond to:
- `bill = float(input("Enter your resturant bill: R"))` — reads a bill amount from the user.
- `tip = 0.15` — tip percentage (15%).
- `val_tip = bill * tip` — tip amount calculated (multiplication).
- `total_cost = bill + val_tip` — total (addition).
- `print(... round(..., 2))` — examples of rounding to two decimal places.
- Later: `bill1 = float(input("Enter bill 1: R"))`, `bill2 = float(input("Enter bill 2: R"))` and `total_bill = bill1 + bill2` — demonstrates combining bills.

## Rounding and absolute value notes
- `round(value, n)` rounds `value` to `n` decimal places. Example: `round(3.14159, 2)` → `3.14`.
- `abs(value)` returns the absolute value (removes the negative sign). Example: `abs(-7)` → `7`.

## Other mathematical operators and examples
Below are examples you can try (these are small independent snippets that illustrate common operators). They do not modify the original script — they are examples you can run interactively or paste into a small Python file.

1) Addition (+)
```python
# Add two bill values
bill1 = 45.50
bill2 = 30.25
total = bill1 + bill2
print(total)  # 75.75
```

2) Subtraction (-)
```python
# Subtract a discount from a bill
bill = 100.00
discount = 15.00
subtotal = bill - discount
print(subtotal)  # 85.0
```

3) Multiplication (*)
```python
# Multiply to scale a value (e.g., two items of same price)
price_per_item = 12.50
quantity = 3
cost = price_per_item * quantity
print(cost)  # 37.5
```

4) Division (/)
```python
# Division returns a floating point result
total = 75.0
people = 4
share = total / people
print(share)  # 18.75
```

5) Floor division (//)
```python
# Floor division truncates (returns integer-like result)
total_cents = 375  # 3.75 in Rands expressed as cents
per_person_cents = total_cents // 4
print(per_person_cents)  # 93 (cents)
```

6) Modulus (%)
```python
# Remainder after division
total = 100
per_person = 3
remainder = total % per_person
print(remainder)  # 1
```

7) Exponentiation (**)
```python
# Power operator
base = 3
power = 2
result = base ** power
print(result)  # 9
```

8) Absolute value and round
```python
print(abs(-3.5))       # 3.5
print(round(3.14159, 2))  # 3.14
```

9) Using math.floor and math.ceil for explicit control (requires import)
```python
import math
print(math.floor(3.9))  # 3
print(math.ceil(3.1))   # 4
```

## Quick example: tip and per-person share
```python
# Example combining several operators
bill = 120.00
tip_percentage = 0.18
tip_value = bill * tip_percentage          # multiplication
total = bill + tip_value                   # addition
people = 5
per_person = total / people                # division
per_person_rounded = round(per_person, 2)  # rounding
print(per_person_rounded)  # e.g. 28.32
```

## Running the example script
A small example script was added at `examples/example_script.py` which demonstrates tip calculation, combining bills, splitting per-person, and other operators.

To run the example script from the repository root:

    python3 examples/example_script.py

(Or: `python examples/example_script.py` depending on your system's Python setup.)

You should see printed output showing the bill, tip, total, per-person share, combined bills, and operator demonstrations.

## Summary
- The `Restaurant Bill` script uses simple numeric input, multiplication for tip calculation, addition for totals, and `round()` for formatting output.
- This README adds extra examples to illustrate subtraction, multiplication, division, floor division, modulus, exponentiation, absolute value, and rounding.

If you'd like, I can also:
- add a short example that reads values from command-line arguments,
- show how to wrap the script into a reusable function,
- or add a small test/example script in the repo demonstrating the new operator examples.

Which of those (if any) would you like me to add next?