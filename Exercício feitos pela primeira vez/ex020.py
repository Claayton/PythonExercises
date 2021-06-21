#Exercício020
import random
aluno1 = str(input('Qual o nome do aluno 1?: '))
aluno2 = str(input('Qual o nome do aluno 2?: '))
aluno3 = str(input('Qual o nome do aluno 3?: '))
aluno4 = str(input('Qual o nome do aluno 4?: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem sorteada para apresentação dos trabalhos dos alunos é: {}'.format(lista))
print('xD')
