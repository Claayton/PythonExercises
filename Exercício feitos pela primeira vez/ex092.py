# Ex092
from datetime import date

ano_atual = date.today().year
cadastro = {}

cadastro['Nome'] = str(input('Nome: ')).title().strip()
ano_de_nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = ano_atual - ano_de_nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho [digite "0" caso não tenha]: '))

if cadastro['CTPS'] != 0:
    while True:
        cadastro['Contratação'] = int(input('Ano de contratação: '))
        if cadastro['Contratação'] > ano_de_nascimento:
            break
        else:
            print('\033[31mSegundo os dados cadastrados')
            print('essa pessoa não teria nascido ainda nessa data')
            print('POR FAVOR TENTE NOVAMENTE\033[m')
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - ano_de_nascimento

print('-' * 30)
for c, j in cadastro.items():
    print(f'\033[36m{c}\033[m tem o valor \033[34m{j}\033[m')
print('-' * 30)
