import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

#update file
with open("example1.csv", "r") as file:
    row = list(csv.reader(file))
row.append(["David", 10 , "Australia"])


with open("example1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    #write file directly
    #writer.writerows(data)
    #update file
    writer.writerows(row)
    print("CSV file created successfully.")