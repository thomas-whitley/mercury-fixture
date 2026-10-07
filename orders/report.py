'''A plain text summary of an order.'''

from decimal import Decimal

from orders.parse import Line
from orders.pricing import line_total


def summary(lines: list[Line]) -> str:
    """One row per line, then the total before GST.
    Prices each line using the pricing logic (including bulk discounts).
    """
    rows: list[str] = []
    total: Decimal = Decimal(0)
    for line in lines:
        amount = line_total(line)
        rows.append(f"{line.sku} x{line.quantity} {amount:.2f}")
        total += amount
    rows.append(f"TOTAL {total:.2f}")
    return "\n".join(rows)
