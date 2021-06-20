#Ex006b
num = int(input('\033[4;34m'' Digite um número: ''\033[m'))
print('\033[34mO dobro de {} é: \033[m\033[32m{}\033[m'.format(num, num*2))
print('\033[34mO triplo de {} é: \033[m\033[32m{}\033[m'.format(num, num*3))
print('\033[34mA raiz quadrada de {} é: \033[m\033[32m{:.0f}\033[m'.format(num, num**(1/2)))
print('xD')