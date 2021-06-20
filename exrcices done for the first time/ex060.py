#Exercício060
from math import factorial
number = int(input('\033[34mDigite um número e lhe mostrarei o seu fatorial: '))
factorial = factorial(number) #Define o resultado de fatorial para o número escolhido
if number == 0: #Se o número escolhido for '0' o programa mostra a mensagem de erro para não bugar a maquina
    print('\033[31m--ERRO, TENTE NOVAMENTE!--')
else: #Caso contrário segue normalmente
    print('\033[32m{}! \033[31m= \033[32m{}'.format(number, number),end='')#Mostra de cara o número que vc escolheu e o primeiro algarismo (1)
    while number != 1: #Enquanto não chegar ao '1' continua repetindo os números em ordem decrescente
      number = number - 1 #Faz a ordem decrescente dos números
      print(' \033[31mx \033[32m{}'.format(number),end='')
    print(' \033[31m= \033[32m{}'.format(factorial))
print('\033[34mxD\033[m')
