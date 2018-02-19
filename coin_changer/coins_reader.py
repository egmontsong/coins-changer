# -*- coding: utf-8 -*-
"""This module represents coins reader.

"""

import json


class CoinsReader(object):
    """The coins reader read coin set from json file.

    Attributes:
        file_path: file path to the coin set config file.
        coins: the list of available coins.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.coins = self.__read_coin_set()

    def get_coin_set(self):
        """Return coins set

        """
        return self.coins

    def __read_coin_set(self):
        """Return a list of coins that represents the available value of coins

        Arguments:
            file_path: the path to a json file.
        """

        coins = []

        try:
            with open(, 'rb') as coins_set_file:
                coins = json.load(coins_set_file)['coin_set']
            tax_rate_file.close()
            return coins

        except IOError as e:
            print e.errno, e.strerror
            return None


