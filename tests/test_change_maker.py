# -*- coding: utf-8 -*-
"""This module tests change maker.
"""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from changer.change_maker import ChangeMaker


class TestChangeMaker(TestCase):
    """Test change maker

    """

    def setUp(self):
        self.coins = [1, 2, 5, 10, 20, 50]

    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_flow(self, mock_stdout):
        self.change_maker = ChangeMaker(-1, self.coins)
        self.change_maker.make_change()
        self.assertEqual(
                mock_stdout.getvalue(),
                'Target amount must be positive.\n')

    def test_zero_flow(self):
        self.change_maker = ChangeMaker(0, self.coins)
        self.assertEqual(self.change_maker.make_change(), [0, 0, 0, 0, 0, 0])

    def test_positive_flow_24(self):
        self.change_maker = ChangeMaker(24, self.coins)
        self.assertEqual(self.change_maker.make_change(), [0, 2, 0, 0, 1, 0])

    def test_positive_flow_88(self):
        self.change_maker = ChangeMaker(88, self.coins)
        self.assertEqual(self.change_maker.make_change(), [1, 1, 1, 1, 1, 1])

    def test_positive_flow_176(self):
        self.change_maker = ChangeMaker(176, self.coins)
        self.assertEqual(self.change_maker.make_change(), [1, 0, 1, 0, 1, 3])

    def test_positive_flow_188(self):
        self.change_maker = ChangeMaker(188, self.coins)
        self.assertEqual(self.change_maker.make_change(), [1, 1, 1, 1, 1, 3])
