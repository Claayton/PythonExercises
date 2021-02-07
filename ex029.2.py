# Ex029.2
"""Write a program that reads the speed of car
If he exceeds the speed of 80km/h, show a message saying that he was fined
The fine will coast R$:7.00 for each km above the limit"""

print('=-'*15)
print('\033[31mRADAR MINHA MULTA MINHA VIDA, SPEED LIMIT: 80Km/h\033[m')
print('=-'*15)
speed = float(input('What is de current speed of the car?: '))
if speed > 80:
    print(f'\033[31mYOU WERE FINED! the amount of the fine is: R$: {(speed - 80) * 7:.2f}\033[m')
else:
    print('\033[32mYou are within the speed limit')
print('\033[32mHave a nice day, and drive safely\033[m')
