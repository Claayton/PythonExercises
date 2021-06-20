# Ex086
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
print('Digite valores para um matriz 3x3:')
for m in range(0, 3):
    for n in range(0, 3):
        matriz[m][n].append(int(input(f'Digite um valor para [{m}, {n}]: ')))
print('-' * 25)
for m in range(0, 3):
    for l in matriz[m]:
        for c in l:
            print(f'[\033[31m{f"{c}":^5}\033[m]', end=' ')
    print('\n', end='')
print('-' * 25)
