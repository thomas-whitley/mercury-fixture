'''A plain text summary of an order.'''

from decimal import Decimal

from orders.parse import Line
from orders.pricing import line_total


def summary(lines: list[Line]) -> str:
    """One row per line, then the total before GST. Uses line_total for each line.

    The output format is exactly as before: each line is "SKU xQ amount" where amount is
    the line total before GST (including bulk discount) formatted to two decimal places,
    followed by a final "TOTAL amount" line.
    """
    rows: list[str] = []
    total = Decimal(0)
    for line in lines:
        amount = line_total(line)
        rows.append(f"{line.sku} x{line.quantity} {amount:.2f}")
        total += amount
    rows.append(f"TOTAL {total:.2f}")
    return "\n".join(rows)
