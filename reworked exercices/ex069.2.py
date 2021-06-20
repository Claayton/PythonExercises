# Ex069.2
"""Create a program that reads the age and sex of several people.
For each registered person, the program must ask if the user wants to continue or not.
At the end show:
How many people are over 18;
How many men were registered;
How many women are under 20."""

again = ''
cont_age18 = 0
cont_men = 0
cont_women20 = 0
cont_total = 0
print(f'\033[1;32;40m{"REGISTER":^30}\033[m')
while True:
    if again == 'N':
        break
    while True:
        age = int(input('\033[mHow old are you?\033[32m: '))
        if age > 18:
            cont_age18 += 1
        if 100 > age > 0:
            break
    while True:
        sex = str(input('\033[mWhat is you gender?: \033[32m')).upper().strip()
        if sex == 'M':
            cont_men += 1
        if sex == 'F' or sex == 'M':
            break
        else:
            print(f'\033[1;32;40m{"INVALID RESPONSE, TRY AGAIN":^30}\033[m')
    if age < 20 and sex == 'F':
        cont_women20 += 1
    cont_total += 1
    while True:
        again = str(input('\033[mDo you want to continue?: ')).upper()
        if again == 'N' or again == 'S':
            if again == 'S':
                print(f'\033[1;32m{"":-^30}\033[m')
            break

print(f'\033[40m{" ":^30}\033[m')
print(f'Of the \033[32m{cont_total}\033[m registered')
print(f'\033[32m{cont_age18}\033[m people are over 18 years old')
print(f'\033[32m{cont_men}\033[m are men')
print(f'\033[32m{cont_women20}\033[m are women under 20 years old')
