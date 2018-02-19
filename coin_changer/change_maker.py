# -*- coding: utf-8 -*-
"""This module represents change maker.

"""


class ChangeMaker(object):
    """For a given target amount, the change maker will produce a combination
       of coins that sum to the target amount based on what is avialable in
       coin set.

    Attributes:
        target_amount: the amount that needs to make change.
        coins: a list of coins values.
    """

    def __init__(self, target_amount, coins):
        self.target_amount = target_amount
        self.coins = coins

    def make_change(self):
        """return a list that indicates the required number of each value of coins

        """
        
        return 'This is changes'
