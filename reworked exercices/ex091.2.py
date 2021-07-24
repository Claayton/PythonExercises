# Ex091.2
"""Create a program where 4 players roll a die and have a random result.
Store these results in a dictionary.
At the end, put this dictionary in order, knowing that the winner rolled the highest number on the dice."""

from random import randint
from time import sleep
from operator import itemgetter

results = {}

print(f'\033[1;34;40m{"Playing the dice":^40}\033[m')
for c in range(1, 5):
    results[f'Player {c}'] = randint(1, 6)
for p, d in results.items():
    sleep(0.5)
    print(f'\033[1;32;40m{f"{p} rolled {d} on the dice":<40}\033[m')

sorted_results = sorted(results.items(), key=itemgetter(1), reverse=True)
print(f'\033[1;34;40m{"Player Ranking":^40}\033[m')
for p, d in enumerate(sorted_results):
    sleep(0.5)
    print(f'\033[1;32;40m{f"{p + 1}° place {d[0]} with {d[1]} on the dice":<40}\033[m')
print(f'\033[1;32;40m{"xD":<40}\033[m')
