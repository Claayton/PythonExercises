# Módulo
def aumentar(num, aumento, dinheiro=False):
    result = num + (num * aumento / 100)
    if dinheiro:
        return f'R$: {result:.2f}'
    else:
        return result


def diminuir(num, desconto, dinheiro=False):
    result = num - (num * desconto / 100)
    if dinheiro:
        return f'R$: {result:.2f}'
    else:
        return result


def dobro(num, dinheiro=False):
    result = num * 2
    if dinheiro:
        return f'R$: {result:.2f}'
    else:
        return result


def metade(num, dinheiro=False):
    result = num / 2
    if dinheiro:
        return f'R$: {result:.2f}'
    else:
        return result


def moeda(num):
    return f'R$: {num:.2f}'


def resumo(num, aumento, desconto):
    print('-' * 50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-' * 50)
    print(f'{"Preço analisado":_<35}{moeda(num):_>15}')
    print(f'{"Dobro do preço":_<35}{moeda(dobro(num)):_>15}')
    print(f'{"Metade do preço":_<35}{moeda(metade(num)):_>15}')
    print(f'{"80% de Aumento":_<35}{moeda(aumentar(num, 80)):_>15}')
    print(f'{"35% de Redução":_<35}{moeda(diminuir(num, 35)):_>15}')
    print('-' * 50)
