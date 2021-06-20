# Ex022.2
"""Create a program that reads a person's full name and show:
The name with all uppercase and lowercase letters
How many letters have the name without considering spaces
How many letters have the first name"""

from time import sleep
name = str(input('Enter your full name: ')).strip()
# The following code shows a small animation, indicating loading
print('Analyzing name.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1)
print('.', end=''), sleep(0.1), print('.', end=''), sleep(0.1), print('.'), sleep(0.1)

print(f'It is name in uppercase is: {name.upper()}')
print(f'It is name in lowercase is: {name.lower()}')
name_clean = name.replace(" ", "") # Remove all the spaces from the sentence
print(f'Your name has {len(name_clean)} letters')
name_clean = name.split() # Separate the sentence by word
name_clean = name_clean[0] # Selects only the first word of the name
print(f'Your first name is {name_clean.title()} and he has {len(name_clean)} letters')
