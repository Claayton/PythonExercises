#Ex016.2
#Crie um programa que leia um número real qualquer pelo teclado, e mostre na tela sua porção inteira.

from math import trunc
value = float(input('Enter a value: '))
print(f'The value entered is {value}, end its entire portion is {trunc(value)}')
