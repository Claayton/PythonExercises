# Ex005.2
"""Make a program that reads a whole number, and shows your successor and predecessor on the screen"""

number = int(input('Type a number: '))
predecessor = number - 1
successor = number + 1
print('Analyzing the value')
print(f'His predecessor is {predecessor}, and')
print(f'His successor is {successor}.')
