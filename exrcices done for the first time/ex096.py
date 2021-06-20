# Ex096
def area(largura, comprimento):
    print(f'A área de um terreno de \033[32m{largura:.1f}\033[m x \033[32m{comprimento:.1f}\033[m'
          f' é de \033[32m{largura*comprimento:.1f}m²\033[m')


print(f'\033[7;37m{"CONTROLE DE TERRENOS":^60}\033[m')
area(float(input('Qual a largura do terreno?: ')), float(input('Qual o comprimento do terreno?: ')))
