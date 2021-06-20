# Ex103
def ficha(nome='<desconhecido>', gols=0):
    print(f'\033[32mO jogador \033[34m{nome}\033[32m, fez \033[34m{gols}\033[32m gols(s) no campeonato!\033[m')


nome_do_jogador = str(input('Nome do jogador: '))
qtdade_de_gols = str(input('Quantidade de gols no campeonato: '))

if qtdade_de_gols.isnumeric():
    qtdade_de_gols = int(qtdade_de_gols)
else:
    qtdade_de_gols = 0
if nome_do_jogador.strip() == '':
    ficha(gols=qtdade_de_gols)
else:
    ficha(nome_do_jogador, qtdade_de_gols)
