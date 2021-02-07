#Ex015.2
"""Write a program that asks the number of kilometers traveled by a rental car and the number of days it was rented,
calculate the price to pay, knowing that the car coast R$60.00 per day, and R$0.15 per km driven"""

days = int(input('For how many days the car was rented?: '))
km = float(input('HOw many Km were run?: '))
total_days = days * 60
total_km = km * 0.15
total = total_days + total_km
print(f'The total payable is R$: {total:.2f}')
