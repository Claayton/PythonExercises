#Ex022.2
#Crie um rpograma que leia um nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas e minusculas
#Quantas letras tem o nome sem considerar os espaços
#Quantas letras tem o primeiro nome

from time import sleep
name = str(input('Enter your full name: ')).strip()
#O codigo a seguir faz uma pequena animaçaozinha com se estivesse carregando as informaçoes
print('Analyzing name.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.'), sleep(0.1)

print(f'It is name in upper case is: {name.upper()}')
print(f'It is name in lower case is: {name.lower()}')
name_clean = name.replace(" ", "") #Retira todos os espaços da frase, ou no caso do nome
print(f'Your name has {len(name_clean)} letters')
name_clean = name.split() #Separa a frase (no caso o nome) por palavra
name_clean = name_clean[0] #Seleciona apenas a primeira palavra do nome
print(f'Your first name is {name_clean.title()} and he has {len(name_clean)} letters')
