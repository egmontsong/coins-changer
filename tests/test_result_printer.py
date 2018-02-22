# -*- coding: utf-8 -*-
"""This module tests result printer.
"""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from changer.result_printer import ResultPrinter


class TestResultPrinter(TestCase):
    """Test result printer

    """

    def setUp(self):
        self.coins = [1, 2, 5, 10, 20, 50]
        self.positive_change = [1, 0, 0, 1, 0, 3]
        self.zero_change = [0, 0, 0, 0, 0, 0]
        self.negative_change = [1, 0, 0, -1, 0, 3]

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_positive_result(self, mock_stdout):
        self.result_printer = ResultPrinter(self.coins, self.positive_change)
        self.result_printer.print_result()
        self.assertEqual(
                mock_stdout.getvalue(),
                '3 * 50 cent coin\n1 * 10 cent coin\n1 * 1 cent coin\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_zero_result(self, mock_stdout):
        self.result_printer = ResultPrinter(self.coins, self.zero_change)
        self.result_printer.print_result()
        self.assertEqual(
                mock_stdout.getvalue(),
                'No change needed.\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_negative_result(self, mock_stdout):
        self.result_printer = ResultPrinter(self.coins, self.negative_change)
        self.result_printer.print_result()
        self.assertEqual(
                mock_stdout.getvalue(),
                'Quantity of coins must be positive.\n')