# Ex094
lista_de_pessoas = []
total_de_idade = 0
again = 'S'
cont = 0

while True:
    cont += 1
    lista_de_pessoas.append({})
    lista_de_pessoas[cont - 1]['Nome'] = str(input('Nome: ')).title().strip()
    while True:
        lista_de_pessoas[cont - 1]['Sexo'] = str(input('Sexo [F/M]: ')).upper().strip()
        if lista_de_pessoas[cont - 1]['Sexo'][0] in 'MF':
            break
        else:
            print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
    lista_de_pessoas[cont - 1]['Idade'] = int(input('Idade: '))
    total_de_idade += lista_de_pessoas[cont - 1]['Idade']
    while True:
        again = str(input('\033[32mVocê quer cadastrar mais alguém? [S/N]: \033[m')).upper().strip()
        if again != 'N' and again != 'S':
            print('\033[31mCOMANDO INVÁLIDO, TENTE NOVAMENTE!\033[m')
        if again == 'S' or again == 'N':
            break
    if again == 'N':
        break
media_de_idade = total_de_idade/cont
print('=' * 40)
print(f'\033[34mForam cadastradas \033[32m{cont}\033[34m pessoas\033[m.')
print(f'\033[34mA média de idade do grupo de pessoas é \033[32m{media_de_idade:.2f}\033[m.')
print('\033[34mAs Mulheres cadastradas foram: \033[m')
for c in lista_de_pessoas:
    if c['Sexo'] == 'F':
        print(f'    \033[32m=>\033[m{c["Nome"]}', end='.')
        print()
print('\033[34mAs pessoas cadastradas com a idade acima da média foram: \033[m')
for c in lista_de_pessoas:
    if c['Idade'] >= media_de_idade:
        print(f'    \033[32m=>\033[m{c["Nome"]}', end='\033[32m=>\033[m')
        print()
print('=' * 40)
