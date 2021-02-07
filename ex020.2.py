#Ex020.2
"""The same teacher from the previous challenge wants to draw the order of presentation of the student's works,
do a job that reads the names of the four students and shows the order draw"""

import random
name1 = str(input('What the name of the first student?: '))
name2 = str(input('What the name of the second student?: '))
name3 = str(input('What the name of the third student?: '))
name4 = str(input('What the name of the fourth student?: '))
list = [name1, name2, name3, name4]
choice = sorted(list)
print(f'The order drawn was \n{choice}')
