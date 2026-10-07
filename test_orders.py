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
        """Summary should apply bulk discounts to line amounts and total."""
        csv = (
            "sku,quantity,unit_price\n"
            "A,2,10.00\n"            # 2 * 10.00 = 20.00 (no discount)
            "C,10,1.00\n"            # 10 * 1.00 = 10.00 - 5% = 9.50 (discount)
        )
        lines = parse_orders(csv)
        summary_text = summary(lines)
        # Expect the discounted amount for SKU C and correct total
        expected_lines = [
            "A x2 20.00",
            "C x10 9.50",
            "TOTAL 29.50",
        ]
        self.assertEqual(summary_text.splitlines(), expected_lines)
