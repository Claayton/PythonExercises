# Ex081.2
"""Create a program that will read multiple numbers and put them in a list.
After that, show:
A - How many numbers were figured.
B - The list of values, ordered in descending order.
C - If valor 5 is entered and is or in not in the list."""

values = []
again = 'N'

print('-' * 40)
while True:
    number = int(input('Enter a number: '))
    values.append(number)
    while again != 'S' or again != 'N':
        again = str(input('Do you want to continue? [S/N]: ')).upper()
        if again  == 'S' or again == 'N':
            break
        print('\033[33mINVALID COMMAND, TRY AGAIN!\033[m')
    if again == 'N':
        break
print('-' * 40)
print(f'You typed {len(values)} elements.')
values.sort(reverse=True)
print(f'The values in descending order are {values}.')
if 5 in values:
    print('The value 5 is on the list.')
else:
    print('The value 5 is not on the list.')
print('xD')
