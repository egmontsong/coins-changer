# -*- coding: utf-8 -*-
"""This module tests main function.
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
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.changer.run()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                '1 * 20 cent coin\n2 * 2 cent coin\n')