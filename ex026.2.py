#Ex026.2
#Faça um programa que leia uma frase pelo teclado e mostre,
#Quantas vezes aparece a letra "A",
#Em que posiçao ela aparece pela primeira vez,
#Em que posiçao ela aparece pela ultima vez

sentence = str(input('Type a sentence: ')).strip().upper()
letter_A = sentence.count('A')
print(f'In this sentence there are {letter_A} letters "A"')
print(f'The fist letter "A" is in the position: {sentence.find("A") + 1}')
print(f'The last letter "A" is in the position: {sentence.rfind("A") + 1}')
