# Ex035.2
"""Develop a program that reads the length of three lines, and tell the user whether or not they can form a triangle"""

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
else:
    print('The above segments CANNOT form a triangle')
