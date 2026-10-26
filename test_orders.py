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
        # 10 items of SKU A at 10.00 each -> bulk discount 5% off line total
        csv = "sku,quantity,unit_price\nA,10,10.00\n"
        lines = parse_orders(csv)
        # line_total before GST: 10*10 = 100, minus 5% = 95.00
        self.assertEqual(summary(lines), "A x10 95.00\nTOTAL 95.00")

    def test_summary_multiple_lines_with_bulk_discount(self):
        csv = "sku,quantity,unit_price\nA,10,10.00\nB,5,2.00\n"
        lines = parse_orders(csv)
        # A: 100 * 0.95 = 95.00, B: 5*2 = 10.00 (no discount)
        self.assertEqual(summary(lines), "A x10 95.00\nB x5 10.00\nTOTAL 105.00")
