# Ex046.2
"""Make a program that shows on the screen a countdown to the fireworks burst,
Going from 10 to 0 with a pause of 1 second between them"""

from time import sleep
import emoji
for counting in range(10, 0 - 1, - 1):
    print(counting)
    sleep(1)
print(emoji.emojize(":boom::boom::boom::boom::boom::boom:", use_aliases=True))
print('FIREWORKS!!!')
print(emoji.emojize(":boom::boom::boom::boom::boom::boom:", use_aliases=True))
