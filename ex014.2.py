#Ex014.2
#Escreva um programa que converta uma temperatura digitada, de °C para °F.

temperature = float(input('Inform the temperature in °C: '))
new_temperature = (temperature * 9 / 5) + 32
print(f'The temperature of {temperature}°C is equivalent to {new_temperature}°F')
