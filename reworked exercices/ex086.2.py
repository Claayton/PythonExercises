# Ex086.2
"""Create a program that creates a 3x3 dimensional matrix and fills it with read by keyboard.
At the end, show the matrix on the screen, with the correct formatting."""

matrix = [[[], [], []],
          [[], [], []],
          [[], [], []]]
cont = 0
cont2 = 0

print('\033[31m=\033[m' * 50)
for c in range(0, 9):
    number = int(input(f'\033[34mEnter a value for [{cont} : {cont2}]: \033[m'))
    matrix[cont][cont2].append(number)
    cont2 += 1
    if c + 1 == 3 or c + 1 == 6 or c + 1 == 9:
        cont += 1
        cont2 =0
print('\033[31m=\033[m' * 50)
for l in matrix:
    for c in l:
        for m in c:
            print(f'\033[35m[{m:^5}]\033[m', end='')
    print()
print('\033[31m=\033[m' * 50)
print('\033[34mxD\033[m')
