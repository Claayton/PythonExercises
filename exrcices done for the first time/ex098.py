# Ex098
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo += 1
    if inicio > fim:
        fim -= 2
        if passo > 0:
            passo *= - 1
    for j in range(inicio, fim + 1, passo):
        print(j, end=' \033[32m>\033[m ')
        sleep(0.3)
    print()
    print('=' * 40)


print('=' * 40)
print('Contagem de 1 até 10, contando de 1 em 1: ')
contador(1, 10, 1)
print('Contagem de 10 até 0, contando de 2 em 2: ')
contador(10, 0, 2)
print('Escolha uma contagem personalizada: ')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
