#Exercício069
maior18 = homens = womanmenos20 = 0
while True: #Realiza a repetição para continuar a cadastrar pessoas
    print('\033[31m-------------------')
    print('\033[32mCADASTRE UMA PESSOA')
    print('\033[31m-------------------')
    while True: #Realiza a repetição apenas para o caso do usuário digitar uma idade impossível
        age = int(input('\033[32mIdade: \033[m'))
        if age < 150: #Se a idade for menor que 150 interrompe a repetição
            break
    while True: #Realiza a repetição apenas para o caso do usuário errar a digitação
        sex = str(input('\033[32mSexo [M/F]: \033[m')).strip().upper()[0]
        if sex == 'M' or sex == 'F': #Se sexo for igual a 'M' ou 'F', interrompe a repetição
            break
    if age >= 18: #Se idade for maior ou igual a 18 soma mais 1
        maior18 += 1
    if sex == 'M': #Se for homem soma mais 1
        homens += 1
    if sex == 'F' and age < 20: #Se for mulher menor de 18 soma mais 1
        womanmenos20 += 1
    while True: #Realiza a repetição apenas para o caso do usuário errar a digitação
        continua = str(input('\033[31mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
        if continua == 'S' or continua == 'N': #Se usuário digitar certo, interrompe a repetição
            break
    if continua == 'N': #Se usuário não quiser continuar interrompe a repetição, caso contrario continua
        break
print('\033[31m-------------------')
print('\033[32mCADASTROS CONCLUÍDOS')
print(f'\033[32mForam cadastrados {maior18} pessoa(s) maior(es) de 18 anos')
print(f'\033[32mForam cadastrados {homens} homem(ns)')
print(f'\033[32mForam cadastradas {womanmenos20} mulher(es) com menos de 20 anos')
print('\033[32mxD\033[m')
