#Ex025.2
#Crie um programa que leia o nome de uma pessoa, e diga se ela tem 'SILVA' no nome

name = str(input('Enter a name: ')).strip().upper()
print(f'There is "Silva" in that name?: {"SILVA" in name}')
