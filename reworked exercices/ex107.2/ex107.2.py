# Ex107.2
"""Create a module called currency.py that has built-in functions increase(), decrease(), double(), half().
Also make a program that imports this module and uses some of these functions."""

import currency

print("\033[34m==\033[m" * 20)
price = float(input('Enter a price: '))
print(f'\033[31mThe half of \033[32m{price:.2f}\033[31m is \033[32m{currency.half(price):.2f}\033[m')
print(f'\033[33mThe double of \033[32m{price:.2f}\033[33m is \033[32m{currency.double(price):.2f}\033[m')
print(f'\033[34mIncrease 10% we have \033[32m{currency.increase(price, 10):.2f}\033[m')
print(f'\033[35mDecreasing 10% we have \033[32m{currency.decrease(price, 10):.2f}\033[m')
print("\033[34m==\033[m" * 20)
print('xD')
