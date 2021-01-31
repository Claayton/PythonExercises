#Ex023.2
#Faça um programa que leia um numero de 0 a 9999, e mostre na tela cada um dos digitos separados

number = str(input('Enter a number: '))
unity = number[-1:] #Seleciona o ultimo numero da str
ten = number[-2:-1] #Selaciona o penltimo numero
hundred = number[-3:-2] #Seleciona o segundo numero numero
thousand = number[-4:-3] #Seleciona o primeiro numero
print(f'Unity: {unity}')
print(f'Ten: {ten}')
print(f'Hundred: {hundred}')
print(f'Thousand: {thousand}')
