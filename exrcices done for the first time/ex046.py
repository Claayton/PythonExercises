#Exercício046
from time import sleep
import emoji
print('\033[32mCONTAGEM REGRESSIVA PARA O ANO NOVO:\033[m')
sleep(1)
for c in range(10, 0 - 1, -1):#repete os números de 10 até o 0
    print(c)
    sleep(1)
print(emoji.emojize("\033[31m:boom::boom::boom:KABUM:boom::boom::boom:", use_aliases=True))
print(emoji.emojize("\033[32m:boom::boom::boom:FOGUETE:boom::boom::boom:", use_aliases=True))
print(emoji.emojize("\033[33m:boom::boom::boom:FOGOS E MAIS FOGOS:boom::boom::boom:", use_aliases=True))
print(emoji.emojize("\033[34m:boom::boom::boom:GUANAGARA VIADO:boom::boom::boom:", use_aliases=True))
print('\033[32mxD')