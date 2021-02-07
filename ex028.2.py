# Ex028.2
"""Writes a program that makes the computer 'think' of an integer between 0 and 5
And ask the user to try to find out what number was chosen by the computer
The program should write on the screen if the user won or lost the game"""

from random import randint
from time import sleep

print('\033[31m=-'*22)
print('\033[32mTRY TO GUESS THE NUMBER I AM THINKING! ')
print('\033[31m=-'*22)
pc_number = randint(0, 5)
usu_number = int(input('\033[32mBETWEEN 0 AND 5, WHICH NUMBER I THOUGHT?:\033[m '))
print('\033[35mPROCESSING...')
sleep(1)
if pc_number == usu_number:
    print(f'\033[32mHIT! I really think about number\033[m {usu_number}')
else:
    print(f'\033[31mWRONG! the number I thought was \033[m {pc_number}, \033[31mand not \033[m{usu_number}')
