#Exercício067
while True:
    escolha = int(input('Qual tabuada você quer saber?: '))
    if escolha < 0: #Encerra o programa quando o número digitado for negativo
        break
    print('_' * 15)
    print('{:^15}'.format(f'TABUADA DO {escolha}'))
    print('-' * 15)
    contador = 0
    while True: #Realiza a repetição para a multiplicação até o número 10
        if contador >= 10: #Interrompe a repetição quando chega no número 10
            break
        contador += 1 #Realiza a contagem dos números para utilizar no print de resposta
        resultado = escolha * contador #Realiza a multiplicação da tabuada
        print(f'{escolha} X {contador:>2} ={resultado:>4}')
print('OBRIGADO POR UTILIZAR O PROGRAMA')
print('xD')
