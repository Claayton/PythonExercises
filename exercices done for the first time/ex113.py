# Ex113
def leiaint(descriçao):
    while True:
        try:
            number = int(input(descriçao))
        except (ValueError, TypeError):
            print('\033[31mERRO, Digite um número Inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return number


def leiafloat(descriçao):
    while True:
        try:
            number = float(input(descriçao))
        except (ValueError, TypeError):
            print('\033[31mERRO, Digite um número Real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return number


inteiro = leiaint('Digite um número Inteiro: ')
real = leiafloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {inteiro}, e o Real foi {real}')
