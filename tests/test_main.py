# -*- coding: utf-8 -*-
"""This module tests main function.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(sys.path)
from unittest.mock import patch
from unittest import TestCase
from coin_changer.main import Main


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
        self.main = Main()

   
    @patch('builtins.input', return_value=24)
    def test_positive_flow_24(self, input):
        stdout_org = sys.stdout
        try:
            sys.stdout = self.formatted_output
            self.main.main()
        finally:
            sys.stdout = stdout_org
            self.assertEqual(
                str(self.formatted_output),
                '1 * 20 cent coin\n2 * 2 cent coin\n')