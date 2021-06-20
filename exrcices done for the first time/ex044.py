#Exercício044
preco = float(input('Preço do produto: '))
print('1 _ à vista_ dinheiro ou cheque\n2 _ à vista_ cartão\n3 _ em até 2x no cartão\n4 _ 3x ou mais no cartão')
condicao = float(input('SELECIONE SUA CONDIÇÃO DE PAGAMENTO: '))
if condicao == 1:
    print('Você tem 10% de desconto, por isso vai pagar R$: {:.2f}'.format(preco - (preco * 10/100)))
elif condicao == 2:
    print('Você tem 5% de desconto, por isso vai pagar R$: {:.2f}'.format(preco - (preco * 5/100)))
elif condicao == 3:
    print('Você vai pagar em 2x no cartão\nPor isso pagará 2x de:\nR$: {:.2f}, no total: R$: {:.2f}'.format(preco/2, preco))
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas pretende pagar: '))
    print('Você vai pagar em {}x e tera 20% de juros'.format(parcelas))
    print('Por isso pagará {}x de R$: {:.2f}, no total: R$: {:.2f}'.format(parcelas, ((preco+(preco*20/100))/parcelas), preco+(preco*20/100)))
else:
    print('OPÇÃO DE PAGAMENTO INVÁLIDA')
print('xD')
