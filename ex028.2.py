#Ex028.2
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5,
#E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador,
#O programa deverá escrever na tela se o usuário venceu ou perdeu a partida.

from random import randint
from time import sleep

print('\033[31m=-'*22)
print('\033[32mTENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO! ')
print('\033[31m=-'*22)
pc_number = randint(0, 5)
usu_number = int(input('\033[32mENTRE O E 5, EM QUAL NÚMERO PENSEI?:\033[m '))
print('\033[35mPROCESSANDO...')
sleep(1)
if pc_number == usu_number:
    print(f'\033[32mACERTOU! eu realmente pensei no múmero\033[m {usu_number}')
else:
    print(f'\033[31mERROU! o número que eu pensei foi\033[m {pc_number}, \033[31mE NÃO \033[m{usu_number}')
