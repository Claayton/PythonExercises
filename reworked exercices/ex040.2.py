# Ex040.2
"""Create a program that reads two grades from a student and calculates their average,
Showing a message at the end, according to the average reached:
Average below 5.0: FAIL
Average between 5.0 and 6.9: RECOVERY
average 7.0 or higher: APPROVED"""

first_note = float(input('First note: '))
second_note = float(input('Second note: '))
average = (first_note + second_note) / 2
print(f"Apart from {first_note:.1f} and {second_note:.1f}, the student's average is {average:.1f}")
if average <= 4.9:
    print('The student is FALLING')
elif 4.9 < average < 6.9:
    print('The student is in RECOVERY')
elif average >= 7.0:
    print('The student is APPROVED')
