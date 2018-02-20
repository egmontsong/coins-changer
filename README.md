# money-changer
[![Build Status](https://travis-ci.org/egmontsong/coins-changer.svg?branch=master)](https://travis-ci.org/egmontsong/coins-changer)
[![codecov](https://codecov.io/gh/egmontsong/coins-changer/branch/master/graph/badge.svg)](https://codecov.io/gh/egmontsong/coins-changer)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bdcbe53edebf44baa6b1b8602ac1833a)](https://www.codacy.com/app/egmontsong/coins-changer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=egmontsong/coins-changer&amp;utm_campaign=Badge_Grade)
[![codebeat badge](https://codebeat.co/badges/75096f68-25ac-402d-b1ed-fbe2fb201275)](https://codebeat.co/projects/github-com-egmontsong-coins-changer-master)


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

## Features
* CI integration with Travis.
* Follows PEP8 code style and Google Docstrings style for Python.

## How to use it
### Install dependencies
```bash
# Use virtualenv (recommended)
pip install virtualenv
virtualenv venv --python=python3.6
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run with command line
```bash
# in root 
python coin_changer/main.py  # run with main
```

## Run Tests
### Run all tests
```bash
nose2
nose2 --with-coverage                          # with coverage report
nose2 --with-coverage --coverage ./coin_changer  # only show coverage to main package
coverage report -m                             # with missing lines no. indicated
```

## Tools
### [Nose2](https://github.com/nose-devs/nose2)
The successor to nose, based on unittest2.


### [Pipreqs](https://github.com/bndr/pipreqs)
Generate requirements.txt file for any project based on imports.
```bash
pipreqs ./ 
# generate requirements.txt based on all files in current directory.
```
