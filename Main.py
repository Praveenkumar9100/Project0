import json
import pandas as pd

# Reading Customer Data
with open('D:/REV Projects/Project_0/DataSets/customers.json ', 'r') as file:
    customer_data = json.load(file)
customers_df = pd.DataFrame(customer_data)
print("Customers_Data:")
print(customers_df)

# Reading Transaction Logs
with open('D:/REV Projects/Project_0/DataSets/transaction_logs.json', 'r') as file:
    transaction_data = json.load(file)
transactions_df = pd.DataFrame(transaction_data)
print("\nTransaction_Logs:")
print(transactions_df)