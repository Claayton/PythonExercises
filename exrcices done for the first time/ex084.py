# Ex084
cadastro = []
pessoas = []
cont = 0
print(f'\033[7m{"CADASTRO DE PESO":^45}\033[m')
while True:
    pessoas.append(str(input('Nome: ').title()))
    pessoas.append(float(input('Peso: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    cont += 1
    while True:
        again = str(input('Quer cadastrar mais alguém? [S/N]: ')).upper()
        if again == 'S' or again == 'N':
            print(f'\033[7;40;32m{f"{cont} PESSOA(S) CADASTRADA(S) COM SUCESSO!":^45}\033[m')
            break
        else:
            print(f'\033[7;40;31m{"OPÇÃO INVÁLIDA, TENTE NOVAMENTE!":^45}\033[m')
    if again == 'N':
        break
cont2 = 0
maior = []
menor = []
for pessoa in cadastro:
    if cont2 == 0:
        maior.append(pessoa)
        menor.append(pessoa)
    cont2 += 1
    if maior[0][1] < pessoa[1]:
        maior.clear()
        maior.append(pessoa)
    elif maior[0][1] == pessoa[1] and maior[0][0] != pessoa[0]:
        maior.append(pessoa)
    if menor[0][1] > pessoa[1]:
        menor.clear()
        menor.append(pessoa)
    elif menor[0][1] == pessoa[1] and menor[0][0] != pessoa[0]:
        menor.append(pessoa)
print(f'\033[mO maior peso é {maior[0][1]:.1f}kg. Peso de: ', end='\033[32m')
for ma in maior:
    print(ma[0], end='; ')
print(f'\n\033[mO menor peso é {menor[0][1]:.1f}kg. Peso de: ', end='\033[32m')
for me in menor:
    print(me[0], end='; ')
print('\033[m')
