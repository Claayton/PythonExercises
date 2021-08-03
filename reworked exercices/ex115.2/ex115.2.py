# Ex115.2
"""Create a small modularized system that allows you to register people by name and age in a simple text file.
The system will only have 2 options: register a new person and list all registered people."""
import design, data

archive = 'cursoemvdeoex115.txt'
if not data.file_exists(archive):
    data.create_file(archive)


design.menu()
