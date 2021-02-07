#Ex008.2
"""Write a program that read a value in meters, and displays it converted to centimeters and millimeters"""

meters = int(input('Enter a distance in meters: '))
quilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
milimeters = meters * 1000
print(f'{meters} meters is equals to: ')
print(f'{quilometers} km')
print(f'{hectometers} hm')
print(f'{decameters} dam')
print(f'{decimeters} dm')
print(f'{centimeters} cm')
print(f'{milimeters} mm')
