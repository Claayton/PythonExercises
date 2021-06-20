#Ex011b
preço = float(input('\033[34mQual o preço desse produto? \033[m'))
print('\033[34m=-\033[m'*20)
print('\033[31mPROMOÇÃO\033[m')
print('\033[34m=-\033[m'*20)
print('\033[34mHoje esse produto esta custando: \033[m\033[31mR$ {:.2f}\033[m'.format(preço - (preço*5/100)))
print('\033[34mxD\033[m')
