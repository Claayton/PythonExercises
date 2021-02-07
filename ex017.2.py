#Ex017.2
"""Make a program that reads the length of the opposite leg and the adjacent leg of a right triangle,
calculate and show the length of the hypo"""

from math import hypot
opposite = float(input('What is the length of the opposite side?: '))
adjacent = float(input('What is the length of the adjacent side?: '))
hypotenuse = hypot(opposite, adjacent)
print(f'The length of the hypotenuse is {hypotenuse:.2f}')
