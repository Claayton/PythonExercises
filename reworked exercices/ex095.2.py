# Ex095.2
"""Enhance CHALLENGE 093 to work with multiple players by incluidng a sistem to view each player's achievement details."""

team = []
enjoyment = {}

print('\033[35m><\033[m' * 30)
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
            print('\033[35m><\033[m' * 30)
            break
        else:
            print('\033[31mINVÁLID COMAND, TRY AGAIN! [S/N]\033[m')
    if again == 'N':
        break

# FALTA TERMINAR AINDA

for c, i, in enjoyment.items():
    print(f'The field \033[32m{c}\033[m has the values \033[32m{i}\033[m')
print('\033[35m><\033[m' * 30)
print(f"The \033[32m{enjoyment['Name']}\033[m player played \033[32m{matches}\033[m matches")
for c, i in enumerate(enjoyment['Gols']):
    print(f'\033[31m    ->\033[m In match \033[32m{c}\033[m he scored \033[32m{i}\033[m gols')
print(f"It was a total of \033[32m{enjoyment['Total']}\033[m gols.")
print('\033[35m><\033[m' * 30)
print('\033[32mxD\033[m')