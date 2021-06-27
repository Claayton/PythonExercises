# Ex074.2
"""Create a program that will generate five random numbers and put them in a tuple. After that, show the generated number language and also indicate the largest and smallest values that are in the tuple."""

from random import randint

numbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('The values draw were: ', end='')
for n in numbers:
    print(f'\033[34m{n}\033[m', end=' ')
print()
print(f'The highest value draw was: \033[34m{max(numbers)}\033[m')
print(f'The lowest value  draw was: \033[34m{min(numbers)}\033[m')
print('\033[34mxD\033[m')
