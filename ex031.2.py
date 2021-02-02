#Ex031.2
#Desenvolva um programa que pergunte a distância de uma viagem am quilômetros,
#Calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200km, e R$0.45 para viagens mais longas.

distance = float(input('How far is the trip?: '))
if distance <= 200:
    price = 0.50
else:
    price = 0.45
print(f'Your {distance}km trip will cost R$: {price * distance:.2f}')
