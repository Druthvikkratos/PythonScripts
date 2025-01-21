import pandas as pd

data = {
    "Store_Id":[1,1, 2, 1, 2, 3, 1,2, 3, 1,2, 3],
    "Date":["2024-01-01","2024-01-01","2024-01-01","2024-01-02","2024-01-02","2024-01-02",
            "2024-01-03","2024-01-03","2024-01-03","2024-01-04","2024-01-04","2024-01-04"],
    "Product_Category":["Electronics","Clothing","Electronics","Food","Clothing", "Electronics",
                        "Food", "Electronics","Clothing","Electronics","Food", "Clothing"],
    "Sales_Amount":[850.99, 120.50, 1200.00, 75.25, 200.00, 950.50, 45.75, 1500.25, 175.00,
                    725.00, 125.75, 899.99],
    "Units_Sold":[2,3,3,5,4,2,3,4,5,1,8,2],
     "Customer_Age":[34,28,45,22,31,29,55,41,33,38,26,47],
    "Customer_Gender":["M", "F", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
    "Promotion_Active":[True, False,True,False,True,False,False,True,True,
                       False,True,True ]

}

df = pd.DataFrame(data)
df.to_csv("salesdata.csv", index=False)
print("CSV data created successfully")
dp = pd.read_csv("salesdata.csv")
row = dp.shape[0]
column = dp.shape[1]

#print length of rows and columns
print("Rows: ", row)  
print("Columns: ", column)  

#print unique values from selected column
unique = dp['Product_Category']
print(unique.unique())

#calculate average sales amt of all transactions
getSalesAmt = dp["Sales_Amount"]
#method 1:
sumOfSakesAmt = getSalesAmt.sum()
average = sumOfSakesAmt / len(getSalesAmt)
print(average)
#method2:
print(getSalesAmt.mean())

#What is the total sales amount per store?
total_by_store = dp.groupby('Store_Id')['Sales_Amount'].sum()
print(total_by_store)

# Find the average number of units sold by product category.
avg_by_product_category = dp.groupby('Product_Category')['Units_Sold'].mean().to_frame('Average units')
avg_by_product_category = dp.groupby('Product_Category').agg({'Units_Sold': 'mean'})
print(avg_by_product_category)

#Calculate the total sales for each day.
tot_sales_of_each_day = dp.groupby('Date')['Sales_Amount'].sum().to_frame('Total Sales')
print(tot_sales_of_each_day)


# Show only transactions where promotion was active.
onlyTrue = dp['Promotion_Active'] == True
print(dp[onlyTrue])

#Find all electronics sales over $1000.
electronics = dp['Product_Category'] == 'Electronics'
sales = dp['Sales_Amount'] > 1000
combined = dp[electronics & sales]
print(combined)


#Get transactions where customers are younger than 30.
getTransactions = dp['Sales_Amount']
getAges = dp['Customer_Age'] < 30
combined = dp[(dp['Customer_Age'] < 30) & dp['Sales_Amount']]
print(combined)

#What's the average sales amount by gender and product category?
gender_product_category = dp.groupby(['Product_Category', 'Customer_Gender']).count()
print(dp[gender_product_category])
groupBy = dp.groupby(['Product_Category', 'Customer_Gender'])['Sales_Amount'].mean()
print(groupBy)

#On which date did each store have its highest sales
# Method 1: Using idxmax()
highest_sales_dates = dp.groupby('Store_Id').apply(lambda x: x.loc[x['Sales_Amount'].idxmax(), 'Date'])

# OR Method 2: Using sort_values
highest_sales = dp.sort_values('Sales_Amount').groupby('Store_Id').last()
print(highest_sales)


#Calculate the percentage of total sales that came from promotions.
total_Sales = dp['Sales_Amount'].sum()
onlyTrue = dp['Promotion_Active'] == True
promotions_sales = dp[onlyTrue]['Sales_Amount'].sum()
total_promotion_sales = (promotions_sales/total_Sales) * 100
print(total_promotion_sales)

#Add a new column 'sales_per_unit' by dividing sales_amount by units_sold.
sales_amt = dp['Sales_Amount']
units_sold = dp['Units_Sold']
sales_unit = sales_amt/ units_sold
dp['sales_per_unit'] = sales_unit
dp.to_csv("salesdata.csv", index=False)
print("SuccessFull")


#Find all rows where Store_Id is 2.
store_id = dp['Store_Id'] == 2
print(dp[store_id])

#Filter the rows where Sales_Amount is greater than 500.
sales_amt = dp['Sales_Amount'] > 500
print(dp[sales_amt])

#Get all records where the Customer_Gender is 'F' and the Promotion_Active is True.
gender_f = dp['Customer_Gender'] == 'F'
promotion_active = dp['Promotion_Active'] == True
combine = dp[gender_f & promotion_active]
print(combine)

#Select only the columns Date, Product_Category, and Sales_Amount.
columns = dp[['Date', 'Product_Category', 'Sales_Amount']]
print(columns)

#Find the total Sales_Amount for each Store_Id
total = dp.groupby('Store_Id')['Sales_Amount'].sum()
print(total)

#Get the average Units_Sold for each Product_Category.
average = dp.groupby('Product_Category')['Units_Sold'].mean()
print(average)

#Count the number of transactions for each Customer_Gender.
transaction = dp.groupby('Customer_Gender')['Sales_Amount'].size()
print(transaction)
transaction_counts = dp['Customer_Gender'].value_counts()
print(transaction_counts)

#Calculate the total sales amount (Sales_Amount) on 2024-01-01.
date = dp['Date'] == "2024-01-01"
promotions_sales = dp[date]['Sales_Amount'].sum()
print(promotions_sales)

#Sort the DataFrame by Sales_Amount in descending order.
desc = dp.sort_values('Sales_Amount', ascending=False)
#Reset the index of the DataFrame after sorting.
index = desc.reset_index()
#Set the Date column as the index of the DataFrame.
setindex = index.set_index('Date')
print(setindex)

#Add a new column Is_High_Sales that is True if Sales_Amount is greater than 800, otherwise False.
greater = dp['Sales_Amount'] > 800
dp['High_Sales'] = greater
dp.to_csv("salesdata.csv")
print("Added New Column")

#Create age groups (Young: <30, Adult: 30-45, Senior: >45) and analyze sales patterns.
dp['Age_Group'] = pd.cut(dp['Customer_Age'], bins=[0, 30, 45, 100],labels=["Young", "Adult", "Senior"], right=False)
print(dp[['Customer_Age', 'Age_Group']])

#Pivot the data to see the total Sales_Amount for each Product_Category across different Dates
pivot = dp.pivot_table(values=['Sales_Amount'], index=['Product_Category'], columns=['Date'])
print(pivot)