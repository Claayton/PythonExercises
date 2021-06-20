# Ex010.2
"""Create a program that reads how much money a person has in their wallet, and shows how much dollars they can buy"""

money_in_real = float(input('How much money do you have in your wallet?: '))
money_in_dollar = money_in_real / 3.27
print(f'With R${money_in_real:.2f} can you buy US: ${money_in_dollar:.2f}')
