# -*- coding: utf-8 -*-
"""This module tests changer function.
"""

import sys
from unittest.mock import patch
from unittest import TestCase
from changer.changer import Changer


class FormattedOutput(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)


class Test(TestCase):

    def setUp(self):
        self.formatted_output = FormattedOutput()
        self.changer = Changer()


    @patch('builtins.input', return_value=24)
    def test_positive_flow_24(self, input):
        """when input is 24, the result should be:
           1 * 20 cent coin
           2 * 2 cent coin
        """
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.changer.run()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                '> 1 * 20 cent coin\n> 2 * 2 cent coin\n')

    @patch('builtins.input', return_value=-24)
    def test_negative_flow_n24(self, input):
        """when input is -24, the result should be:
           'Target amount must be positive integer.'
        """
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.changer.run()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                'Target amount must be positive integer.\n')

    @patch('builtins.input', return_value=0)
    def test_negative_flow_zero(self, input):
        """when input is 0, the result should be:
           'No change needed.'
        """
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.changer.run()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                'No change needed.\n')

    @patch('builtins.input', return_value='some_string')
    def test_negative_flow_string(self, input):
        """when input is string, the result should be:
           'This was not a number, please try again.'
        """
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.changer.run()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                'This was not a number, please try again.\n')