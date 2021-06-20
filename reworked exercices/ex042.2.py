# Ex042.2
"""Redo the challenge 035 of the triangles, adding the ability to show what type of triangle will be formed:
Equilateral: all sides equals,
Isosceles: two equal sides,
Scalene: all different sides"""

print('=-' * 15)
print(f'{"TRIANGLE ANALYZING":-^30}')
print('=-' * 15)
first = float(input('First segment: '))
second = float(input('Second segment: '))
third = float(input('third segment: '))
list = [first, second, third]
list = sorted(list)
if list[0] + list[1] > list[2]:
    print('The above segments CAN form a triangle')
    if first == second and second == third:
        print('Equilateral triangle')
    elif first == second or first == third or second == third:
        print('Isosceles triangle')
    elif first != second and first != third and second != third:
        print('Scalene triangle')
else:
    print('The above segments CANNOT form a triangle')
