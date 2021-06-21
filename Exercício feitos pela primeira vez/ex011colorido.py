#Ex011
largura = float(input('\033[31mQual a largura dessa parede? \033[m'))
altura = float(input('\033[31mQual a altura dessa parede? \033[m'))
media = largura*altura
print('\033[31mA área da parede é de \033[m\033[32m{}\033[m\033[31m metros\033[m'.format(media))
print('\033[33mSabendo que cada litro de tinta pinta uma área de 2m²\033[m')
print('\033[33mVocê vai precisar de\033[m \033[32m{}\033[m\033[33m litros de tinta para pinta a parede\033[m'.format(media/2))
print('\033[31mxD\033[m')
