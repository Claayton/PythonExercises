# Ex 077
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for cada in palavras:
    print(f'\n\033[mNa palavra \033[36m{cada}\033[m temos as vogais: \033[32m',end='')
    for vogal in cada:
        if vogal in 'AEIOU':
            print(vogal, end=' ')
