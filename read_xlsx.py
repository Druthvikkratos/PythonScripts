import pandas as pd # type: ignore

file_path = "ganesh.xlsx"

try:
    df = pd.read_excel(file_path)
    print("excel file read successfully")
    print(df)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")   
except Exception as e:
    print(f"An error occurred: {e}")