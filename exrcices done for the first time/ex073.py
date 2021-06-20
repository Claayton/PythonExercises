# Ex073
tabela = ('Flamengo', 'Internacional', 'Atlético', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
          'Atlético Paranaense', 'Red Bull Bragantino', 'Ceará', 'Conrinthians', 'Atlético GO', 'Bahia', 'Sport',
          'Fortaleza', 'Vasco da Gama', 'Goias', 'Coritiba', 'Botafogo')
cont = 0
while True:
    print(f'\033[m\033[7m{"BRASILEIRÃO 2021":^55}\033[m')
    print("""\033[7m[1]\033[m - Mostra todos os times na ordem da tabela
\033[7m[2]\033[m - Mostra o G5 do Brasilerão
\033[7m[3]\033[m - Mostra a zona de rebaixamento do Brasileirão
\033[7m[4]\033[m - Mostra todos os times em ordem alfabética
\033[7m[5]\033[m - Mostra a posição do Grêmio na tabela
\033[7m[6]\033[m - Encerrar programa""")
    print(f'\033[m\033[7m{" ":^55}\033[m')
    choice = int(input('Escolha o que deseja mostrar: '))
    if choice == 1:
        cont = 0
        for times in tabela:
            cont += 1
            if cont % 2 == 0:
                print('\033[31m', end='')
            else:
                print('\033[32m', end='')
            print(f'{cont}°-{times}')
        print('\033[m', end='')
    elif choice == 2:
        cont = 0
        for times in range(0, 5):
            cont += 1
            if cont % 2 == 0:
                print('\033[31m', end='')
            else:
                print('\033[32m', end='')
            print(f'{cont}°-{tabela[cont - 1]}')
            print('\033[m', end='')
    elif choice == 3:
        cont = 17
        for times in range(0, 4):
            if cont % 2 == 0:
                print('\033[31m', end='')
            else:
                print('\033[32m', end='')
            print(f'{cont}°-{tabela[cont - 1]}')
            cont += 1
            print('\033[m', end='')
    elif choice == 4:
        cont = 0
        for times in sorted(tabela):
            cont += 1
            if cont % 2 == 0:
                print('\033[31m', end='')
            else:
                print('\033[32m', end='')
            print(f'{cont}°-{times}')
        print('\033[m', end='')
    elif choice == 5:
        cont = 0
        for times in tabela:
            cont += 1
            print('\033[32m', end='')
            if times == 'Grêmio':
                print(f'{cont}°-{times}\033[m')
    elif choice == 6:
        break
    else:
        print(f'\033[7;31m{"COMANDO INVÁLIDO, TENTE NOVAMENTE":^55}\033[m')
