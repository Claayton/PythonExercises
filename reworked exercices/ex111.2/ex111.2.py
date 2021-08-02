# Ex111.2
"""Create a package called utilitiesCeV that has two built-in modules called currency and data.
Transfer all the functions used in challenges 107, 108, 109 to the first package and keep every running."""

from utilitiescev import currency

print("\033[34m==\033[m" * 21)
price = float(input('Enter a price: '))
currency.summary(price, 80, 35)
print("\033[34m==\033[m" * 21)
print('xD')
