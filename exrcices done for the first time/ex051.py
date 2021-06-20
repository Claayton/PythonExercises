#Exercício051
termo = int(input('\033[33mDigite o primeiro termo de uma PA: '))
razao = int(input('\033[33mDigite a razão dessa PA: '))
print('\033[32mOs 10 primeiros termos dessa PA são: \033[m')
for c in range(termo, termo + razao * 10, razao):
    print(c, end='\033[32m -> \033[m')
print('ACABOU')
print('xD')
