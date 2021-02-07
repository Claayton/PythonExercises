#Ex011.2
"""Make a program that reads the width and height of a wall,
calculate your area and the required amount of paint to paint it,
knowing that each liter of paint paints an area of 2m²"""

width = float(input('How wide is the wall?: '))
height = float(input('How tall is the wall?: '))
area = width * height
paint = area / 2
print(f'The area this wall is {area}m²')
print(f'If each liter of paint paints 2m² of wall, to paints this wall it will be need {paint} liters of paint')
