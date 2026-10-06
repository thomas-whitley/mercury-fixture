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
        # Line 1: 3 * 3.33 = 9.99, + GST = 10.989 -> 10.99
        # Line 2: 1 * 3.33 = 3.33, + GST = 3.663 -> 3.66
        # Total: 10.99 + 3.66 = 14.65
        csv = "sku,quantity,unit_price\nA,3,3.33\nB,1,3.33\n"
        self.assertEqual(order_total(parse_orders(csv)), Decimal("14.65"))

    def test_summary_ends_with_the_total(self):
        self.assertEqual(summary(parse_orders(CSV)).splitlines()[-1], "TOTAL 22.50")
