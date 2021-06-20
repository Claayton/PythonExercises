# Módulo
def leiadinheiro(valor):
    while True:
        valor_lido = input(valor).strip().replace(',', '.')
        if valor_lido.replace('.', '').isnumeric():
            valor_lido = float(valor_lido)
            break
        else:
            print(f'\033[31mERRO "{valor_lido}" NÃO É UM PREÇO VÁLIDO!\033[m')
    return valor_lido
