#Exercício015
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos com o carro? '))
diaria = dias*60
kmr = km*0.15
preço = diaria+kmr
print('Se você alugou o carro por {} dias, e andou {} km\nO valor final a pagar será: R$: {:.2f}.'.format(dias, km, preço))
print('xD')
