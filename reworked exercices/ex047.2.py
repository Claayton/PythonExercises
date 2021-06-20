# Ex047.2
"""Create a program that shows on the screen all the even numbers that are in the interval between 1 and 50."""

for even in range(0, 51, 2):
    print(even, end='\033[31m->\033[m')
print('THE END')
