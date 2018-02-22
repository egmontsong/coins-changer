# -*- coding: utf-8 -*-
"""This module tests change maker.
"""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import changer.config as config
from changer.coins_reader import CoinsReader


class TestCoinsReader(TestCase):
    """Test coins reader

    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_set(self, mock_stdout):
        """when coins set has negative value
           program should print 'Coin must be positive value.'
        """
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/coin_set_neg.json')
        self.coins_reader.get_coin_set()
        self.assertEqual(
                mock_stdout.getvalue(),
                'Coin must be positive value.\n')

    def test_positive_set(self):
        """when coins set is [1, 2, 5, 10, 20, 50]
           program should return [1, 2, 5, 10, 20, 50]
        """
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/coin_set.json')
        self.assertEqual(self.coins_reader.get_coin_set(),
                         [1, 2, 5, 10, 20, 50])

    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_file_not_exist(self, mock_stdout):
        """when coins set file is not exist
           program should print 'No such file or directory'
        """
        self.coins_reader = CoinsReader(config.SETTING_DIR + '/not_exist.json')
        self.coins_reader.get_coin_set()
        self.assertEqual(
                mock_stdout.getvalue(),
                'No such file or directory\n')
