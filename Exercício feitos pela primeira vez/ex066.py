#Exercício066
contador = 0
soma = 0
print('\033[31mPara encerrar o programa digite "999" a qualquer momento\033[m')
while True:
    num = int(input('\033[34mDigite um número: \033[m'))
    if num == 999: #Programa para quando for digitado '999'
        break
    contador += 1 #Conta quantos números foram digitados
    soma += num #Realiza a soma dos números digitados
print(f'\033[32mVocê digitou {contador}')
print(f'\033[32mA soma entre eles é {soma}')
print('\033[34mxD\033[m')
