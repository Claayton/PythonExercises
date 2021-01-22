#Ex012.2
#Faça um algoritmo que leia o preço de um produto, e mostre seu novo preço com 5% de desconto.

price = float(input('What is the product price?: '))
new_price = price - (price * 5 / 100)
print(f'The product that coast R$: {price:.2f}')
print(f'Will now coast R$: {new_price:.2f} with 5% discount')
