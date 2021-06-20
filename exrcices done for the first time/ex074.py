# Ex074
# Ex 074
from random import randint
numeros = randint(0, 9) ,randint(0, 9) ,randint(0, 9), randint(0, 9), randint(0, 9)
cont = 0
print(f'Os números sorteados são: ')
for sorteio in numeros:
    cont += 1
    print(sorteio, end=' ')
    if cont == 1:
        maior = sorteio
        menor = sorteio
    if sorteio > maior:
        maior = sorteio
    if sorteio < menor:
        menor = sorteio
print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')
