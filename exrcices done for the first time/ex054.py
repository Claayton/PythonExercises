#Exercício055
from datetime import date
atual = date.today().year
soma = 0
for c in range(1, 7 + 1):
  year = int(input('Qual o ano de nascimento da {}° pessoa?: '.format(c)))
  if year + 21 <= atual:
    soma += 1
print('Dessas  7 pessoas {} já são maiores de idade'.format(soma))
print('E {} ainda são menores de idade'.format(7 - soma))
print('xD')
