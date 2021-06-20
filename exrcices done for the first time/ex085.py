# Ex085
values = [[], []]
for v in range(0, 7):
    num = int(input(f'Digite seu {v + 1}° número: '))
    if num % 2 == 0:
        values[0].append(num)
    else:
        values[1].append(num)
print(f'Os valores pares digitados foram: \033[32m{sorted(values[0])}\033[m')
print(f'Os valores ímpares digitados foram: \033[32m{sorted(values[1])}\033[m')
