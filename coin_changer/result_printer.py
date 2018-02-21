# -*- coding: utf-8 -*-
"""This module represents result printer.

"""


class ResultPrinter(object):
    """The result printer will print a list of number that indicates
       the quantity of each coin value needed to sum to a target amount.

    Attributes:
        coins_set: the available coins.
        change:

    """

    def __init__(self, coins, change):
        self.coins = coins
        self.change = change

    def __validate_change(self):
        """return if chagne is valid to print

        """
        if len([value for value in self.change if value == 0]) == len(self.coins):
            print('No change needed.')
            return False
        elif len([value for value in self.change if value < 0]) > 0:
            print('Quantity of coins must be positive.')
            return False
        else:
            return True
    
    def print_result(self):
        """return the formatted result (a dictionary)

        """
        if self.__validate_change() is False:
            return None
            

        change_dict = dict(zip(self.coins[::-1], self.change[::-1]))
        formatted_result = {print(str(value) + ' * ' + str(key) + ' cent coin')
                            for key, value in change_dict.items() if value > 0}
        return formatted_result
