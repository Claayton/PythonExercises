# Ex 101
from datetime import date


def voto(ano_de_nascimento):
    global idade
    idade = date.today().year - ano_de_nascimento

    if idade < 16:
        return 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'


nascimento = int(input('Digite o ano de nascimento: '))
print(f'Com {date.today().year - nascimento} anos, {voto(nascimento)}')
