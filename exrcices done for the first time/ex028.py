#Exercício028
from random import choice
from time import sleep
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('TENTE ADVINHAR O NÚMERO QUE ESTOU "PENSANDO" ENTRE 0 E 5...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
pcnum = choice([0, 1, 2, 3, 4, 5]) #O computador pensa em um número
playernum = int(input('Em que número eu pensei? ')) #O jogador tenta adivinhar
print('..........PROCESSSANDO!..........')
sleep(2)
if playernum == pcnum:
    print('PARABÉNS SEU MERDA, VOCÊ CONSEGUIU ME VENCER!!!')
    print('Realmente eu pensei no número {}'.format(pcnum))
else:
    print('NÚMERO ERRADO OTÁRIO, TENTE OUTRA VEZ!!!')
    print('O número que eu tinha pensado foi o {}'.format(pcnum))
print('xD')
