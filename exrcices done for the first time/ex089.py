# Ex089
print(f'\033[7;37m{"BOLETIM":^35}\033[m')
bulletins = []
student = []
cont = 0
while True:
    cont += 1
    student.append(str(input(f'Nome do {cont}° aluno: ').title()))
    student.append(float(input(f'Nota 1: ')))
    student.append(float(input(f'Nota 2: ')))
    while True:
        again = str(input(f'\033[7;37m{"Deseja continuar? [S/N]: ":^35}\033[m')).upper()
        if again == 'S' or again == 'N':
            bulletins.append(student[:])
            student.clear()
            break
        else:
            print(f'\033[7;31m{"COMANDO INVÁLIDO, TENTE NOVAMENTE!":^35}\033[m')
    if again == 'N':
        break
print(f'\033[32m{"N°":<5}\033[m{"Nome":<20}\033[32m{"Média":>10}\033[m')
cont2 = 0
cont3 = 0
average = 0
while True:
    cont3 = 0
    print(f'\033[32m{f"{cont2 + 1}":<5}\033[m', end='')
    print(f'\033[m{f"{bulletins[cont2][cont3]}":<20}\033[m', end='')
    nota1 = bulletins[cont2][cont3 + 1]
    nota2 = bulletins[cont2][cont3 + 2]
    average = (nota1 + nota2) / 2
    print(f'\033[32m{f"{average}":>10}\033[m')
    cont2 += 1
    media = 0
    if cont2 == len(bulletins):
        break
print(f'\033[7;31m{"Digite 999 para encerrar":^35}\033[m')
while True:
    while True:
        student = int(input(f'\033[7;37m{"Mostrar notas de qual aluno? ":^35}\033[m'))
        if student <= len(bulletins) or student == 999:
            break
    if student == 999:
        break
    print(f'{f"Notas de {bulletins[student - 1][0]}:":<20}{f"{bulletins[student - 1][1:]}":>15}')
print(f'\033[7;37m{"VOLTE SEMPRE! xD":^35}\033[m')
