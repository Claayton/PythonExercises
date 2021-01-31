#Ex024.2
#Crie um programa que leia o nome de uma cidade, e diga se ela começa ou nao com o nome 'SANTO'

city = str(input('Enter the name of a city: ')).strip().upper()
print('This city starts with "Santo"?: ', end='')
print(city[0:5] == "SANTO")
