# Ex081
values = []
while True:
    values.append(int(input('Digite um número: ')))
    while True:
        again = str(input('Deseja digitar mais valores? [S/N]: ')).upper()
        if again == 'S' or again == 'N':
            break
        else:
            print('\033[31mComando inválido, tente novamente!\033[m')
    if again == 'N':
        break
print('-'*40)
print(f'Você digitou \033[32m{len(values)}\033[m valores')
values.sort(reverse=True)
print(f'Os valores na ordem decrescente são: \033[32m{values}\033[m')
if 5 in values:
    print('O valor \033[32m5\033[m faz parte da lista')
else:
    print('O valor \033[32m5\033[m não faz parte da lista')
