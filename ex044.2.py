# Ex044.2
"""Write a program that calculate the amount to be paid for a product,
considering its normal price and payment condition:
Cash/check: 10% discount
Cash on credit card: 5% discount
Up to 2 x on credit card: normal price
3 x or more on credit card: 20% interest"""

print('-' * 40)
print(f'{"M0Z1S-ST0RE":=^40}')
print('-' * 40)
price = float(input('Purchase price: '))
print('-' * 40)
print(f"""{'PAYMENT METHODS:':=^40}
[ 1 ] - CASH/CHECK
[ 2 ] - CASH ON CREDIT CARD
[ 3 ] - 2X ON CREDIT CARD
[ 4 ] - 3X OR MORE ON CREDIT CARD""")
print('-' * 40)
choice = int(input('What is your choice?: '))
final_purchase = 0
if choice == 1:
    final_purchase = price - (price * 10 / 100)
    print('Payment in cash or check')
    print(f'Your purchase of R$: {price:.2f}, will coast {final_purchase:.2f}')
elif choice == 2:
    final_purchase = price - (price * 5 / 100)
    print('Payment in cash on credit')
    print(f'Your purchase of R$: {price:.2f}, will coast {final_purchase:.2f}')
elif choice == 3:
    final_purchase = price
    print('Payment in 2x on credit card')
    print(f'Your purchase of R$: {price:.2f}, will coast {final_purchase:.2f}')

elif choice == 4:
    final_purchase = price + (price * 20 / 100)
    pair = int(input('how many installments?: '))
    print(f'Payment in {pair}x of R$: {final_purchase / pair:.2f} on credit card')
    print(f'Your purchase of R$: {price:.2f}, will coast {final_purchase:.2f}')
else:
    print('INVALID OPTION')
