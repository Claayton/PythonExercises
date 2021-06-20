#Exercício033
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
if num1 < num2 and num1 < num3:
  menor = num1
if num2 < num1 and num2 < num3:
  menor = num2
if num3 < num1 and num3 < num2:
  menor = num3
print('O menor número é {}'.format(menor))
if num1 > num2 and num1 > num2:
  maior = num1
if num2 > num1 and num2 > num3:
  maior = num2
if num3 > num1 and num3 > num2:
  maior = num3
print('O maior número é {}'.format(maior))
print('xD')
