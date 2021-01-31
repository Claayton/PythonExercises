#Ex027.2
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

name = str(input('Enter a name: ')).title().strip()
name = name.split()
print(f'Your first name is {name[0]}')
print(f'And your last name is {name[-1]}')
print(f'Nice to meet you {name[0]}')
