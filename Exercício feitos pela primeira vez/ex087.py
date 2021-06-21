# Ex087
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
print('Digite valores para um matriz 3x3:')
for m in range(0, 3):
    for n in range(0, 3):
        matriz[m][n].append(int(input(f'Digite um valor para [{m}, {n}]: ')))
print('-' * 25)
par = 0
soma_3 = 0
maior_2 = 0
cont = 0
coluna = 1
for m in range(0, 3):
    for l in matriz[m]:
        for c in l:
            print(f'[\033[31m{f"{c}":^5}\033[m]', end=' ')
            if c % 2 == 0:
                par += c
            if coluna == 3 or coluna == 6 or coluna == 9:
                soma_3 += c
            coluna += 1
            if m == 1:
                if cont == 0:
                    maior_2 = c
                    cont += 1
                if c > maior_2:
                    maior_2 = c
    print()
print('-' * 25)
print(f'A soma dos valores pares é \033[32m{par}\033[m')
print(f'A soma dos valores da terceira coluna é \033[32m{soma_3}\033[m')
print(f'O maior valor da segunda linha é \033[32m{maior_2}\033[m')
