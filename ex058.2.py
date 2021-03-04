# Ex058.2
"""Improve de game of challenge 028.2, where the computer will 'think' of a number from 0 to 10.
But now the player falls trying to add until he gets it right, showing in the end how many guesses it took to win"""

from random import randint
from time import sleep

cont = 1
result = ''

print('\033[31m=-'*28)
print('\033[32mBETWEEN 0 AND 10, TRY TO GUESS THE NUMBER I AM THINKING! ')
print('\033[31m=-\033[m'*28)
pc_number = randint(0, 10)
while result != 'Win':
    usu_number = int(input('WHICH NUMBER I THOUGHT?: '))
    print('\033[35mPROCESSING...\033[m')
    sleep(1)
    if pc_number == usu_number:
        result = 'Win'
    else:
        cont += 1
    if pc_number > usu_number:
        print('\033[35mA little more\033[m')
    elif pc_number < usu_number:
        print('\033[35mA little less\033[m')
print(f'You \033[32mWON\033[m after {cont} attempts')
