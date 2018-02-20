# -*- coding: utf-8 -*-
"""This module tests change maker.
"""

import unittest
from coin_changer.change_maker import ChangeMaker


class TestChangeMaker(unittest.TestCase):
    """Test change maker

    """

    def setUp(self):
        self.coins = [1, 2, 5, 10, 20, 50]

    def test_negative_flow(self):
        self.change_maker = ChangeMaker(-1, self.coins)
        self.assertEqual(self.change_maker.make_change(),
                         'Target amount must be positive.')

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
