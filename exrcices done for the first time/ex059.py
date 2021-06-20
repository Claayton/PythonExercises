#Exercício059
from time import sleep
escolha = 0
n1 = int(input('\033[33mDigite seu primeiro valor: \033[m'))
n2 = int(input('\033[33mDigite seu segundo valor: \033[m'))
while escolha != 5: #Enquanto a opção 5 não for escolhida programa continua
  print('''  \033[36m[1]- SOMAR
  [2]- MULTIPLICAR
  [3]- MAIOR
  [4]- NOVOS NÚMEROS
  [5]- SAIR DO PROGRAMA''')
  escolha = int(input('\033[33mEscolha uma das opções: \033[m')) #Você escolhe sua opção dentre as 5 disponíveis
  if escolha == 1: #Se a escolha for '1', os números serão somados e lhe mostrará o resultado
    soma = n1 + n2
    print('\033[32mO resultado da soma {} + {}  é: \033[m{}'.format(n1, n2, soma))
  elif escolha == 2: #Se a escolha for '2', os números serão multipçlicados e lhe mostrará o resultado
    multiplicar = n1 * n2
    print('\033[32mO resultado da multiplicação {} X {} é: \033[m{}'.format(n1, n2, multiplicar))
  elif escolha == 3: #Se a escolha for '3', lhe mostrará qual dos números é o maior
    if n1 > n2:
      maior = n1
    elif n2 > n1:
      maior = n2
    print('\033[32mO maior número entre {} e {} é: \033[m{}'.format(n1, n2, maior))
  elif escolha == 4: #Se a escolha for '4', você poderá escolher novos números
    n1 = int(input('\033[33mDigite seu primeiro valor: \033[m'))
    n2 = int(input('\033[33mDigite seu segundo valor: \033[m'))
  elif escolha == 5: #Se a escolha for '5', programa se encerra mostrando uma mensagem de agradecimento
    print('\033[33mFINALIZANDO!...')
  else: #Se a escolha não estiver dentre as opções disponíveis aparece um aviso de opção inválida
    print('\033[31mOPÇÃO INVÁLIDA!, TENTE NOVAMENTE!')
  sleep(1)
print('\033[33mORBIGADO POR UTILIZAR O PROGRAMA!')
print('\033[33mxD\033[m')
