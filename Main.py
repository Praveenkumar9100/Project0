import json
import pandas as pd

# Reading Customer Data
with open('D:/REV Projects/Project_0/DataSets/customers.json ', 'r') as file:
    customer_data = json.load(file)
customers_df = pd.DataFrame(customer_data)
# print("Customers_Data:")
# print(customers_df)

# Reading Transaction Logs
with open('D:/REV Projects/Project_0/DataSets/transaction_logs.json', 'r') as file:
    transaction_data = json.load(file)
transactions_df = pd.DataFrame(transaction_data)
# print("\nTransaction_Logs:")
# print(transactions_df)


# ----knowing the information of both tables and decription-----
# print("Customer Data Information:")
# print(customers_df.info())

# print("Customer Data Description:")
# print(customers_df.describe(include='all'))

# print("transaction_logs Data Information:")
# print(transactions_df.info())

# print("transaction data Description:")
# print(transactions_df.describe(include='all'))

# knowing missing values in customer data
print("Missing Values in Customer Data:")
print(customers_df.isnull().sum())


print("Missing Values in transaction Data:")
print(transactions_df.isnull().sum())