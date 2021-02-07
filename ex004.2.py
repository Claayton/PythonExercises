# Ex004.2
"""Make a program that read something on the keyboard, and shows on the screen it's primitive type,
and all the information about it"""

word = input('Type something: ')
print(f'The primitive type of this value is: {type(word)}')
print(f'Only have spaces?: {word.isspace()}')
print(f'It is a number?: {word.isnumeric()}')
print(f'It is alphabetical?: {word.isalpha()}')
print(f'Is in upper case?: {word.isupper()}')
print(f'It is in tiny?: {word.islower()}')
print(f'Is capitalized?: {word.istitle()}')
