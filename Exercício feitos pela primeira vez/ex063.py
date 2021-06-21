#Exercicio063
print('\033[32m-----SEQUÊNCIA DE FIBONACCI-----')
number = int(input('\033[32mQuantos dígitos da sequência você quer ver?: '))
contador = 0
fib0 = 0
fib1 = 1
fib2 = 0
if number == 0 or number == 1: #Se se for escolhido '0' ou '1' dígitos, será mostrado o número '0'
  print('\033[32m{}'.format(0))
elif number == 2: #Se for escolhido '2' dígitos, será mostrado os números '0' e '1'
  print('\033[32m{}\033[31m - \033[32m{}'.format(0, 1))
else: #Se for escolhido qualquer outro valor, será mostrado a quantidade de dígitos escolhida
  print('\033[32m{} \033[31m-> \033[32m{}'.format(0, 1), end=' \033[31m-> \033[m')
  while contador != number - 2: #Repete até mostrar a quantidade de dígitos escolhida
    contador+= 1 #Realiza a contagem de digitos
    fib2 = fib0 + fib1 #Soma os dois últimos valores para chegar em um novo valor
    print('\033[32m{}'.format(fib2), end=' \033[31m-> ')
    fib0 = fib1 #Indica que na próxima repetição, o valor recebido por 'fib1' será lido como 'fib0'
    fib1 = fib2 #Indica que na próxima repetição, o valor recebido por 'fib2' será lido como 'fib1'
print('\033[32mFIM\033[m')
