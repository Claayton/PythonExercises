#Exercício038
num1 = int(input('\033[36mDigite um número: \033[m'))
num2 = int(input('\033[36mDigite outro número: \033[m'))
if num1 > num2:
  print('\033[32mO primeiro número é MAIOR\033[m')
elif num2 > num1:
  print('\033[33mO segundo número é MAIOR\033[m')
else:
  print('\033[31mNÃO EXISTE VALOR MAIOR\nOs dois números são iguais\033[m')
print('\033[36mxD\033[m')
