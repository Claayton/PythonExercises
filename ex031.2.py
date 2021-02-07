# Ex031.2
"""Develop a program that asks the distance of a trip in kilometers,
Calculate the price of the trip, charging R$ 0,50 per km for trips up to 200km, and R$ 0.45 for longer trips"""

distance = float(input('How far is the trip?: '))
if distance <= 200:
    price = 0.50
else:
    price = 0.45
print(f'Your {distance}km trip will cost R$: {price * distance:.2f}')
