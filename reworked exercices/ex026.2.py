# Ex026.2
"""Make a program that reads a sentence from keyboard, and shows
The letters 'A' appears many times
In what positions does she appear for the first time
In what positions does she appear for the last time"""

sentence = str(input('Type a sentence: ')).strip().upper()
letter_A = sentence.count('A')
print(f'In this sentence there are {letter_A} letters "A"')
print(f'The fist letter "A" is in the position: {sentence.find("A") + 1}')
print(f'The last letter "A" is in the position: {sentence.rfind("A") + 1}')
