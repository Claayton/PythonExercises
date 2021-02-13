# Ex045.2
"""Create a program that makes the computer play JOKENPÔ with you"""

from random import choice
from time import sleep
print(f'\033[7:30:44m{"JOKENPÔ":-^30}\033[m')
print(f"""Your options:
\033[7:30:44m{'[ 1 ] - STONE':<30}\033[m
\033[7:30:44m{'[ 2 ] - PAPER':<30}\033[m
\033[7:30:44m{'[ 3 ] - SCISSOR':<30}\033[m""")
possibilities = [1, 2, 3]
choice_p1 = int(input('Make your choice: '))
choice_pc = choice(possibilities)
if choice_pc == choice_p1:
    result = '\033[33mTIE, TRY AGAIN\033[m'
elif choice_pc == 1 and choice_p1 == 2 or choice_pc == 2 and choice_p1 == 3 or choice_pc == 3 and choice_p1 == 1:
    result = '\033[32mVICTORY, CONGRATULATIONS!\033[m'
else:
    result = '\033[31mDEFEAT, TRY AGAIN!\033[m'
possibilities = ['STONE', 'PAPER', 'SCISSOR']
print('\033[7:30:44m...........JO\033[m', end=''), sleep(0.5)
print('\033[7:30:44mKEN\033[m', end=''), sleep(0.5)
print('\033[7:30:44mPÔ............\033[m')
print(f'You have chosen \033[34m{possibilities[choice_p1 - 1]}\033[m')
print(f'And the computer chose \033[34m{possibilities[choice_pc - 1]}\033[m')
print(result)
print('\033[7:30:44m...\033[m' * 10)
