# Ex080
values = []
for v in range(0, 5):
    number = int(input('Digite um valor: '))
    if v == 0:
        values.append(number)
        print(f'Valor {number} adicionado ao fim da lista')
    else:
        for p, c in enumerate(values):
            if number >= c:
                if c == values[-1]:
                    values.append(number)
                    print(f'Valor {number} adicionado ao fim da lista')
                    break
                elif number <= values[p + 1]:
                    values.insert(p + 1, number)
                    print(f'Valor {number} adicionado na posição {p + 1}')
                    break
            else:
                values.insert(0, number)
                print(f'Valor {number} adicionado ao início da lista')
                break
print('-' * 45)
print(f'Os valores digitados foram: \033[32m{values}\033[m')
