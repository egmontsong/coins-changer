# -*- coding: utf-8 -*-
"""This module represents result printer.

"""


class ResultPrinter(object):
    """The result printer will produce a command line outpur for how
       many coins needed for a coin value to sum to the target.

    Attributes:
        coins_set: the available coins.
        change:

    """

    def __init__(self, coins_set, change):
        self.coins_set = coins_set
        self.change = change

    def print_result(self):
        """return the formatted result (a dictionary)

        """
        change_dict = dict(zip(self.coins_set[::-1], self.change[::-1]))
        {print(str(value) + ' * ' + str(key) + ' cent coin')
         for key, value in change_dict.items() if value > 0}
