"""Prices lines. Ten or more of one SKU takes 5 percent off. GST is 10 percent."""

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
    """The order's total including GST, rounded per line to the cent, half up."""
    total = Decimal(0)
    for line in lines:
        line_before_gst = line_total(line)
        line_with_gst = line_before_gst * (1 + GST)
        rounded_line = line_with_gst.quantize(CENT, rounding=ROUND_HALF_UP)
        total += rounded_line
    return total
