'''Parses an order CSV with the header sku,quantity,unit_price and no blank lines.'''

import csv
import io
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Line:
    sku: str
    quantity: int
    unit_price: Decimal


class InvalidOrders(ValueError):
    """Raised with every bad line's number, counting the header as line 1."""

    def __init__(self, line_numbers: list[int]) -> None:
        self.line_numbers = line_numbers
        super().__init__("invalid lines: " + ", ".join(map(str, line_numbers)))


def parse_orders(text: str) -> list[Line]:
    """Parse CSV text into a list of Line objects.

    Any line with an invalid SKU, a non‑integer quantity, a quantity less than 1,
    or an invalid unit_price is considered bad. All bad line numbers are
    collected (counting the header as line 1) and raised together via
    ``InvalidOrders``.
    """
    lines: list[Line] = []
    bad: list[int] = []
    for number, row in enumerate(csv.DictReader(io.StringIO(text)), start=2):
        try:
            # Strip whitespace from SKU
            sku = row["sku"].strip()
            # Parse quantity; ensure it is a positive integer (>=1)
            quantity = int(row["quantity"])  # may raise ValueError
            if quantity < 1:
                raise ValueError("quantity must be >= 1")
            # Parse unit price
            unit_price = Decimal(row["unit_price"])  # may raise InvalidOperation
            lines.append(Line(sku, quantity, unit_price))
        except (ValueError, InvalidOperation, TypeError, AttributeError):
            bad.append(number)
    if bad:
        raise InvalidOrders(bad)
    return lines
