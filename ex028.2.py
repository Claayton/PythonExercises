#Ex028.2
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5,
#E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador,
#O programa deverá escrever na tela se o usuário venceu ou perdeu a partida.

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
