def half(value):
    result = value / 2
    return result


def double(value):
    result = value * 2
    return result


def increase(value, porcentage):
    increase = value * porcentage / 100
    result = value + increase
    return result


def decrease(value, porcentage):
    increase = value * porcentage / 100
    result = value - increase
    return result


def currency(value):
    result = f'RS: {value:.2f}'
    result.replace('.', ',')
    return result