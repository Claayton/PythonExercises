# Ex077.2
"""Create a program that has a tuple with several words (don't use accents).
After that, you must show, for each word, wich are its vowel."""

words = (
    'Learn',
    'Program',
    'Leanguage',
    'Python',
    'Course',
    'Free',
    'Study',
    'Pratice',
    'Work',
    'Marketplace',
    'Programmer',
    'Future'
)

print(f'\033[7m{"VOWES":^60}\033[m')
for w in words:
    print(f'In the word \033[32m{w}\033[m we have the vowes: ', end=' ')
    for e in w:
        if e.lower() in 'aeiou':
            print(f'\033[32m{e}\033[m', end=' ')
    print()
print(f'\033[7m{"xD":^60}\033[m')
