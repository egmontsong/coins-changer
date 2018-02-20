# -*- coding: utf-8 -*-
"""This is main module which conducts the whole process of payslip generation.

"""


from change_maker import ChangeMaker
from coins_reader import CoinsReader
from result_printer import ResultPrinter
import config as config

def main():
    """1. Capture input target amount
       2. Read coins set from coins
       3. make change to a target amount
       4. Output a list of requied coins and their quantities.

    """

    target_amount = int(input("Enter your change in cents:\n"))

    # read coins
    coins_reader = CoinsReader(config.SETTING_DIR + '/coin_set.json')
    coins = coins_reader.get_coin_set()

    # make change to a target amount
    change_maker = ChangeMaker(target_amount, coins)
    change = change_maker.make_change()

    # print formatted result
    result_printer = ResultPrinter(coins, change)
    result_printer.print_result()


if __name__ == '__main__':
    main()
