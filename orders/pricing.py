'''Prices lines. Ten or more of one SKU takes 5 percent off. GST is 10 percent.'''

from decimal import ROUND_HALF_UP, Decimal

from orders.parse import Line

GST = Decimal('0.10')
BULK_QUANTITY = 10
BULK_DISCOUNT = Decimal('0.05')
CENT = Decimal('0.01')


def line_total(line: Line) -> Decimal:
    """The line's total before GST, after any bulk discount, not rounded."""
    total = line.quantity * line.unit_price
    if line.quantity >= BULK_QUANTITY:
        total -= total * BULK_DISCOUNT
    return total


def _rounded_line_total_including_gst(line: Line) -> Decimal:
    """Calculate a line's total *including* GST and round to the cent (half‑up)."""
    total_with_gst = line_total(line) * (1 + GST)
    return total_with_gst.quantize(CENT, rounding=ROUND_HALF_UP)


def order_total(lines: list[Line]) -> Decimal:
    """The order's total including GST.

    Each line's total (including GST) is rounded to the cent (half‑up) first,
    and the order total is the sum of those rounded line totals.
    """
    return sum((_rounded_line_total_including_gst(line) for line in lines), Decimal(0))
