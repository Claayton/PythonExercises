# Ex089.2
"""Create a program that reads multiple student's names and two grades and stores them in a composite list.
At the end, show a report containing the average of each one and allow the user to show the grades of each individual student."""

all_grades = []
each_grade = []
again = 'S'

print(f'\033[1;32;40m{"STUDENT NOTES":^50}\033[m')
while again != 'N':
    each_grade.append(str(input('\033[32mName: \033[m').title()))
    each_grade.append(float(input('\033[32mGrade 1: \033[m')))
    each_grade.append(float(input('\033[32mGrade 2: \033[m')))
    all_grades.append(each_grade[:])
    each_grade.clear()
    while True:
        again = str(input('\033[36mDo you want to continue? [S/N]: \033[m')).upper().strip()
        if again == 'S' or again == 'N':
            break
        else:
            print(f'\033[1;30;41m{"INVALID RESPONSE, TRY AGAIN":^50}\033[m')
print(f'\033[1;32;40m{" ":^50}\033[m')
print(f'\033[1;34;40m{"N°":^4}{"Name":<38}{"Average":^8}\033[m')

cont = 0
for grades in all_grades:
    average = (grades[1] + grades[2]) / 2
    print(f'\033[1;35;40m{cont:^4}{grades[0]:<38}{average:^8}\033[m')
    cont += 1
print(f'\033[1;34;40m{"xD":<50}\033[m')

while True:
    show = int(input("\033[36mShow which student's grades? \033[32m([999] interrupts): \033[m"))
    if show == 999:
        print(f'\033[1;32;40m{"OBRIGADOI POR UTILIZAR O PROGRAMA, VOLTE SEMPRE!":^50}\033[m')
        break
    average = (all_grades[show][1] + all_grades[show][2]) / 2
    print(f'\033[1;34;40m{"Name":<20}{"Grade01":^10}{"Grade02":^10}{"Average":^10}\033[m')
    print(f'\033[1;35;40m{all_grades[show][0]:<20}{all_grades[show][1]:^10}{all_grades[show][2]:^10}{average:^10}\033[m')
