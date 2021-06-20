# Ex091
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
for j in range(0, 4):
    num = randint(1, 6)
    jogadores[f'Jogador0{j + 1}'] = num
print('\033[34mValores sorteados:\033[m')
for j, c in jogadores.items():
    sleep(0.5)
    print(f'O \033[32m{j}\033[m tirou o valor: \033[32m{c}\033[m.')

print('\033[34mRanking dos jogadores:\033[m')
ordenados = {}
ordenados = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
cont = 0

for j, c in ordenados:
    cont += 1
    print(f'Em \033[32m{cont}° lugar \033[m o \033[32m{j}\033[m com  \033[32m{c}\033[m pontos.')
