def half(value, monetary=False):
    result = value / 2
    if monetary:
        return currency(result)
    else:
        return result


def double(value, monetary=False):
    result = value * 2
    if monetary:
        return currency(result)
    else:
        return result


def increase(value, porcentage, monetary=False):
    increase = value * porcentage / 100
    result = value + increase
    if monetary:
        return currency(result)
    else:
        return result


def decrease(value, porcentage, monetary=False):
    increase = value * porcentage / 100
    result = value - increase
    if monetary:
        return currency(result)
    else:
        return result


def currency(value):
    result = f'RS: {value:.2f}'
    result = result.replace('.', ',')
    return result

def summary(value, increases, decreases):
    print("\033[34m<>\033[m" * 21)
    print(f"{'VALUE SUMMARY':^40}")
    print("\033[34m<>\033[m" * 21)
    print(f"{'Analysed price:':.<30}\033[32m{currency(value):>10}\033[m")
    print(f"{'Double the price:':.<30}\033[32m{double(value, True):>10}\033[m")
    print(f"{'Half-price:':.<30}\033[32m{half(value, True):>10}\033[m")
    print(f"{f'{increases}% increase':.<30}\033[32m{increase(value, increases, True):>10}\033[m")
    print(f"{f'{decreases}% reduction':.<30}\033[32m{decrease(value, decreases, True):>10}\033[m")
    print("\033[34m<>\033[m" * 21)

