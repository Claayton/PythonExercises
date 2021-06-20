# Ex072
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        numero = int(input('Digite um número entre "0" e "20": '))
        if 20 >= numero >= 0:
            break
        print('\033[31mOpção invãlida!, Tente novamente\033[m')
    print(f'Você digitou o número \033[32m{extenso[numero]}\033[m')
    continua = str(input('Vpcê quer tentar novamente?[S/N]: ')).upper().strip()
    if continua == 'N':
        break
print('xD')
