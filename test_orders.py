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

    def test_summary_ends_with_the_total(self):
        self.assertEqual(summary(parse_orders(CSV)).splitlines()[-1], "TOTAL 22.50")

    def test_order_total_rounds_each_line(self):
        # Build an order where per‑line rounding matters.
        csv = "sku,quantity,unit_price\nA,2,1.23\nB,1,2.34\n"
        lines = parse_orders(csv)
        # Expected:
        # A: 2 * 1.23 = 2.46; *1.10 = 2.706 → 2.71
        # B: 1 * 2.34 = 2.34; *1.10 = 2.574 → 2.57
        # Total = 5.28
        expected = Decimal('5.28')
        self.assertEqual(order_total(lines), expected)


if __name__ == '__main__':
    unittest.main()
