#Exercício017
import math
op = float(input('Qual o comprimento do cateto oposto do triângulo retângulo? '))
ad = float(input('Qual o comprimento do cateto adjascente do triângulo retângulo? '))
hip = (pow(op, 2) + pow(ad, 2))**(1/2)
print('Se o comprimento do cateto oporto é {},\nE o cumprimento do cateto adjascente é {},'.format(op, ad))
print('O comprimeito da hipotenusa é {:.2f}.'.format(hip))
print('xD')
