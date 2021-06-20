#Exercício058
from random import randint
print('\033[34m______________________________________________________________')
print('\033[32mTENTE ADIVINHAR O NÚMERO QUE ESTOU "PENSANDO!" ENTRE 0 E 10...')
print('\033[34m--------------------------------------------------------------')
pcnum = randint([0, 10]) #Escolhe um dos números entre 0 e 10
playernum = 0
contagem = 0
while playernum != pcnum: #Enquanto playernum for diferente de pcnum o programa continua
    playernum = int(input('\033[34mQual é o seu palpite?: '))
    contagem += 1 #Contador de erros do jogador
    if playernum > pcnum: #Mostra se o número for menor que o do comoutador
        print('\033[31mUM POUCO MENOS, TENTE NOVAMENTE!')
    elif playernum < pcnum: #Mostra se o número for maior que o do computador
        print('\033[31mUM POUCO MAIS, TENTE NOVAMENTE')
print('\033[32mACERTOU!')
print('\033[32mForam necessários {} palpites para vencer!'.format(contagem))
print('\033[34mxD\033[m')
