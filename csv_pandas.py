import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("example_pandas.csv", index=False)
print("CSV file created with pandas.")

dp = pd.read_csv("example_pandas.csv")

new_data = {"Name": "David", "Age": 40, "City": "Houston"}
dp = pd.concat([dp, new_data], ignore_index=True)

dp.to_csv("example_pandas.csv", index=False)
print("CSV file updated with pandas.")
