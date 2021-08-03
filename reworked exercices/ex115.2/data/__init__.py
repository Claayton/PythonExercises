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

