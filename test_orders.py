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

    def test_summary_uses_line_total_with_bulk_discount(self):
        csv = "sku,quantity,unit_price\nC,10,5.00\n"
        expected = ["C x10 47.50", "TOTAL 47.50"]
        self.assertEqual(summary(parse_orders(csv)).splitlines(), expected)

    def test_summary_mixed_bulk_and_regular_items(self):
        csv = (
            "sku,quantity,unit_price\n"
            "A,10,1.00\n"  # bulk discount: 10*1 =10 -> 5% off => 9.50
            "B,2,2.00\n"   # no discount: 2*2 =4.00
        )
        expected = ["A x10 9.50", "B x2 4.00", "TOTAL 13.50"]
        self.assertEqual(summary(parse_orders(csv)).splitlines(), expected)
