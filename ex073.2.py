# Ex073.2
"""Create a tuple filled with the top 20 from the Brazilian soccer league table, in the order of placement.
Then show:
A)-The first 5;
B)-The last 4 placed;
C)-Teams in alphabetical order;
D)-Wat position is the GRÊMIO team in."""

teams = ('Fortaleza', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
         'Fluminense', 'Palmeiras', 'Bahia', 'Atlético-GO', 'Flamengo',
         'Corinthians', 'Sport', 'Ceará', 'Santos', 'Internacional',
         'Cuiabá', 'São Paulo', 'Chapecoense', 'Juventude', 'América-MG', 'Grêmio')

Show = input('\033[34mPress \033[32mEnter\033[34m to show the top 5 from the brazilian soccer League are: \033[m')
for c in range(0, 5):
    print(f'\33[31m{c + 1}°\033[m - ', end='')
    print(f'\033[32m{teams[c]}\033[m')
Show = input('\033[34mPress \033[32mEnter\033[34m'
             ' to show the last 4 placed from the brazilian soccer league are: \033[m')
for c in range(16, 20):
    print(f'\33[31m{c + 1}°\033[m - ', end='')
    print(f'\033[32m{teams[c]}\033[m')
Show = input('\033[34mPress \033[32mEnter\033[34m to show the teams in alphabetical order: \033[m')
cont = 0
for c in sorted(teams):
    cont += 1
    print(f'\033[31m{cont}°\33[m - \033[32m{c}\033[m')
Show = input('\033[34mPress \033[32mEnter\033[34m to show the position of the \033[32mGrêmio\033[34m team: \033[m')
for e, c in enumerate(teams):
    if c == 'Grêmio':
        print(f'\033[31m{e + 1}°\33[m - \033[32m{c}\033[m')
print('\033[34mxD\033[m')
