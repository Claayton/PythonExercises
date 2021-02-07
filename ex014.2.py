# Ex014.2
"""Write a program that converts a entered temperature, from °C to °F"""

temperature = float(input('Inform the temperature in °C: '))
new_temperature = (temperature * 9 / 5) + 32
print(f'The temperature of {temperature}°C is equivalent to {new_temperature}°F')
