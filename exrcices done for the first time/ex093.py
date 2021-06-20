# Ex093
jogador = {}

jogador['Nome'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input(f'Quantas partidas \033[36m{jogador["Nome"]}\033[m jogou no campeonato? '))
jogador['Gols'] = []

for c in range(0, partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na {c + 1}° partida? ')))

total = 0
for t in jogador['Gols']:
    total += t
jogador['Total'] = total
print('=' * 60)
print(jogador)
print('=' * 60)
for c, j in jogador.items():
    print(f'\033[34m{c}\033[m tem o valor \033[36m{j}\033[m.')
print('=' * 60)
print(f'\033[32mO jogador {jogador["Nome"]} jogou {partidas} partidas.\033[m')
cont = 0
for c in jogador['Gols']:
    print(f'\033[31m=>\033[m Na \033[34m{cont + 1}° \033[m partida, fez \033[36m{c}\033[m gol(s).')
    cont += 1
print(f'No total \033[32m{jogador["Nome"]}\033[m fez \033[32m{jogador["Total"]}\033[m gol(s).')
print('=' * 60)
