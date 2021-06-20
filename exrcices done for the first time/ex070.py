#Exercício070
total = 0
maisdemil = 0
contador = 0
barato = 0
nomebarato = ''
print('\033[31m--------------------------')
print('\033[32m>>>>>ATACADÃO DO M0Z1<<<<<')
print('\033[31m--------------------------')
while True: #Realiza a repetição para continuar cadastrando produtos
    produto = str(input('\033[32mNome do produto: \033[m')).capitalize()
    preco = float(input('\033[32mPreço: \033[m'))
    while True: #Realiza a repetição apenas para o caso do usuário errar na digitação
        continua = str(input('\033[31mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
        if continua == 'S' or continua == 'N': #Se usuário digitar corretamente, interrompe a repetição
            break
    print('\033[31m--------------------------')
    contador += 1 #Realiza a contagem de produtos
    total += preco #Realiza a soma dos produtos
    if preco > 1000: #Realiza a contagem dos produtos com preço maior que 1000
        maisdemil += 1
    if contador == 1: #O primeiro preço torna-se o mais barato no cadastro do primeiro produto
        barato = preco
        nomebarato = produto #Nomeia o protudo mais barato como o primeiro
    if barato > preco: #Indica se o proximo preço for mais barato
        barato = preco
        nomebarato = produto #Nomeia o mais barato como o proximo caso essa seja a situação
    if continua == 'N': #Interrompe a repetição caso usuário indique que não quer continuar
        break
print('\033[31m>>>>>>>FIM DA COMPRA<<<<<<')
print(f'\033[32mTOTAL DA COMPRA: \033[mR$: {total:.2f}')
print(f'\033[m{maisdemil} \033[32mprodutos custam mais de R$: 1000.00')
print(f'\033[32mO produto mais barato foi \033[m{nomebarato} \033[32mque custa R$: \033[m{barato:.2f}')
print('\033[32mxD\033[m')
