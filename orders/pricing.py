'''Pricing utilities for order calculations.

This module provides functions to calculate line totals and overall order totals,
including GST (Goods and Services Tax). The GST is applied at a rate of 10%.
The `order_total` function now rounds each line's total *including* GST to the
nearest cent using half‑up rounding, and then sums those rounded values.
'''  

from decimal import ROUND_HALF_UP, Decimal

from orders.parse import Line

GST = Decimal("0.10")
BULK_QUANTITY = 10
BULK_DISCOUNT = Decimal("0.05")
CENT = Decimal("0.01")


def line_total(line: Line) -> Decimal:
    """The line's total before GST, after any bulk discount, not rounded."""
    total = line.quantity * line.unit_price
    if line.quantity >= BULK_QUANTITY:
        total -= total * BULK_DISCOUNT
    return total


def order_total(lines: list[Line]) -> Decimal:
    """The order's total including GST.

    Each line's subtotal (including GST) is rounded to the nearest cent using
    half‑up rounding, and the order total is the sum of those rounded line
    amounts.
    """
    total = sum(
        (line_total(line) * (1 + GST)).quantize(CENT, rounding=ROUND_HALF_UP)
        for line in lines
    )
    return total
