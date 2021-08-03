# Ex114.2
"""Create a Python code that tests whether the "pudim.com" site is accessible by the computer being used."""

import requests

try:
    site = requests.get('http://www.pudim.com.br/')
except:
    print('\033[31mAn erro occurred while tryng to access the "pudim.com" website!.\033[m')
else:
    print('\033[32mThe "pudim.com" site is 100% accessible at the moment!\033[m')
