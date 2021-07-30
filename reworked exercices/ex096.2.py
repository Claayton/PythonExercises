# Ex096.2
"""Made a program that has a function called area(), which receives the dimensions of a rectangular terrain (width and length) and shows the area of the terrain."""

def area(width, length):
    return width * length

print('\033[35m--\033[m' * 25)
print(f"\033[34m{'Controle de Terrenos':^20}\033[m")
print('\033[35m--\033[m' * 25)
width = float(input('\033[34mWidth (m): \033[m'))
length = float(input('\033[34mLength (m): \033[m'))
print(f'\033[32mThe surface of a {width} m x {length} m plot is \033[34m{area(width, length)} m²\033[m')
print('\033[35m--\033[m' * 25)
print('\033[35mxD\033[m')
