# Ex084.2
"""Make a program that reads names and weights of several people, saving everything in a list.
At the end, show:
A - How many people were registered.
B - A list with the heaviest people.
C - A listing with the lighter people."""

people = []
each = []
again = 'S'
cont = 0

print('\033[31m=\033[m' * 50)
while again != 'N':
    cont += 1
    name = str(input(f'\033[36mEnter the name of the {cont}° people: \033[m')).capitalize()
    each.append(name)
    weight = float(input(f'\033[36mEnter the float of the {cont}° people: \033[m'))
    each.append(weight)
    people.append(each[:])
    each.clear()
    while True:
        again = str(input('\033[32mDo you want to continue? \033[34m[S/N]: \033[m')).upper().strip()
        if again == 'S' or again == 'N':
            break
        else:
            print('\033[31mINVALID COMMAND, TRY AGAIN!\033[m')
print('\033[31m=\033[m' * 50)
print(f'\033[36mIn all you registered \033[32m{cont} people.\033[m')
heighest = 0
lowest = 0
cont = 0
for w in people:
    if cont == 0:
        heighest = w[1]
        lowest = w[1]
    if w[1] > heighest:
        heighest = w[1]
    if w[1] < lowest:
        lowest = w[1]
    cont +=1

people_heighest = []
people_lowest = []
for e in people:
    if e[1] == heighest:
        people_heighest.append(e[0])
    if e[1] == lowest:
        people_lowest.append(e[0])

print(f'\033[36mThe heighest weight was \033[32m{heighest} kg\033[36m, weight of\033[32m', end=' | ')
for c in people_heighest:
    print(f'{c}', end=' | ')
print()
print(f'\033[36mThe lowest weight was \033[32m{lowest} kg\033[36m, weight of\033[32m', end=' | ')
for c in people_lowest:
    print(f'{c}', end=' | ')
print()
print('\033[31m=\033[m' * 50)
print('\033[36mxD\033[m')
