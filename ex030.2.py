# Ex030.2
"""Create a program that reads a integer and shows on the screen whether it is ODD or EVEN"""

number = int(input('Type a number: '))
if number % 2 == 0:
    print(f'It is numebr is {number}, and it is: \033[32mEVEN\033[m')
else:
    print(f'Is is number is {number}, and it is: \033[32mODD\033[m')
