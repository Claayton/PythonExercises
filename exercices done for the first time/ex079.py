# Ex079
values = []
again = ''
while True:
    number = int(input('Digite um valor: \033[32m'))
    if number not in values:
        values.append(number)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado não será adicionado!\033[m')
    while True:
        again = str(input('Quer digitar outro valor? [S/N]: \033[32m')).upper()
        if again == 'S' or again == 'N':
            break
        else:
            print('\033[31mComando inválido, Tente novamente!\033[m')
    if again == 'N':
        break
print('-' * 40)
print('Você adicionou os valores: ', end=' ')
for v in sorted(values):
    print(v, end=' ')
print()
