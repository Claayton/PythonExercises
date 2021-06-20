# Ex016.2
"""Create a program that reads any real number from the keyboard, and shows its entire portion on the screen"""

from math import trunc
value = float(input('Enter a value: '))
print(f'The value entered is {value}, end its entire portion is {trunc(value)}')
