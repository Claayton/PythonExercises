# Ex094.2
"""Create a program that reads multiple people's names, gendersm and ages, stores each person's data in a dictionary, and all dictionaries in a list.
At the end show:
A - How many people registered
B - The average age
C - A list of womem
D - An above-average age list."""

people_list = []
people = {}
cont = 0
sum_age = 0

print('\033[35m><\033[m' * 30)
while True:
    name = str(input('\033[34mName: \033[m').title().strip())
    people['Name'] = name
    while True:
        gender = str(input('\033[34mGender \033[36m[M/F]\033[34m: \033[m').upper().strip())
        if gender == 'M' or gender == 'F':
            break
        else:
            print('\033[31mINVÁLID COMAND, TRY AGAIN! [M/F]\033[m')
    people['Gender'] = gender
    age = int(input('\033[34mAge: \033[m'))
    sum_age += age
    people['Age'] = age
    people_list.append(people.copy())
    cont += 1
    people.clear()
    while True:
        again = str(input('\033[34mDo you want to continue?\033[36m[S/N]\033[34m: \033[m').upper().strip())
        if again == 'S' or again == 'N':
            print('\033[35m><\033[m' * 30)
            break
        else:
            print('\033[31mINVÁLID COMAND, TRY AGAIN! [S/N]\033[m')
    if again == 'N':
        break
average = sum_age/cont
print(f'\033[31mA - \033[mIn all we have \033[36m{cont}\033[m people registered.')
print(f'\033[31mB - \033[mThe average age is \033[36m{average}\033[m years old.')
print(f'\033[31mC - \033[mThe women registered were: ', end=' \033[31m-\033[m ')
for c in people_list:
    if c['Gender'] == 'F':
        print(f"\033[36m{c['Name']}\033[m", end=' \033[31m-\033[m ')
print()
print(f'\033[31mD - \033[mList od people who are above average:')
for c in people_list:
    if c['Age'] > average:
        print(f"    Name: \033[36m{c['Name']}\033[m - Gender: \033[36m{c['Gender']}\033[m - Age: \033[36m{c['Age']}\033[m")
print('\033[35m><\033[m' * 30)
print('\033[36mxD\033[m')
