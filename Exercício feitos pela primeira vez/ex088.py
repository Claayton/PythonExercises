# Ex088
from random import randint
from time import sleep
draw = []
each = []
print(f'\033[7;35m{"SURPRESINHA MEGA SENA":^36}\033[m')
quantity = int(input('Quantos jogos você quer sortear? '))
cont = 0
cont2 = 0
while cont != quantity:
    while True:
        game = randint(0, 60)
        if game not in each:
            each.append(game)
        if len(each) == 6:
            draw.append(each[:])
            each.clear()
            break
    cont += 1
for c in draw:
    cont2 += 1
    c.sort()
    if cont2 % 2 == 0:
        print(f'\033[7;35m{f" Jogo {cont2}: {c}":<36}\033[m')
    else:
        print(f'\033[7;32m{f" Jogo {cont2}: {c}":<36}\033[m')
    sleep(0.5)
print(f'\033[7;35m{"BOA SORTE! xD":^36}\033[m')
