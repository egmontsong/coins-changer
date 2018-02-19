# -*- coding: utf-8 -*-
"""This is main module which conducts the whole process of payslip generation.

"""


from change_maker import ChangeMaker

def main():
    """1. Read coins set from coins
       2. make change to a target amount
       3. Output a list of requied coins and their quantities.

    """

    target_amount = 24

    # read coins
    coins = [1, 2, 5, 10, 20, 50]

    # make change to a target amount
    change_maker = ChangeMaker(target_amount, coins)
    print(change_maker.make_change())


if __name__ == '__main__':
    main()
