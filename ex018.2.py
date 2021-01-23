#Ex019.2
#Faça um rpograma que leia um ângulo qualquer, e mostre na tela o valor de ceno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angle = float(input('Type an angle you want: '))
angle_rad = radians(angle)
sin = sin(angle_rad)
cos = cos(angle_rad)
tan = tan(angle_rad)
print(f'The angle of {angle:.1f} has SINE of {sin:.2f}')
print(f'The angle of {angle:.1f} has COSINE of {cos:.2f}')
print(f'The angle of {angle:.1f} has TANGENT of {tan:.2f}')
