# Ex082.2
"""Create a program that will read multiple numbers and put them in a list.
After that, create two extra lists that will contain only the even values and the odd vlaues you typed, respectively.
At the end, show the content of the generated lists."""

values = []
odd = []
even = []
again = 'S'

while True:
    number = int(input('\033[32mEnter a number: \033[m'))
    values.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    while again != 'S' or again != 'N':
        again = str(input('\033[32mDo you want to continue? [S/N]: \033[m')).upper()
        if again  == 'S' or again == 'N':
            break
        print('\033[33mINVALID COMMAND, TRY AGAIN!\033[m')
    if again == 'N':
        break
print('_' * 40)
print(f'\033[34mThe full list is \033[32m{values}\033[m')
print(f'\033[34mThe list of pairs is \033[32m{even}\033[m')
print(f'\033[34mThe list of odd is \033[32m{odd}\033[m')
print('\033[34mxD\033[m')
