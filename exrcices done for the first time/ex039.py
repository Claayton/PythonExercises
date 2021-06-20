#Exercício039
from datetime import date
year = int(input('\033[36mQual o ano do seu nascimento?: \033[m'))
thisyear = date.today().year
idade = thisyear - year
if idade < 18:
  print('\033[32mAinda não chegou sua hora de se alistar ao serviço militar\033[m')
  print('\033[32mAinda falta {} anos até chegar sua vez\033[m'.format(18 - idade))
elif idade == 18:
  print('\033[33mJá está na sua hora de se alistar ao serviço militar\033[m')
else:
  print('\033[31mJá passou da sua hora de se alistar ao serviço militar')
  print('Você passou {} anos do prazo para se alistar seu tongo\033[m'.format(idade - 18))
print('\033[36mxD\033[m')
