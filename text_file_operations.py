import os
input_file = 'opp.txt'
import pandas as pd


if not os.path.exists(input_file):
   with open(input_file, "w") as file:
        file.write("hello \n")
        file.write("how are you \n")
        print("file read successfull")
else:
   with open(input_file, "r") as file:
      content = file.read()
      print("file read successfull")



try:
    with open(input_file, "r") as file:
        content = file.read()
        print(f"file read successfull {content}")
except FileNotFoundError:
    print("file not found creating the file.....")
    with open(input_file, 'w') as file:
        file.write("hello \n")
        file.write("hiii \n")
    print(f"file write success {content}")
    with open(input_file, "r") as file:
        content = file.read()
        print(f"file read successfull {content}")


file_name = 'newfile.xlsx'

data = {'Name': ['Ganesh'],
        'Age': [25]}
ds = pd.DataFrame(data)
try:
    dp= pd.read_excel(file_name)
    print("File Read Successfull")
except FileNotFoundError:
    print("File Not Found Creating the File....")
    ds.to_excel(file_name, index=False)
    print("File Created Successfull")


new_data = pd.DataFrame({
    'Name': ['Sarath'],
    'Age': [27]
})
if os.path.exists(file_name):
    existing_data = pd.read_excel(file_name)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_excel(file_name, index=False)
    print("New Data is appended successfull")
else:
    combined_data = new_data
    combined_data.to_excel(file_name, index=False)
    print("Data appended successfully.")

