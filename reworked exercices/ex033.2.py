# Ex033.2
"""Make a program that reads three numbers, and shows on the screen which is the largest and which is the smallest"""

number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))
number3 = int(input('Enter your third number: '))
bigger = number1
smaller = number1
if number2 > number1:
    bigger = number2
if number3 > number1 and number3 > number2:
    bigger = number3
print(f'The bigger number is {bigger}')
if number2 < number1:
    smaller = number2
if number3 < number1 and number3 < number2:
    smaller = number3
print(f'the smaller number is {smaller}')
