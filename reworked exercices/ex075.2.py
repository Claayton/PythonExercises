# Ex075.2
"""Develop a program that reads four values from the keyboard.
At the end show:
A - How many times did the value p appear
B - in what position was the first value 3 typed
C - What were the even numbers."""

numbers = (
    int(input('Enter a number: ')),
    int(input('Enter other number: ')),
    int(input('Type one more number: ')),
    int(input('Enter your last number: '))
    )

print(f'You typed the numbers:', end=' ')
for n in numbers:
    print(f'\033[32m{n}\033[m', end=' ')
print()
print(f'The value 9 appered \033[32m{numbers.count(9)}\033[m times')
if 3 in numbers:
    print(f'The value 3 appered in the \033[32m{numbers.index(3) + 1}°\033[m position')
else:
    print('The number 3 was not entered')
print(f'The even values entered were: ', end='')
for e in numbers:
    if e % 2 == 0:
        print(f'\033[32m{e}\033[m', end=' ')
print()
print('\033[32mxD\033[m')
