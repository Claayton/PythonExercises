#Ex015.2
#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado
#E a quantidade de dias pelos quais ele foi alugado,
#Calcule o preço a pagar, sabendo que o carro custa R$60.00, por dia e R$0.15 por Km rodado.

days = int(input('For how many days the car was rented?: '))
km = float(input('HOw many Km were run?: '))
total_days = days * 60
total_km = km * 0.15
total = total_days + total_km
print(f'The total payable is R$: {total:.2f}')
