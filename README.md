# coins-changer
[![Build Status](https://travis-ci.org/egmontsong/coin-change.svg?branch=master)](https://travis-ci.org/egmontsong/coin-change)
Coins changer based on dynamic programming algorithm

## Problem
We need a simple program which can tell us what change we need to give
to a customer in our shop. Our program will only handle coins that are 50, 20,
10, 5, 2 and 1 cents in value. For example, if we input 24 cents into our
program, it will tell us that we can use 1 * 20 cent coin and 2 * 2 cent coins
to return the correct amount of change.

The program should accept user input on the command line, print the results to
the screen and then immediately exit. Here is an example of what the program
input and output should look like:

> Enter your change in cents:
> 24
> 1 * 20 cent coin
> 2 * 2 cent coins

Another example:

> Enter your change in cents
> 88
> 1 * 50 cent coin
> 1 * 20 cent coin
> 1 * 10 cent coin
> 1 * 5 cent coin
> 1 * 2 cent coin
> 1 * 1 cent coin