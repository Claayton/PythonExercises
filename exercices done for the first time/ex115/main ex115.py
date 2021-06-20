# Ex115
from arquivo import *
from funçoes import *
from time import sleep

txt = 'cursoemvideo.txt'
if not arquivoexiste(txt):
    criararquivo(txt)

while True:
    choice = menu(['Ver pessoas Cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])
    if choice == 1:
        # Opção de listar o conteúdo do arquivo
        lerarquivo(txt)
        sleep(1)
    elif choice == 2:
        # Opção de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO', pinta(3))
        nome = str(input(f'{pinta(4)}Nome: {pinta()}'))
        idade = leiaint(f'{pinta(4)}Idade: {pinta()}')
        cadastrar(txt, nome, idade)
        sleep(1)
    elif choice == 3:
        # Opção de sair do sistema
        print(f'{pinta(4)}Saindo... {pinta()}')
        sleep(1)
        print(f'{pinta(3)}{"OBRIGADO POR UTILIZAR O PROGRAMA!":^40}{pinta()}')
        break
    else:
        print(f'{pinta(5)}{"OPÇÃO INVÁLIDA, TENTE NOVAMENTE!":^40}{pinta()}')
        sleep(1)
        continue
