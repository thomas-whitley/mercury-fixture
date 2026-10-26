import unittest
from decimal import Decimal

from orders import InvalidOrders, order_total, parse_orders, summary, line_total

CSV = "sku,quantity,unit_price\nA,2,10.00\nB,1,2.50\n"


class Orders(unittest.TestCase):
    def test_parses_lines(self):
        self.assertEqual([line.sku for line in parse_orders(CSV)], ["A", "B"])

    def test_reports_every_bad_price_by_line_number(self):
        with self.assertRaises(InvalidOrders) as caught:
            parse_orders("sku,quantity,unit_price\nA,1,x\nB,1,1\nC,1,y\n")
        self.assertEqual(caught.exception.line_numbers, [2, 4])

    def test_order_total_includes_gst(self):
        self.assertEqual(order_total(parse_orders(CSV)), Decimal("24.75"))

    def test_summary_ends_with_the_total(self):
        self.assertEqual(summary(parse_orders(CSV)).splitlines()[-1], "TOTAL 22.50")

    def test_order_total_rounds_per_line(self):
        # Two lines where rounding per line differs from rounding on the whole order
        csv_small = "sku,quantity,unit_price\nA,1,0.04\nB,1,0.04\n"
        lines = parse_orders(csv_small)
        # line_total for each line should be 0.04, GST makes 0.044 which rounds to 0.04 per line
        # Sum of rounded lines = 0.08, whereas whole‑order rounding would give 0.09
        self.assertEqual(order_total(lines), Decimal('0.08'))
        # Ensure line_total itself is unchanged (no rounding, no GST)
        self.assertEqual(line_total(lines[0]), Decimal('0.04'))
        self.assertEqual(line_total(lines[1]), Decimal('0.04'))
