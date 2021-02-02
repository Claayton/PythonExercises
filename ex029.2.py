#Ex029.2
#Escreva um programa que leia a velocidade de um carro,
#Se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado,
#A multa vai custar R$7.00 por cada km acima do limite
print('=-'*15)
print('\033[31mRADAR MINHA MULTA MINHA VIDA, SPEED LIMIT: 80Km/h\033[m')
print('=-'*15)
speed = float(input('What is de current speed of the car?: '))
if speed > 80:
    print(f'\033[31mYOU WERE FINED! the amount of the fine is: R$: {(speed - 80) * 7:.2f}\033[m')
else:
    print('\033[32mYou are within the speed limit')
print('\033[32mHave a nice day, and drive safely\033[m')
