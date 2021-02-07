#Ex013.2
"""Make an algorithm that reads an employee's salary, and shows his new salary with a 15% increase"""

salary = float(input("Type the employee's salary: "))
increase = salary * 15 / 100
print(f"If the employee's salary was R$: {salary:.2f}")
print(f'with a 15% increase, you will receive R$: {salary + increase:.2f}')
