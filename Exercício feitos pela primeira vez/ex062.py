#Exercício062
termo = int(input('\033[34mDigite o primeiro termo de uma PA: \033[m'))
razao = int(input('\033[34mDigite a razão dessa PA: \033[m'))
contador = 0
contador2 = 0
contador3 = 0
print('\033[34mOs 10 primeiros termos dessa PA são: ')
resultado = termo + razao #Soma o termo com a razão pela primeira vez e já mostra na tela
print('\033[32m{} \033[31m-> \033[32m{}'.format(termo, resultado), end=' \033[31m-> ')
while contador != 10 - 2: #Indica para realizar a repetição até '10', (-2 pq os primeiros 2 termos já apareceram antes)
    contador += 1 #Realiza a contagem para determinar a hora de parar
    resultado += razao #Realiza a soma de cada termo e já mostra na tela 1 por 1
    print('\033[32m{}'.format(resultado), end=' \033[31m-> ')
mostramais = int(input('Quer ver mais quantos termos?: '))
while mostramais != 0: #Continua perguntando se quer mais termos até que seja digitado o '0'
    contador2 = 0 #Determina a nova repetição de acordo com a escolha de quantos termos a mais
    while contador2 != mostramais: #Repete a quantidade de termos a mais forem escolhidas
        contador2 += 1 #Realiza a nova contagem de termos a mais
        resultado += razao #Realiza a soma dos termos a mais e já mostra na tela 1 por 1
        print('\033[32m{}'.format(resultado), end=' \033[31m-> ')
    contador3 +=contador2 #Conta quantos termos foram mostrados na segunda onda
    mostramais = int(input('Quer ver mais quantos termos?: '))
print('\033[32mPA finalizada com o total de {} termos'.format(contador + contador3 + 2))
print('\033[34mxD\033[m')
