# Ex076.2
"""Create a program that has a unique tuple with product names and their prices in sequence.
At the end, show a peice list, organizing the data in tabular form."""

products = (
    'Pencil', 1.75,
    'Rubber', 2,
    'Notebook', 15.90,
    'Pencil Case', 25,
    'Protractor', 4.20,
    'Compass', 9.99,
    'Schoolbag', 120.32,
    'Pens', 22.30,
    'Book', 34.90
)

print(f'\033[7m{"PRE LISTING":^50}\033[m')
cont = 0
for p in products:
    if cont % 2 == 0:
        print(f'{p:.<40}', end='')
    else:
        print(f'R${p:>8.2f}')
    cont += 1    
print(f'\033[7m{"xD":^50}\033[m')
