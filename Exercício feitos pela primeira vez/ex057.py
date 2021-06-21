#Exercício057
sex = ''
escolha = ''
while sex != 'M' and sex != 'F':
#Enquanto não for digitado 'M' ou 'F' o programa continua perguntando
  sex = input('\033[36mDigite seu sexo \033[32m[M ou F]: ').strip().upper()[0]
  if sex == 'M': #Se digitar 'M' escolha recebe Masculino
    escolha = 'Masculino'
    print('\033[32mVocê escolheu a opção {}'.format(escolha))
  elif sex == 'F': #Se digitar 'F' escolha recebe Feminino
    escolha = 'Feminino'
    print('\033[32mVocê escolheu a opção {}'.format(escolha))
  else: #Se digitar qualquer outra coisa, programa insiste
    print('\033[31mOpção Inválida - Tente Novamente!\033[m')
print('xD')
