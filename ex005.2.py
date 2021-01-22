#Ex005.2
#Faça um programa que leia um número inteiro, e mostre na tela seu sucessor e seu antecessor.

number = int(input('Type a number: '))
predecessor = number - 1
successor = number + 1
print('Analyzing the value')
print(f'His predecessor is {predecessor}, and')
print(f'His successor is {successor}.')
