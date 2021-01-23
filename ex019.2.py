#Ex019.2
#Um professor quer sortear um de seus quatro alunos para apagar o quadro.
#Faça um rpograma que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
name1 = str(input('What is the name of the first student?: '))
name2 = str(input('What is the name of the second student?: '))
name3 = str(input('What is the name of the third student?: '))
name4 = str(input('What is the name of the fourth student?: '))
list = [name1, name2, name3, name4]
choice = choice(list)
print(f'The choicen student was {choice}')
