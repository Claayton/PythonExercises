# Ex093.2
"""Create a program that manages a football player's performance.
The program will read the number of goals scored in each match.
In the end, all will be stored in a dictionary, including the total goals scored during the championship."""

enjoyment = {}

print('\033[35m><\033[m' * 30)
enjoyment['Name'] = str(input("\033[32mPlayer's name: \033[m").title().strip())
matches = int(input(f"\033[32mHow many games {enjoyment['Name']} played: \033[m"))
enjoyment['Gols'] = []
for c in range(0, matches):
    enjoyment['Gols'].append(int(input(f'\033[32mHow many gols in match {c}: \033[m')))
enjoyment['Total'] = sum(enjoyment['Gols'])
print('\033[35m><\033[m' * 30)
print(enjoyment)
print('\033[35m><\033[m' * 30)
for c, i, in enjoyment.items():
    print(f'The field \033[32m{c}\033[m has the values \033[32m{i}\033[m')
print('\033[35m><\033[m' * 30)
print(f"The \033[32m{enjoyment['Name']}\033[m player played \033[32m{matches}\033[m matches")
for c, i in enumerate(enjoyment['Gols']):
    print(f'\033[31m    ->\033[m In match \033[32m{c}\033[m he scored \033[32m{i}\033[m gols')
print(f"It was a total of \033[32m{enjoyment['Total']}\033[m gols.")
print('\033[35m><\033[m' * 30)
print('\033[32mxD\033[m')
