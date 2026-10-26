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
    """Parse CSV text into a list of :class:`Line` objects.

    Lines with a quantity less than 1 or with an invalid price are considered
    bad and will cause an :class:`InvalidOrders` exception containing the
    offending line numbers (header counted as line 1).
    """
    lines: list[Line] = []
    bad: list[int] = []
    for number, row in enumerate(csv.DictReader(io.StringIO(text)), start=2):
        try:
            qty = int(row["quantity"])
            price = Decimal(row["unit_price"])
            # Quantity must be at least 1; otherwise treat as bad line.
            if qty < 1:
                raise ValueError
            lines.append(Line(row["sku"].strip(), qty, price))
        except (ValueError, InvalidOperation, TypeError, AttributeError):
            bad.append(number)
    if bad:
        raise InvalidOrders(bad)
    return lines
