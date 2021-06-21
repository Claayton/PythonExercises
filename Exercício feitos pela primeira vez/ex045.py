#Exercício045
from random import randint
from time import sleep
itens = ('', 'PEDRA', 'PAPEL', 'TESOURA')
print('\033[36m==================JOKENPÔ==================\033[m')
print('\033[36m[1] PEDRA\n[2] PAPEL\n[3] TESOURA\033[m')#opções do player
p1 = int(input('\033[36mFAÇA SUA ESCOLHA E DIGITE AQUI: \033[m'))#player escolhendo
pc = randint(1, 3)#computador escolhendo
sleep(0.5)
if p1 != 1 and p1 != 2 and p1 != 3:
    print('\033[31m======OPÇÃO INVÁLIDA, TENTE NOVAMENTE======\033[m')  # caso o player digite algo fora das opções
else:
    print('\033[31m==================JO', end=''), sleep(0.5), print('KEN', end=''), sleep(0.5)#animaçãozinha
    print('PÔ==================\033[m')
    print('\033[33mVocê escolheu {}\n\033[35mComputador escolheu {}'.format(itens[p1], itens[pc]))
    if p1 == 1 and pc == 1 or p1 == 2 and pc == 2 or p1 == 3 and pc == 3:#opções em que o jogo fica empatado
        print('\033[33m==========EMPATE, JOGUE NOVAMENTE==========\033[m')
    elif p1 == 1 and pc == 2 or p1 == 2 and pc == 3 or p1 == 3 and pc == 1:#opções em que o player perde o jogo
        print('\033[31m==============COMPUTADOR VENCEU!==============\033[m')
    elif p1 == 1 and pc == 3 or p1 == 2 and pc == 1 or p1 == 3 and pc == 2:#opções em que o player ganha o jogo
        print('\033[32m==========PARABÉNS, VOCÊ VENCEU!==========\033[m')
print('\033[36mxD\033[m')