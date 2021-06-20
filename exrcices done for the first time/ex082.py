# Ex082
values = []
pares = []
impares = []
while True:
    number = int(input('Digite um número: '))
    values.append(number)
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)
    while True:
        again = str(input('Quer digitar mais números? [S/N]: ')).upper()
        if again == 'S' or again == 'N':
            break
        else:
            print('Comando inválido, tente novamente!')
    if again == 'N':
        break
print('-' * 40)
print(f'A lista completa é \033[32m{values}\033[m')
print(f'A lista de pares é \033[32m{pares}\033[m')
print(f'A lista de ímpares é \033[32m{impares}\033[m')
