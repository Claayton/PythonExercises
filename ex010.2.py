#Ex010.2
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e mostre quantos dólares ela pode comprar.

money_in_real = float(input('How much money do you have in your wallet?: '))
money_in_dollar = money_in_real / 3.27
print(f'With R${money_in_real:.2f} can you buy US: ${money_in_dollar:.2f}')
