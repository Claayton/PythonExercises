# Ex109.2
"""Modify the function created in challenge 107 so that they accept one more parameter, informing wheter or not the value returned by them will be the currency() function, developed in challenge 108."""

import currency

print("\033[34m==\033[m" * 20)
price = float(input('Enter a price: '))
print(f'\033[31mThe half of \033[32m{currency.currency(price)}\033[31m is \033[32m{(currency.half(price, True))}\033[m')
print(f'\033[33mThe double of \033[32m{currency.currency(price)}\033[33m is \033[32m{currency.double(price, True)}\033[m')
print(f'\033[34mIncrease 10% we have \033[32m{currency.increase(price, 10, True)}\033[m')
print(f'\033[35mDecreasing 10% we have \033[32m{currency.decrease(price, 10, True)}\033[m')
print("\033[34m==\033[m" * 20)
print('xD')
