# Ex102
"""Create a program that has a factorial() function that takes two parameters :
The first one that indicates the number to calculate and the other one called show, which will be a logical value (optional) indicating whether or not the factorial calculation process will be shown on the screen."""

def factorial(number, show=False):
    """
    -> Caculate the factorial of a number.
    :param number: The number to be calculated.
    :param show: (Optional) Show or not the calculation process.
    :return: The factorial valeu of a number.
    """
    factorial = 1
    init = number
    print('\033[35m--\033[m' * 20)
    if show:
        while init != 1:
            factorial *= init
            init -= 1
            print(f"\033[31m{init}\033[m", end=' x ' if init != 1 else ' = ')
    else:
        while init != 1:
            factorial *= init
            init -= 1
    return f'\033[32m{factorial}\033[m\n\033[35m{"--"* 20}\033[m'

print(factorial(5, True))
# Help(factorial)
print('xD')
