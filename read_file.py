file_path = "example.txt"
search_word = "Python"

try:
    with open(file_path, "r") as file:
        found = False
        
        for line_num, line in enumerate(file, 1):
            if search_word in line:
                found = True
                print(f"Word found at line: {line_num}")
                break
        if not found:
                print(f"Word not found in file")
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
