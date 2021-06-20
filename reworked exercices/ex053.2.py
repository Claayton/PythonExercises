# Ex053.2
"""Create a program that reads any sentence and tells if it is a palindrome, disregarding the spaces"""

phrase = str(input('Type a phrase: ')).strip().upper().replace(' ', '')
num = len(phrase)
inverse = ''
usual = ''
for p in range(0, num):
    usual += (phrase[p])
    inverse += (phrase[- p - 1])
print(f'The inverse of \033[32m{usual}\033[m is \033[32m{inverse}\033[m')
if usual == inverse:
    print('The typed sentence is a palindrome!')
else:
    print('The typed sentence is not a palindrome!')
