#Exercício042
print('\033[33mDIGITE UM VALOR PARA 3 RETAS E\nLHE MOSTRAREI SE É POSSÍVEL FORMAR UM TRIÂNGULO\nE O TIPO DE TRIÂNGULO QUE SERÁ FORMADO\033[m')
AB = float(input('\033[33mDigite o tamanho da primeira reta: \033[m'))
CD = float(input('\033[33mDigite o tamanho da segunda reta: \033[m'))
EF = float(input('\033[33mDigite o tamanho da terceira reta: \033[m'))
lista = [AB, CD, EF]
lista = (sorted(lista))
listaordem = lista[0]+lista[1]
if listaordem > lista[2]:
    print('\033[32mSIM!, é possível formar um triângulo\033[m')
    if AB == CD == EF:
        print('\033[35mTRIÂNGULO EQUILÁTERO\033[m')
    elif AB == CD and AB != EF or AB == EF and AB != CD or CD == EF and CD != AB:
        print('\033[35mTRIÂNGULO ISÓSCELES\033[m')
    else:
        print('\033[35mTRIÂNGULO ESCALENO\033[m')
    print('\033[33mxD\033[m')
else:
    print('\033[31mNÃO!, é impossível formar um triângulo\033[m')
