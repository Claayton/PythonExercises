#Ex018.2
"""Make a program that reads any angle, and shows on the screen the value of cine, cosine and tangent fo that angle"""

from math import sin, cos, tan, radians
angle = float(input('Type an angle you want: '))
angle_rad = radians(angle)
sin = sin(angle_rad)
cos = cos(angle_rad)
tan = tan(angle_rad)
print(f'The angle of {angle:.1f} has SINE of {sin:.2f}')
print(f'The angle of {angle:.1f} has COSINE of {cos:.2f}')
print(f'The angle of {angle:.1f} has TANGENT of {tan:.2f}')
