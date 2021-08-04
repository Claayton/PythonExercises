# Ex115.2
"""Create a small modularized system that allows you to register people by name and age in a simple text file.
The system will only have 2 options: register a new person and list all registered people."""
import design, data
from time import sleep

archive = 'cursoemvdeoex115.txt'
if not data.file_exists(archive):
    data.create_file(archive)

while True:
    menu = design.menu()
    if menu == 1:
        design.header('REGISTERED PEOPLE', design.paint(9))
        data.read_record(archive)
        sleep(1)
    elif menu == 2:
        design.header('NEW RECORD', design.paint(9))
        name = str(input(f'{design.paint(5)}Name: {design.paint()}').title().strip())
        age = data.readint(f'{design.paint(5)}Age: {design.paint()}')
        data.register_person(archive, name, age)
        sleep(1)
    elif menu == 3:
        design.header('THANKS FOR USING! BYE!', design.paint(7))
        sleep(1)
        break
design.header('xD', design.paint(7))
