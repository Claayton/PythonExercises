#Exercício050
soma = 0 #indica qual o primeiro número a ser somado
for c in range(0, 5 + 1): #indica quantas vezes deve se repetir a sequencia
    lista = (c + 1) #indica a sequencia do número que você deve digitar
    valor = int(input('Digite seu {}° número: '.format(lista)))
    if valor % 2 == 0: #seleciona entre os números digitados apenas os multiplos de 2 (ímpares)
        soma = soma + valor #soma os valores
print('A soma dentre os números pares que você digitou é {}, os números ímpares foram desconsiderados.'.format(soma))
print('xD')
