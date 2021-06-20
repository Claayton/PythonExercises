#Exercício068
from random import randint
from time import sleep
resultadofinal = ''
contador = 0
while True: #Repete tudo até jogador perder
  if resultadofinal == '\033[31mGAME OVER\033[m': #Se jogador perder o programa para
    break
  print('\033[36m>>>>>>>>>> PAR OU ÍMPAR <<<<<<<<<<\033[m')
  print('\033[36m-\033[m'*34)
  playernum = int(input('Escolha seu número entre 0 e 10: '))
  pcnum = randint(0, 10) #PC escolhe um número aleatório entre '0' e '10'
  soma = playernum + pcnum #Realiza a soma da escolha do jogador e da escolha do PC
  if soma % 2 == 0: #Se o resto da divisão por 2 for '0' significa que o resultado foi 'PAR'
    resultado = 'P'
  elif soma % 2 != 0: #Se o resto da divisão por 2 não for '0' significa que o resultado foi 'ÍMPAR'
    resultado = 'I'
  while True:
    escolhaplayer = str(input('Você escolhe PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0] #Jogador escolhe PAR/ÍMPAR
    if escolhaplayer == 'P' or escolhaplayer == 'I':
      break
  sleep(0.5) #Tempinho para calcular o resultado (apenas estética)
  if resultado == escolhaplayer: #Se resultado for igual a escolha do player, player ganha e jogo repete
    resultadofinal = '\033[32mGANHOU\033[m'
    contador += 1 #Conta quantas vezes player ganha
  elif resultado != escolhaplayer: #Se resultado for diferente de escolha do player, player perde e jogo acaba
    resultadofinal = '\033[31mGAME OVER\033[m'
  if resultado == 'P': resultado = 'PAR' #Apenas para facilitar, nomeia 'P' como 'PAR'
  elif resultado == 'I': resultado = 'ÍMPAR' #Apenas para facilitar, nomeia 'I' como 'ÍMPAR'
  print('\033[36m-\033[m'*34)
  print(f'Você jogou \033[32m{playernum}\033[m e o computador jogou \033[32m{pcnum}\033[m')
  print(f'{soma} é {resultado}')
  print(resultadofinal)
  sleep(0.5)
print(f'Você ganhou {contador} vezes')
print('\033[36mxD\033[m')
