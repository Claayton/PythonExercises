#Exercício029
from time import sleep
velocidade = float(input('Qual a sua velocidade? '))
if velocidade > 80:
    print('-=-=-=-=PROCESSANDO=-=-=-=-')
    sleep(2)
    print('VOCÊ FOI MULTADO SEU BURRO!!!')
    print('O limite de velocidade é 80km/h')
    multa = float(velocidade - 80) * 7
    print('Você deve pagar uma multa de R$: {:.2f}'.format(multa))
else:
    print('-=-=-=-=PROCESSANDO=-=-=-=-')
    sleep(2)
    print('PARABÉNS!!!\nVocê está dentro do limite de velocidade!')
print('Tenha um bom dia e dirija com segurança!')
print('xD')
