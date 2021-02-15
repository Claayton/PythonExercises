# Ex050.2
"""Develop a program that reads six integers and shows the sum only of those that are even,
If the value entered is odd, disregard it"""

sum = 0
for value in range(1, 7):
    number = int(input('Type a value: '))
    if number % 2 == 0:
        sum += number
print(f'The sum between 6 numbers informed is {sum}')
