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
        
        if self.target_amount < 0:
            return 'Target amount must be positive.'
            
        # assign 'inf' to all cells to make sure they are greater than i
        # min_combos[i] is smallest set of coins to target i.
        min_combos = [0] + [float('inf')] * self.target_amount

        # to memorise the all previous best combos, a table is used to record
        # the result.
        # combos[i][j] is the number of coins for coin value j to target i
        combos = [[0] * len(self.coins)] * (self.target_amount + 1)

        # start from 1 as 0 is already solved
        for i in range(1, self.target_amount + 1):
            for j, coin in enumerate(self.coins):
                if coin > i:
                    break
                last = i - coin
                combo = combos[last]
                if (min_combos[i] > min_combos[last] + 1):
                    min_combos[i] = min_combos[last] + 1
                    current_combo = list(combo)
                    current_combo[j] += 1
                    combos[i] = current_combo

        return combos[self.target_amount]
