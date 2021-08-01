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
    result.replace('.', ',')
    return result