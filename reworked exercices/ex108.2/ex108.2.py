# Ex108.2
"""Adapt the code from challenge 107 by creating an additional function called currency() that can display the values as a formatted currency value."""

import currency

print("\033[34m==\033[m" * 20)
price = float(input('Enter a price: '))
print(f'\033[31mThe half of \033[32m{currency.currency(price)}\033[31m is \033[32m{currency.currency(currency.half(price))}\033[m')
print(f'\033[33mThe double of \033[32m{currency.currency(price)}\033[33m is \033[32m{currency.currency(currency.double(price))}\033[m')
print(f'\033[34mIncrease 10% we have \033[32m{currency.currency(currency.increase(price, 10))}\033[m')
print(f'\033[35mDecreasing 10% we have \033[32m{currency.currency(currency.decrease(price, 10))}\033[m')
print("\033[34m==\033[m" * 20)
print('xD')
