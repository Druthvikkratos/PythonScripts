import pandas as pd # type: ignore

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

file_path = "new_excel_file.xlsx"
df.to_excel(file_path, index=False)
print(f"'{file_path}' has been created and written to.")