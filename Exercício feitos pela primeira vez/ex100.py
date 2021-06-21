# Ex100
from random import randint
from time import sleep
numeros = []


def sorteia(lista):
    print('Sorteando os 5 valores', end=': ')
    for c in range(0, 5):
        lista.append(randint(0, 9))
    for v in lista:
        print(v, end=' \033[32m>\033[m ')
        sleep(0.3)
    print()


def soma_par(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de \033[32m{numeros}\033[m, temos: \033[32m{soma}\033[m.')


sorteia(numeros)
soma_par(numeros)
