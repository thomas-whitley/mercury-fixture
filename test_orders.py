import unittest
from decimal import Decimal

from orders import InvalidOrders, order_total, parse_orders, summary

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

    def test_order_total_rounds_per_line(self):
        # Three lines each 0.015 before GST -> each with GST 0.0165 rounds to 0.02
        csv = "sku,quantity,unit_price\nX,1,0.015\nY,1,0.015\nZ,1,0.015\n"
        lines = parse_orders(csv)
        # Per-line rounding: 0.02 * 3 = 0.06
        self.assertEqual(order_total(lines), Decimal("0.06"))
        # Old method would give 0.05 (0.045 * 1.10 = 0.0495 -> 0.05)

    def test_summary_ends_with_the_total(self):
        self.assertEqual(summary(parse_orders(CSV)).splitlines()[-1], "TOTAL 22.50")
