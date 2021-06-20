# Ex106
def ajuda(funçao):
    from time import sleep
    print(f'\033[0;30;45mAcessando o manual do {funçao}')
    sleep(1)
    print('\033[0;30;42m')
    help(funçao)
    sleep(1)

print('\033[0;30;46m=' * 40)
print(f'{"SISTEMA DE AJUDA PyHelp":^40}')
print('\033[0;30;46m=' * 40)
comando = input('\033[mFunção ou Biblioteca-> ')
while True:
    if comando.lower() == 'fim':
        print('\033[0;30;41m=' * 40)
        print(f'{"ESPERO TER AJUDADO, VOLTE QUANDO PRECISAR!":^40}')
        print('\033[0;30;41m=' * 40)
        break
    ajuda(comando)
    print('\033[0;30;46m=' * 40)
    print(f'{"SISTEMA DE AJUDA PyHelp":^40}')
    print('\033[0;30;46m=' * 40)
    comando = input('\033[mFunção ou Biblioteca-> ')
