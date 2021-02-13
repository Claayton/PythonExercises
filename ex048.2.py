# Ex048.2
"""Make a program that calculate the sum of all odd numbers that are multiples of 3, and are in the range 1 to 500"""

sum = 0
count = 0
for multiples in range(1, 501, 2):
    if multiples % 3 == 0:
        sum += multiples
        count += 1
print(f'The sum of all {count} values is: {sum}')
