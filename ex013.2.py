#Ex013.2
#Faça um algoritmo que leia o salário de um funcionário, e mostre seu novo salário com 15% de aumento.

salary = float(input("Type the employee's salary: "))
increase = salary * 15 / 100
print(f"If the employee's salary was R$: {salary:.2f}")
print(f'with a 15% increase, you will receive R$: {salary + increase:.2f}')
