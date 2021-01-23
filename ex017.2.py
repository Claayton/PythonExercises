#Ex017.2
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#Calcule e mostre o comprimento da hipótenusa

from math import hypot
opposite = float(input('What is the length of the opposite side?: '))
adjacent = float(input('What is the length of the adjacent side?: '))
hypotenuse = hypot(opposite, adjacent)
print(f'The length of the hypotenuse is {hypotenuse:.2f}')
