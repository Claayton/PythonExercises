# Ex045.2
"""Create a program that makes the computer play JOKENPÔ with you"""

from random import choice
from time import sleep
print('_-_' * 10)
print(f'{"JOKENPÔ":-^30}')
print('_-_' * 10)
print("""Your options:
[ 1 ] - STONE
[ 2 ] - PAPER
[ 3 ] - SCISSOR""")
possibilities = [1, 2, 3]
choice_p1 = int(input('Make your choice: '))
choice_pc = choice(possibilities)
if choice_pc == choice_p1:
    result = 'TIE, TRY AGAIN'
elif choice_pc == 1 and choice_p1 == 2 or choice_pc == 2 and choice_p1 == 3 or choice_pc == 3 and choice_p1 == 1:
    result = 'VICTORY, CONGRATULATIONS'
else:
    result = 'DEFEAT, TRY AGAIN'
possibilities = ['STONE', 'PAPER', 'SCISSOR']
print('...........JO', end=''), sleep(0.5), print('KEN', end=''), sleep(0.5), print('PÔ............')
print(f'You have chosen {possibilities[choice_p1 - 1]}\nAnd the computer chose {possibilities[choice_pc - 1]}')
print(result)
print('...' * 10)
