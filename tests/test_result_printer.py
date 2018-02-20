# -*- coding: utf-8 -*-
"""This module tests result printer.
"""

import sys
import unittest
import coin_changer.config as config
from coin_changer.result_printer import ResultPrinter


class FormattedOutput(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)


class TestResultPrinter(unittest.TestCase):
    """Test result printer

    """

    def setUp(self):
        self.coins = [1, 2, 5, 10, 20, 50]
        self.change = [1, 0, 0, 1, 0, 3]
        self.formatted_output = FormattedOutput()

    def test_print_result(self):
        self.result_printer = ResultPrinter(self.coins, self.change)
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.result_printer.print_result()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                '3 * 50 cent coin\n1 * 10 cent coin\n1 * 1 cent coin\n')
