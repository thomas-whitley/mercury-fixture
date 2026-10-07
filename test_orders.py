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

    def test_reports_bad_quantity_and_price(self):
        bad_csv = (
            "sku,quantity,unit_price\n"
            "A,1,1.00\n"      # line 2 - good
            "B,0,2.00\n"      # line 3 - bad quantity
            "C,2,3.00\n"      # line 4 - good
            "D,1,xyz\n"       # line 5 - bad price
        )
        with self.assertRaises(InvalidOrders) as caught:
            parse_orders(bad_csv)
        self.assertEqual(caught.exception.line_numbers, [3, 5])
