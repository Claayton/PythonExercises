#Exercício052
num = int(input('\033[32mDigite um número: '))
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print('\033[31mEste número \033[32mNÃO\033[m \033[31mé primo, segue em verde os números em que ele pode ser dividido: ')
    for c in range(1, num + 1):
        if num % c == 0:
            print('{}'.format('\033[32m'), end=' ')
        else:
            print('{}'.format('\033[31m'), end=' ')
        print(c, end=' ')
else:
    print('\033[32mEste número é primo, ele só pode ser dividido por 1 e por ele mesmo: ')
    for c in range(1, num + 1):
        if num % c == 0:
            print('{}'.format('\033[32m'), end=' ')
        else:
            print('{}'.format('\033[31m'), end=' ')
        print(c, end=' ')

print('\nxD')
