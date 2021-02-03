#Ex032.2
#Faça um programa que leia um ano qualquer, e mostre se ele é ou não BISSEXTO.

from datetime import date
year = int(input('What year do you want to analyze? \nType "0" for the current year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a LEAP YEAR')
else:
    print(f'{year} is not a LEAP YEAR')
