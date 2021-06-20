#Exercício061
termo = int(input('\033[34mDigite o primeiro termo de uma PA: \033[m'))
razao = int(input('\033[34mDigite a razão dessa PA: \033[m'))
contador = 0
print('\033[34mOs 10 primeiros termos dessa PA são: ')
resultado = termo + razao #Soma o termo com a razão pela primeira vez e já mostra na tela
print('\033[32m{} \033[31m-> \033[32m{}'.format(termo, resultado), end=' \033[31m-> ')
while contador != 10 - 2: #Indica para realizar a repetição até '10', (-2 pq os primeiros 2 termos já apareceram antes)
    contador += 1 #Realiza a contagem para determinar a hora de parar
    resultado += razao #Realiza a soma de cada termo e ja mostra na tela 1 por 1
    print('\033[32m{}'.format(resultado), end=' \033[31m-> ')
print('\033[32mACABOU')
print('\033[34mxD\033[m')
