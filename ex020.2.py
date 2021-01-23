#Ex020.2
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos,
#Faça um trabalho que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
name1 = str(input('What the name of the first student?: '))
name2 = str(input('What the name of the second student?: '))
name3 = str(input('What the name of the third student?: '))
name4 = str(input('What the name of the fourth student?: '))
list = [name1, name2, name3, name4]
choice = sorted(list)
print(f'The order drawn was \n{choice}')
