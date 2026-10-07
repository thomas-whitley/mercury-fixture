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

    def test_order_total_rounds_each_line_gst(self):
        # Line 1: 1 * 3.33 -> 3.33 + 10% = 3.663 -> rounds to 3.66
        # Line 2: 1 * 6.66 -> 6.66 + 10% = 7.326 -> rounds to 7.33
        # Total: 3.66 + 7.33 = 10.99
        # (Unrounded sum would be 9.99 * 1.10 = 10.989 -> 10.99 anyway, let's use values that differ)
        # Line 1: 1 * 3.34 -> 3.34 + 10% = 3.674 -> rounds to 3.67
        # Line 2: 1 * 3.34 -> 3.34 + 10% = 3.674 -> rounds to 3.67
        # Sum of rounded lines: 3.67 + 3.67 = 7.34
        # Unrounded sum: 6.68 * 1.10 = 7.348 -> rounds to 7.35
        csv = "sku,quantity,unit_price\nA,1,3.34\nB,1,3.34\n"
        self.assertEqual(order_total(parse_orders(csv)), Decimal("7.34"))

    def test_summary_ends_with_the_total(self):
        self.assertEqual(summary(parse_orders(CSV)).splitlines()[-1], "TOTAL 22.50")
