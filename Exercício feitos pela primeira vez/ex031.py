#Exercício031
from time import sleep
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    sleep(1)
    print('Você vai pagar R$: {:.2f}'.format(distancia*0.50))
else:
    print('-=-=-=-=-=PROMOÇÃO=-=-=-=-=-')
    sleep(1)
    print('Você vai pagar R$: {:.2f}'.format(distancia*0.45))
print('xD')
