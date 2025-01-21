file_path = 'new_file.txt'

with open(file_path, 'a') as file:
    file.write('This is a new line\n')
    file.write('This is another new line\n')
    file.write('This is the last line\n')