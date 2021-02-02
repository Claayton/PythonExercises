#Ex030.2
#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

number = int(input('Type a number: '))
if number % 2 == 0:
    print(f'It is numebr is {number}, and it is: \033[32mPAIR\033[m')
else:
    print(f'Is is number is {number}, and it is: \033[32mODD\033[m')
