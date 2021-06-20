# Ex038.2
"""Write a program that reads two whole numbers and compare them showing the message on the screen
The first value is higher
The second value is higher
There is no higher value, the two are equal"""

number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if number1 == number2:
    print('There is no higher value, the two numbers are equal!')
elif number1 > number2:
    print('The fist number is higher!')
elif number2 > number1:
    print('The second number is higher!')
