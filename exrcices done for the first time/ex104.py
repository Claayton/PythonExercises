# Ex104
def leiaint(descriçao):

    while True:
        number = input(descriçao)
        if number.isnumeric():
            number = int(number)
            break
        else:
            print('\033[31mERRO, Digite um número inteiro válido!\033[m')
    print(f'Você digitou o número {number}')


numero = leiaint('Digite um número: ')
