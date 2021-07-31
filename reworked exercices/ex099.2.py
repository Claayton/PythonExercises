# Ex099.2
"""Make a program that has a function called larger(), which takes several integer-valued parameters.
your program has to analyze all the highlights and say which one is the biggest."""

from time import sleep

def highest(*values):
    print('\033[35m--\033[m' * 25)
    print('\033[34mAnalyzing past values\033[m')
    highest = 0
    cont = 0
    for c in values:
        if cont == 0:
            highest = c
        if c > highest:
            highest = c
        cont += 1
    print(f'{len(values)} values were passed in total')
    print(f'The highest value informed was {highest}')
    print('\033[35m--\033[m' * 25)
    sleep(1)

highest(2, 9, 4, 5, 7, 1)
highest(4, 7, 0)
highest(1, 2)
highest(6)
highest()
