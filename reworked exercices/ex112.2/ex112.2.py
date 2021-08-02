# Ex112.2
"""Within the utilitiesCeV package that we created in challenge 111, we have a module called data.
Create a function called readmoney() that is capable of working like the input() function, but with a data validation to only accept values that are monetary."""

from utilitiescev import currency, data

print("\033[34m==\033[m" * 21)
price = data.readmoney('Enter a price: ')
currency.summary(price, 80, 35)
print("\033[34m==\033[m" * 21)
print('xD')
