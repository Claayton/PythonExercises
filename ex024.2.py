# Ex024.2
"""Create a program that reads the name of a city, and says whether or not it starts with the name 'SANTO'"""

city = str(input('Enter the name of a city: ')).strip().upper()
print('This city starts with "Santo"?: ', end='')
print(city[0:5] == "SANTO")
