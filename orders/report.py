'''A plain text summary of an order.'''

from decimal import Decimal

from orders.parse import Line
from orders.pricing import line_total


def summary(lines: list[Line]) -> str:
    """One row per line, then the total before GST.

    Uses the same pricing logic as ``line_total`` for each line, ensuring that
    bulk discounts are reflected both in the per‑line amounts and the final
    total row.
    """
    rows: list[str] = []
    total = Decimal(0)
    for line in lines:
        amount = line_total(line)
        rows.append(f"{line.sku} x{line.quantity} {amount:.2f}")
        total += amount
    rows.append(f"TOTAL {total:.2f}")
    return "\n".join(rows)
