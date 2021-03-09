# Ex071.2
"""Create a program that simulates the functioning of an ATM.
At the beginning, ask the user what will be the amount to be withdraw (whole number)
And the program will inform how many bills of each amount will be delivered.
NOTE: Consider that the cashier has bills of R$50, R$20, R$10, R$1."""

banknote = 50
cont50 = 0
cont20 = 0
cont10 = 0
cont01 = 0
note50 = 0
note20 = 0
note10 = 0
note01 = 0
print(f'\033[7m{"GRINGOTTS-BANK":^45}\033[m')
amount = float(input('What amount do you want to withdraw?: \033[32m'))
while True:
    if amount == 0:
        print(f'\033[m\033[7m{" ":^45}\033[m')
        break
    if amount >= 50:
        amount -= 50
        banknote = 50
        cont50 += 1
        note50 += 50
    elif amount >= 20:
        amount -= 20
        banknote = 20
        cont20 += 1
        note20 += 20
    elif amount >= 10:
        amount -= 10
        banknote = 10
        cont10 += 1
        note10 += 10
    elif amount >= 1:
        amount -= 1
        banknote = 1
        cont01 += 1
        note01 += 1
total = note50 + note20 + note10 + note01
print(f'Banknote(s) of R$: 50.00: \033[32m{cont50:.>19}\033[m')
print(f'Banknote(s) of R$: 20.00: \033[32m{cont20:.>19}\033[m')
print(f'Banknote(s) of R$: 10.00: \033[32m{cont10:.>19}\033[m')
print(f'Banknote(s) of R$: 01.00: \033[32m{cont01:.>19}\033[m')
print(f'\033[32m{"TOTAL":.<25}{total:.>20.2f}\033[m')
print(f'\033[7m{"Thanks for using, always come back":^45}\033[m')
