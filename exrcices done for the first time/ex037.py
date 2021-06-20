#Exercício037
print('\033[32mCONVERSOR DE NÚMEROS\033[m')
numero = int(input('\033[36mDigite um número: \033[m'))
print('\033[32m-=\033[m'*12)
escolha = str(input('\033[36mESCOLHA\n_1 para BINARIO\n_2 para OCTAL\n_3 para HEXADECIMAL\nse preferir escreva: \033[m')).upper()
print('\033[32m-=\033[m'*12)
binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)
if escolha == '1' or escolha == 'BINARIO':
  print('\033[32m EM BINÁRIO:\033[m {}'.format(binario[2:]))
elif escolha == '2' or escolha == 'OCTAL':
  print('\033[32m EM OCTAL: \033[m {}'.format(octal[2:]))
elif escolha == '3' or escolha == 'HEXADECIMAL':
  print('\033[32mEM HEXADECIMAL: \033[m{}'.format(hexa[2:]))
else:
  print('\033[31mOPÇÃO INVÁLIDA\033[m')
print('\033[32m-=\033[m'*12)
print('\033[32mxD\033[m')
