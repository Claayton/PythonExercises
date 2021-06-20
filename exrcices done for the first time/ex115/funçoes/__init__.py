# Funções Ex115
paint = ['\033[m',         # 0 - Limpa
         '\033[1;40m',     # 1 - Preto
         '\033[1;32m',     # 2 - Verde
         '\033[1;30;42m',  # 3 - Verde2
         '\033[1;36m',     # 4 - Ciano
         '\033[1;41m']     # 5 - Vermelho


def pinta(cores=0):
    return paint[cores]


def linha(tamanho=40):
    return print(f'{pinta(1)}{" "}{pinta()}' * tamanho)


def cabeçalho(frase, cor):
    return print(f'{cor}{f"{frase}":^40}{pinta()}')


def leiaint(descriçao):
    from time import sleep
    while True:
        number = input(descriçao)
        if number.isnumeric():
            number = int(number)
            break
        else:
            print(f'{pinta(5)}{"ERRO, DIGITE APENAS NUMEROS!":^40}{pinta(0)}')
            sleep(1)
    return number


def menu(lista):
    cabeçalho('MENU PRINCIPAL', pinta(1))
    cont = 0
    for c in lista:
        cont += 1
        print(f'{pinta(2)}[ {cont} ]{pinta(4)} {c} {pinta()}')
    linha()
    choice = leiaint(f'{pinta(4)}Sua escolha: {pinta(0)}')
    return choice
