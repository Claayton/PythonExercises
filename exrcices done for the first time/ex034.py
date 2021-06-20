#Exercício034
salario = float(input('Qual o seu salário?: '))
print('-=-=VOCÊ ACABA DE RECEBER UM AUMENTO=-=-')
if salario == 1250 or salario < 1250:
  novo = salario + (salario*15/100)
else:
  novo = salario + (salario*10/100)
print('Seu salário de R$ {:.2f} passará a ser R$ {:.2f}'.format(salario, novo))
print('xD')
