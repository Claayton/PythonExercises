# Ex044.2
"""Write a program that calculate the amount to be paid for a product,
considering its normal price and payment condition:
Cash/check: 10% discount
Cash on credit card: 5% discount
Up to 2 x on credit card: normal price
3 x or more on credit card: 20% interest"""

print('\033[7:30:47m-\033[m' * 40)
print(f'\033[7:30:47m{"M0Z1S-ST0RE":=^40}\033[m')
print('\033[7:30:47m-\033[m' * 40)
price = float(input('Purchase price: '))
print(f"""\033[7:30:47m{'PAYMENT METHODS:':=^40}\033[m
\033[30:47m[ 1 ]\033[m - CASH/CHECK
\033[30:47m[ 2 ]\033[m - C\033[mASH ON CREDIT CARD
\033[30:47m[ 3 ]\033[m - 2X ON CREDIT CARD
\033[30:47m[ 4 ]\033[m - 3X OR MORE ON CREDIT CARD""")
print('\033[7:30:47m-\033[m' * 40)
choice = int(input('What is your choice?: '))
print('\033[7:30:47m-\033[m' * 40)
final_purchase = 0
if choice == 1:
    final_purchase = price - (price * 10 / 100)
    print('Payment in cash or check')
    print(f'Your purchase of R$: {price:.2f},\nWill coast R$: {final_purchase:.2f}')
elif choice == 2:
    final_purchase = price - (price * 5 / 100)
    print('Payment in cash on credit')
    print(f'Your purchase of R$: {price:.2f},\nWill coast R$: {final_purchase:.2f}')
elif choice == 3:
    final_purchase = price
    print('Payment in 2x on credit card')
    print(f'Your purchase of R$: {price:.2f},\nWill coast R$: {final_purchase:.2f}')
elif choice == 4:
    final_purchase = price + (price * 20 / 100)
    pair = int(input('how many installments?: '))
    print('\033[7:30:47m-\033[m' * 40)
    print(f'Payment in {pair}x of R$: {final_purchase / pair:.2f} on credit card')
    print(f'Your purchase of R$: {price:.2f},\nWill coast R$: {final_purchase:.2f}')
else:
    print('INVALID OPTION')
