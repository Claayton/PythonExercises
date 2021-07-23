# Ex087.2
"""Improve the previous challenge, showing at the end:
A - The sum of all values entered.
B - The sum of the values in the third column.
C - The highest value in the second row."""

matrix = [[[], [], []],
          [[], [], []],
          [[], [], []]]
cont = 0
cont2 = 0
total_sum = 0
third_column_sum = 0
second_row_highest = 0

print('\033[31m=\033[m' * 50)
for c in range(0, 9):
    number = int(input(f'\033[34mEnter a value for [{cont} : {cont2}]: \033[m'))
    matrix[cont][cont2].append(number)
    if number % 2 == 0:
        total_sum += number
    cont2 += 1
    if c + 1 == 3 or c + 1 == 6 or c + 1 == 9:
        cont += 1
        cont2 =0
        third_column_sum += number
print('\033[31m=\033[m' * 50)
cont3 = 0
for l in matrix:
    cont3 +=1
    for c in l:
        for m in c:
            print(f'\033[35m[{m:^5}]\033[m', end='')
            if cont3 == 2:
                if m > second_row_highest:
                    second_row_highest = m
    print()
print('\033[31m=\033[m' * 50)
print(f'\033[34mThe sum of the even values entered is: \033[32m{total_sum}.\033[m')
print(f'\033[34mThe sum of the values in the third column is: \033[32m{third_column_sum}.\033[m')
print(f'\033[34mThe Highest valuee in the second row is: \033[32m{second_row_highest}.\033[m')
print('\033[35mxD\033[m')
