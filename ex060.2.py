# Ex060.2
"""Make a program that reads any number and shows its factorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120."""

cont = 0
result = 1

print(f'{"FACTORIAL CALCULATION":^50}')
print('-' * 50)
factorial = int(input('Type a number to see its factorial: '))
while factorial > 0:
    cont += 1
    if cont == 1:
        print(f'\033[32m{factorial}!', end='\033[31m = \033[m')
    result *= factorial
    factorial -= 1
    print(factorial + 1, end='')
    print('\033[31m X \033[m' if factorial > 0 else '\033[31m = \033[m', end='')
print(f'\033[32m{result}\033[m')
