# Ex070.2
"""Create a program that reads the name and price of various products.
The program should ask if the user will continue.
At the end, show:
What is the total spend on the purchase
How many products coast more than R$: 1000.00
What is the cheapest product name"""

cont = 0
cheap_price = 0
cheap_name = ''
more1000 = 0
total = 0
again = ''
print(f'\033[1;32;40m{"BORGOV-STORE":^60}\033[m')
while True:
    if again == 'N':
        break
    cont += 1
    name = str(input('What is the name of the product?: ')).title()
    price = float(input('What is the price of the product?: '))
    while True:
        again = str(input('\033[mDo you want to continue?: ')).upper()
        if again == 'S':
            print(f'\033[1;32m{"":-^60}\033[m')
        elif again == 'N':
            print(f'\033[40m{" ":^60}\033[m')
        if again == 'N' or again == 'S':
            break
    total += price
    if price > 1000:
        more1000 += 1
    if cont == 1:
        cheap_price = price
        cheap_name = name
    if price < cheap_price:
        cheap_price = price
        cheap_name = name
print(f'Total spend os purchase: \033[32mR$: {total:.2f}\033[m')
print(f'Number of products that coast more than R$: 1000.00: \033[32m{more1000}\033[m')
print(f'The cheapest product is \033[32m{cheap_name}\033[m which coast \033[32mR$: {cheap_price:.2f}\033[m')
