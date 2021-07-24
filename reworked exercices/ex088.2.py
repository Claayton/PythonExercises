# Ex088.2
"""Make a program that helps a MEGA-SENA player to create guesses.
The program will ask how many games will be genereted and will draw 6 numbers between 1 and 60 for each game, registering everything in a list."""

from time import sleep
from random import randint
all_games = []
each_game = []
number = 0

print('\033[35m=\033[m' * 50)
print(f'\033[31m{"LETS PLAY AT MEGA-SENA":^50}')
print('\033[35m=\033[m' * 50)

games = int(input('\033[32mHow many games do you want me to draw?: \033[m'))
print(f'\033[32mI AM DRAWING {games} GAMES FOR YOU\033[m')
for c in range(0, games):
    while len(each_game) < 6:
        number = randint(1, 60)
        if number not in each_game:
            each_game.append(number)
    all_games.append(each_game[:])
    each_game.clear()

cont = 0 
for each in all_games:
    cont += 1
    print(f'\033[34mGame {cont:_<20}\033[m', end='')
    print(f'\033[35m{each}\033[m')
    sleep(0.5)
print('\033[35m=\033[m' * 50)
print(f'\033[31m{"GOOD LUCK":^50}\033[m')
print('\033[35m=\033[m' * 50)
print('\033[31mxD\033[m')
