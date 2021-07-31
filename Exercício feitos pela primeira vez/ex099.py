# Ex099
from time import sleep


def maior(* num):
    print('=' * 36)
    print('Analisando valores', end='   ')
    print('\033[31mO ', end='', flush=True), sleep(0.5),
    print('\033[32mO ', end='', flush=True), sleep(0.5),
    print('\033[33mO ', end='', flush=True), sleep(0.5),
    print('\033[34mO ', end='', flush=True), sleep(0.5),
    print('\033[35mO ', end='', flush=True), sleep(0.5),
    print('\033[36mO ', end='', flush=True), sleep(0.5),
    print('\033[37mO ', end='', flush=True), print('\033[m')

    maior = 0
    cont = 0
    for c in num:
        if cont == 0:
            maior = c
        if c > maior:
            maior = c
        cont += 1
        print(c, end='\033[32m > \033[m')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('=' * 36)
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
