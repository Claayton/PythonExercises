# Ex095
lista_de_jogadores = []
cont = 0

print(f'\033[7;37m{"DADOS SOBRE APROVEITAMENTO DE JOGADORES DE FUTEBOL":^60}\033[m')
while True:
    cont += 1
    lista_de_jogadores.append({})
    lista_de_jogadores[cont - 1]['Cod'] = cont - 1
    lista_de_jogadores[cont - 1]['Nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas \033[36m{lista_de_jogadores[cont -1]["Nome"]}\033[m jogou no campeonato? '))
    lista_de_jogadores[cont - 1]['Gols'] = []

    for c in range(0, partidas):
        lista_de_jogadores[cont - 1]['Gols'].append(int(input(f'Quantos gols na {c + 1}° partida? ')))
    total = 0

    for t in lista_de_jogadores[cont - 1]['Gols']:
        total += t
    lista_de_jogadores[cont - 1]['Total'] = total
    while True:
        again = str(input(f'\033[7;34m{"Quer cadastrar mais algum jogador? [S/N]: ":^60}\033[m')).upper().strip()
        if again != 'S' and again != 'N':
            print(f'\033[7;31m{"COMANDO INVÁLIDO, TENTE NOVAMENTE!":^60}\033[m')
        if again == 'S' or again == 'N':
            break
    if again == 'N':
        break

print(f'{"Cod":<5}{"Nome":<25}{"Gol(s)":^25}{"Total":>5}')
for c in lista_de_jogadores:
    gols = str(c['Gols'])
    print(f'\033[7;34m{c["Cod"]:<5}{c["Nome"]:<25}{gols:^25}{c["Total"]:>5}\033[m')

while True:
    while True:
        show = int(input('Mostra dados de qual jogador?[Digite "999" para parar]: '))
        if show != 999 and show > (len(lista_de_jogadores) - 1):
            print(f'\033[7;31m{"JOGADOR NÃO CADASTRADO, TENTE OUTRO CÓDIGO!":^60}\033[m')
        else:
            break
    if show == 999:
        print(f"\033[7;32m{'OBRIGADO POR UTILIZAR O PROGRAMA!':^60}\033[m")
        break
    nome = lista_de_jogadores[show]['Nome']
    print(f"\033[7;37m{f'LEVANTAMENTO DO JOGADOR {nome}':^60}\033[m")
    jogo = 0
    for c in lista_de_jogadores[show]["Gols"]:
        jogo += 1
        print(f'No jogo \033[34m{jogo}\033[m, fez \033[34m{c} gol(s)\033[m.')
print()
