def readmoney(message):
    while True:
        value = str(input(message).strip())
        value = value.replace(',', '.')
        if value.replace('.', '').isnumeric():
            value = float(value)
            break 
        else:
            print(f"\033[31mError, '{value}' is an invalid price!\033[m")
    return value
