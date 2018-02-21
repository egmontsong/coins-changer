# -*- coding: utf-8 -*-
"""This module tests change maker.
"""

from unittest import TestCase
import coin_changer.config as config
from coin_changer.coins_reader import CoinsReader


class TestCoinsReader(TestCase):
    """Test coins reader

    """

    def test_negative_set(self):
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/coin_set_neg.json')
        self.assertEqual(self.coins_reader.get_coin_set(),
                         'Coin must be positive value.')

    def test_positive_set(self):
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/coin_set.json')
        self.assertEqual(self.coins_reader.get_coin_set(),
                         [1, 2, 5, 10, 20, 50])

    def test_negative_file_not_exist(self):
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/not_exist.json')
        self.assertEqual(self.coins_reader.get_coin_set(),
                         'No such file or directory')
