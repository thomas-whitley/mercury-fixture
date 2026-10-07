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
    """Parse CSV order text into a list of :class:`Line` objects.

    A line is considered invalid if:
    - ``quantity`` cannot be converted to an ``int``;
    - ``quantity`` is less than 1;
    - ``unit_price`` cannot be converted to a ``Decimal``;
    - any required field is missing or malformed.
    Invalid lines are collected and reported via :class:`InvalidOrders` with their
    line numbers (header is line 1).
    """
    lines: list[Line] = []
    bad: list[int] = []
    for number, row in enumerate(csv.DictReader(io.StringIO(text)), start=2):
        try:
            sku = row["sku"].strip()
            quantity = int(row["quantity"])
            # Treat quantities below 1 as invalid
            if quantity < 1:
                raise ValueError("quantity must be >= 1")
            unit_price = Decimal(row["unit_price"])
            lines.append(Line(sku, quantity, unit_price))
        except (ValueError, InvalidOperation, TypeError, AttributeError):
            bad.append(number)
    if bad:
        raise InvalidOrders(bad)
    return lines
