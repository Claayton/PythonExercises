# Ex078.2
"""Make a program that reads 5 numerical values and stores them in a list.
At the end show, which was the highest and lowest value entered and their respective positions in the list."""

values = []

for p in range(0, 5):
    values.append(int(input(f'Enter a value for the position {p + 1}: ')))

print(f'You entered the values: ', end='')
max_positions = []
min_positions = []
cont = 0
for v in values:
    print(f'\033[32m{v}\033[m', end=' ')
    if v == max(values):
        max_positions.append(cont)
    if v == min(values):
        min_positions.append(cont)
    cont += 1
print()
print(f'The highest values entered was the \033[32m{max(values)}\033[m, in position (s) ', end='')
for v in max_positions:
    print(f'\033[32m{v}\033[m', end='...')
print()
print(f'The lowest values entered was the {min(values)}, in positions ', end='')
for v in min_positions:
    print(f'\033[32m{v}\033[m', end='...')
print()
print('\033[32mxD\033[m')
