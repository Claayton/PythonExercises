# Ex090
aluno = {}
print('-' * 30)
aluno['Nome'] = str(input('Nome do aluno: ')).title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-' * 30)
for i, a in aluno.items():
    print(f'{i} é igual a: \033[32m{a}\033[m')
print('-' * 30)
