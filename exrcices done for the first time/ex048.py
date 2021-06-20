#Exercíco048
soma = 0 #indica onde deve começar a soma entre os números
cont = 0
for c in range(1, 500 + 1, 2): #repete os números entre 1 e 500, contando de 2 em 2(assim mostrando apenas os impares)
    if c % 3 == 0: #faz com que o programa mostre apenas os números que sao divisiveis por 3
        soma = soma + c #soma os numeros
        cont = cont + 1 #conta quantos números foras somados(eu não quis printar isso, mas fodase)
print('A soma entre todos os números ímpares, entre 1 e 500, múltiplos de 3 é: \033[32m{}\033[m'.format(soma))
print('xD')
