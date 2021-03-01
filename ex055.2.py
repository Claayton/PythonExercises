# Ex055.2
"""Make a program that reads the weight of five people.
At the end, show which was the highest and lowest weight read."""

highest = 0
lowest = 0

for p in range(1, 6):
    weight = float(input(f'What is the weight of the {p}° person?: '))
    highest_weight = weight
    lowest_weight = weight
    if weight > highest_weight:
        highest += 1
        highest_weight = weight
    if weight < lowest_weight:
        lowest += 1
        lowest_weight = weight
print(f'The highest weight is the {highest}° person with {highest_weight:.2f}Kg')
print(f'The lowest weight is the {lowest}° person with {lowest_weight:.2f}Kg')
