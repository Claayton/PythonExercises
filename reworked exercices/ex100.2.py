# Ex100.2
"""Make a program that has a list called numbers and two functions called draw() and even_sum.
The first function will draw 5 numbers and place them into the list and the second function will show the sum of all PAIR values draw by the previous function."""

numbers = []

def draw(list):
    from random import randint
    from time import sleep
    print('\033[32mDrawin 5 values from the list:\033[31m', end=' ')
    for c in range(0, 5):
        number = randint(0, 9)
        print(number, end=', ', flush=True)
        sleep(0.5)
        list.append(number)
    print('\033[32mPronto!\033[m')
        

def even_sum(list):
    print(f'\033[32mAdding the even values of: \033[31m{list}\033[32m, we have: \033[31m', end='')
    sum = 0
    for c in list:
        if c % 2 == 0:
            sum += c
    print(f'{sum}.\033[m')

draw(numbers)
even_sum(numbers)
print('xD')