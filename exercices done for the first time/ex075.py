# Ex 075
nove = 0
tres = 0
cont = 0
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
int(input('Digite mais um npumero: ')), int(input('Digite seu último número: ')))
print('Voce digitou os números: ', end=' ')
for n in numeros:
    print(f"\033[32m{n}\033[m", end=' ')
    cont += 1
    if n == 9:
        nove += 1
    if n == 3:
        tres = cont
print(f'\nO valor 9 apareceu \033[32m{nove}\033[m vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na \033[32m{tres}ª\033[m posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(f"\033[32m{n}\033[m", end=' ')
