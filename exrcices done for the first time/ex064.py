#Exercício064
print('\033[31mDigite "999" quando quiser encerrar o programa\033[m')
contador = 1 #Já começa em 1 pq o primeiro número esta fora do laço
num1 = int(input('\033[34mDigite seu primeiro número: \033[m'))
num2 = 0
soma = num1 #Soma recebe número pq o primeiro número esta fora do laço
while num2 != 999: #Encerra o programa apenas quando for digitado '999'
    num2 = int(input('\033[34mDigite mais um número: \033[m'))
    if num2 != 999: #Realiza a soma dos números apenas a menos que o número seja '999'
        contador += 1  # Realiza a contagem de números digitados
        soma += num2 #Realiza a soma dos números
print('\033[32mVocê digitou {} números '.format(contador)) #O primeiro número esta fora do laço, por isso '-1'
print('\033[32mA soma dos números que você digitou foi {}'.format(soma))
print('\033[34mxD\033[m')
