#Exercício036
from time import sleep
print('\033[36mFICHA DE EMPRÉSTIMO PARA COMPRA DE CASA\033[m')
valor = float(input('\033[36mQual o valor da casa? \033[m'))
salario = float(input('\033[36mQual o salário do comprador? \033[m'))
anos = int(input('\033[36mEm quantos anos pretende pagar?\033[m '))
meses = anos*12
mensal = valor/meses
if mensal > (salario*30/100):
    sleep(1)
    print('\033[31m==-=-=-DESCULPE, EMPRÉSTIMO NEGADO-=-=-==\033[m')
else:
    sleep(1)
    print('\033[32m==-=-=-EMPRÉSTIMO APROVADO-=-=-==\033[m')
    print('\033[36mO valor da prestação mensal da casa é de\033[m\033[32m R${:.2f}\033[m'.format(mensal))
print('\033[36mxD\033[m')
