'''Prices lines. Ten or more of one SKU takes 5 percent off. GST is 10 percent.'''

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
    """Calculate the order total by applying GST to each line individually,
    rounding each line's total to the cent (half‑up), then summing.

    Args:
        lines: A list of :class:`orders.parse.Line` objects.

    Returns:
        Decimal: The summed total of all GST‑inclusive, rounded line totals.
    """
    total = Decimal(0)
    for line in lines:
        # Apply GST to the line total and round to the cent using half‑up.
        line_with_gst = (line_total(line) * (1 + GST)).quantize(CENT, rounding=ROUND_HALF_UP)
        total += line_with_gst
    return total
