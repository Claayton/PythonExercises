# Ex083.2
"""Create a program where the user types any espression that uses parentheses.
Your application should analyze where the expression passed has open and closed parentheses in the correct order."""

list = []
temp = []

expression = str(input('\033[32mType a expression: \033[m'))
for c in expression:
    if c == '(':
        temp.append(c)
    if c == ')':
        temp.append(c)
if len(temp) % 2 == 0:
    print('\033[34mYour expression is \033[32mVALID!\033[m')
else:
    print('\033[34mYour expression is \033[31mINVALID!\033[m')
print('\033[32mxD\033[m')
