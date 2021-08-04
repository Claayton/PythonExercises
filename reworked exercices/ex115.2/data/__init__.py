def readint(message):
    import design
    while True:
        number = str(input(message))
        if number.isnumeric():
            number = int(number)
            break
        else:
            design.header('INVALID COMMAND, ENTER A VALID NUMBER!', design.paint(8))
    return number


def file_exists(file):
    try:
        a = open(file, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        print(f'File {file} does not exist!, creating...')
        return False

def create_file(file):
    try:
        a = open(file, 'wt+')
        a.close()
        print(f'{file} file created successfully!')
    except FileNotFoundError:
        print(f'Error creating file!')


def read_record(text_file):
    import design
    with open(text_file, 'rt') as file:
        for e in file:
            e= e.replace('\n', '')
            e = e.split(';')
            print(f'{e[0]:<30}{e[1]:>5}{"anos":>5}')
        design.header(' ', design.paint(9))

def register_person(text_file, name, age):
    import design
    with open(text_file, 'at') as file:
        file.write(f'{name};{age}\n')
    design.header('REGISTERED SECCESSFULLY!', design.paint(7))
