#Ex015b
from time import sleep
km = int(input('\033[33mQuantos km você andou com o carro alugado? \033[m'))
dias = int(input('\033[33mPor quantos dias você alugou ele? \033[m'))
print('\033[32mPREÇO POR DIA: R$60.00\033[m')
print('\033[32mPREÇO POR KM RODADO: R$0.15\033[m')
print('\033[31m=-=-=-CALCULANDO-=-=-=\033[m')
sleep(2)
precodia = dias*60
precokm = km*0.15
print('\033[33mSe você andou {} km com o carro e alugou por {} dias\033[m'.format(km, dias))
print('\033[33mVocê vai pagar R$ \033[m\033[32m{}\033[m'.format(precodia + precokm))
print('\033[33mxD\033[m')
