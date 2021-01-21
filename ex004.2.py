#Ex004.2
word = input('Type something: ')
print(f'The primitive type of this value is: {type(word)}')
print(f'Only have spaces?: {word.isspace()}')
print(f'It is a number?: {word.isnumeric()}')
print(f'It is alphabetical?: {word.isalpha()}')
print(f'Is in upper case?: {word.isupper()}')
print(f'It is in tiny?: {word.islower()}')
print(f'Is capitalized?: {word.istitle()}')
