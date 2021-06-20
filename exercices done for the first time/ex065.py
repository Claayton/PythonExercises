#Exercício065
contador = 0
continua = 'S'
maior = menor = 0
soma = 0
while continua == 'S': #Enquanto digitar 'S' o programa continua
  num = int(input('\033[33mDigite um número: \033[m'))
  contador += 1 #Realiza a contagem de vezem em que se digita algum número
  soma += num #Soma cada número digitado
  if contador == 1:
    maior = num #Recebe o valor apenas do primeiro número digitado
    menor = num #Recebe o valor apenas do primeiro número digitado
  if maior < num:
    maior = num #Recebe o próximo número caso ele seja maior
  if menor > num:
    menor = num #Recebe o próximo número caso ele seja menor
  continua = str(input('\033[33mQuer continuar digitando números? [N] or [S]: \033[m')).strip().upper()[0]
if continua == 'N': #Termina o programa mostrando o resultado
  media = soma / contador
  print('\033[32mVocê digitou {} números'.format(contador))
  print('\033[32mA soma dos números que você digitou é \033[31m{}'.format(soma))
  print('\033[32mA média dos números que você digitou é \033[31m{}'.format(media))
  print('\033[32mO maior dos números que você digitou é \033[31m{}'.format(maior))
  print(f'\033[32mO menor dos números que você digitou é \033[31m{menor}') #Novo método
  print('\033[32mOBRIGADO POR UTILIZAR O PROGRAMA')
elif continua != 'N' and continua != 'S':
#Mostra uma mensagem de erra caso não seja digitado 'N' ou 'S'
  print('\033[31mCOMANDO INVÁLIDO - TENTE NOVAMENTE')
print('\033[33mxD\033[m')
