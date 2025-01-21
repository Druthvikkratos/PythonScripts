import os

old_file_name = 'new_file.txt'
new_file_name = 'new_file_renamed.txt'

try:
    os.rename(old_file_name, new_file_name)
    print(f"File renamed successfully from {old_file_name} to {new_file_name}")
except FileNotFoundError:
    print(f"File not found at path: {old_file_name}")