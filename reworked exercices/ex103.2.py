# Ex103.2
"""Make a program that has a function called token(), which takes two optional parameters: a player's name and how many goals he scored.
The program must be able to show the player's record, even if some data has not been entered correctly."""

def token(name='<default>', gol='0'):
    print('\033[35m--\033[m' * 25)
    if not name:
        name = '<default>'
    if not gol.isnumeric() or not gol:
        gol = 0
    return f'\033[31m{name}\033[m player scored \033[31m{gol}\033[m gol(s) in the championship.\nxD\n\033[35m{"--"* 25}\033[m'


print('\033[35m--\033[m' * 25)
player = str(input("Player's name: ").title().strip())
gols = str(input('Goal number: '))

print(token(player, gols))
