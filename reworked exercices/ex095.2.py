# Ex095.2
"""Enhance CHALLENGE 093 to work with multiple players by incluidng a sistem to view each player's achievement details."""

team = []
enjoyment = {}

print('\033[35m><\033[m' * 40)
while True:
    enjoyment['Name'] = str(input("\033[32mPlayer's name: \033[m").title().strip())
    matches = int(input(f"\033[32mHow many games {enjoyment['Name']} played: \033[m"))
    enjoyment['Gols'] = []
    for c in range(0, matches):
        enjoyment['Gols'].append(int(input(f'\033[32mHow many gols in match {c}: \033[m')))
    enjoyment['Total'] = sum(enjoyment['Gols'])
    team.append(enjoyment.copy())
    enjoyment.clear()
    while True:
        again = str(input('\033[34mDo you want to continue?\033[36m[S/N]\033[34m: \033[m').upper().strip())
        if again == 'S' or again == 'N':
            print('\033[35m><\033[m' * 40)
            break
        else:
            print('\033[31mINVÁLID COMAND, TRY AGAIN! [S/N]\033[m')
    if again == 'N':
        break

print(f"\033[34m{'Cod':>5} {'Name':<24}{'Gols':<30}{'Total':<20}\033[m")

print('\033[35m--\033[m' * 40)
for c, i in enumerate(team):
    gols = f'{i["Gols"]}'
    print(f"{c:>5} {i['Name']:<24}{gols:<30}{i['Total']:<20}")
while True:
    print('\033[35m--\033[m' * 40)
    show = int(input("\033[34mShow which player's data? \033[31m[999 to stop]\033[34m: \033[m"))
    if show == 999:
        print('\033[32mOBRIGADO POR UTILIZAR O PROGRAMA, TCHAU!\033[m')
        break
    elif show > len(team) - 1:
        print('\033[31mINVALID COMMAND, ENTER THE PLAYER CODE!\033[m')
    else:
        print(f"\033[31m>   \033[32mLevantamento do jogador \033[34m{team[show]['Name']}\033[32m:\033[m")
        for c, i in enumerate(team[show]['Gols']):
            print(f'\033[31m    >   \033[32mNo jogo \033[34m{c}\033[32m fez \033[34m{i}\033[32m Gols.\033[m')
print('\033[35m><\033[m' * 40)
print('\033[32mxD\033[m')
