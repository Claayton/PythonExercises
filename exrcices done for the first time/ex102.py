# Ex102
def fatorial(numero, show=False):
    """
    => CALCULA O FATORIAL DE UM NÚMERO.
    :param numero: O valor inteiro que o usuário deseja saber o fatorial.
    :param show: (Opcional) Mostrar o cálculo inteiro/Mostrar apenas o resultado.
    :return: O resultado fatorial do valor 'numero'.
    """
    cont = 0
    result1 = 1
    result2 = 1

    if not show:
        while numero > 0:
            result1 *= numero
            numero -= 1
        return print(f'\033[32m{result1}\033[m')
    else:
        while numero > 0:
            cont += 1
            if cont == 1:
                print(f'\033[32m{numero}!', end='\033[31m = \033[m')
            result2 *= numero
            numero -= 1
            print(numero + 1, end='')
            print('\033[31m X \033[m' if numero > 0 else '\033[31m = \033[m', end='')
        return print(f'\033[32m{result2}\033[m')


factorial = int(input('Digite um número para ver o fatorial: '))
print('-' * 50)
print(f'{"CALCULO DE FATORIAL":^50}')
print('-' * 50)
fatorial(factorial, True)
help(fatorial)
