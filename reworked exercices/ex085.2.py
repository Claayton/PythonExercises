# Ex085.2
"""Create a program where the user can enter seven numeric vlaues and enter them in a simgle list that keeps the odd and even vlaues separete.
At the end, show the odd and even values in ascending order."""

values = [[], []]

print('\033[31m=\033[m'* 50)
for n in range(0, 7):
    number = int(input(f'\033[35mEnter a {n + 1}° number: \033[m'))
    if number % 2 == 0:
        values[1].append(number)
    else:
        values[0].append(number)
print('\033[31m=\033[m'* 50)
print(f'\033[35mThe ODD numbers in ascending order are: \033[32m{sorted(values[1])}\033[m')
print(f'\033[35mThe EVEN numbers in ascending order are: \033[32m{sorted(values[0])}\033[m')
print('\033[31m=\033[m'* 50)
print('\033[35mxD\033[m')
