#Ex011.2
#Faça um programa que leia a largura e a altura de uma parede,
#Calcule sua área e a qtdade necessária de tinta para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
width = float(input('How wide is the wall?: '))
height = float(input('How tall is the wall?: '))
area = width * height
paint = area / 2
print(f'The area this wall is {area}m²')
print(f'If each liter of paint paints 2m² of wall, to paints this wall it will be need {paint} liters of paint')
