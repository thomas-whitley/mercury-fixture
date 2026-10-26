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

    def test_summary_uses_bulk_discount(self):
        csv_bulk = "sku,quantity,unit_price\nC,10,10.00\n"
        lines = parse_orders(csv_bulk)
        summary_output = summary(lines).splitlines()
        # First line should reflect 5% bulk discount on 10 * 10.00 = 100.00 -> 95.00
        self.assertEqual(summary_output[0], "C x10 95.00")
        # Total line should match the discounted amount
        self.assertEqual(summary_output[-1], "TOTAL 95.00")
