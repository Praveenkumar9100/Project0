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
# print("Missing Values in Customer Data:")
# print(customers_df.isnull().sum())


# print("Missing Values in transaction Data:")
# print(transactions_df.isnull().sum())

# Merging of the both tables

merged_df = pd.merge(transactions_df, customers_df, on='customer_id', how='inner')
# print("Merged DataFrame Info:")
# print(merged_df.info())



#Seperating the tables and connecting to the data base 

from sqlalchemy import create_engine

# Load JSON data
with open('D:/REV Projects/Project_0/DataSets/customers.json', 'r') as file:
    customers_data = json.load(file)
with open('D:/REV Projects/Project_0/DataSets/transaction_logs.json', 'r') as file:
    transactions_data = json.load(file)

# Convert to DataFrames
customers_df = pd.DataFrame(customers_data)
transactions_df = pd.DataFrame(transactions_data)

# Transform Customers DataFrame
customers_df = customers_df[['customer_id', 'customer_name', 'country', 'city']]

# Transform Products DataFrame
products_df = pd.DataFrame({
    'product_id': transactions_df['product_id'].unique(),
    'product_name': transactions_df.drop_duplicates('product_id')['product_name'],
    'product_category': transactions_df.drop_duplicates('product_id')['product_category']
})

# Transform Ecommerce Websites DataFrame
ecommerce_websites_df = pd.DataFrame({
    'website_id': range(len(transactions_df['ecommerce_website_name'].unique())),
    'website_name': transactions_df['ecommerce_website_name'].unique()
})

# Create a mapping from website_name to website_id
website_name_to_id = ecommerce_websites_df.set_index('website_name')['website_id'].to_dict()
transactions_df['website_id'] = transactions_df['ecommerce_website_name'].map(website_name_to_id)

# Transform Transactions DataFrame
transactions_df['datetime'] = pd.to_datetime(transactions_df['datetime'])
transactions_df = transactions_df[['order_id', 'customer_id', 'product_id', 'website_id', 'qty', 'price', 'datetime', 'payment_type', 'payment_txn_id', 'payment_txn_success', 'failure_reason']]

# Create SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:1111@localhost/revp0')

# Insert data into tables
customers_df.to_sql('customers', con=engine, if_exists='replace', index=False)
products_df.to_sql('products', con=engine, if_exists='replace', index=False)
ecommerce_websites_df.to_sql('ecommerce_websites', con=engine, if_exists='replace', index=False)
transactions_df.to_sql('transactions', con=engine, if_exists='replace', index=False)



import mysql.connector

db=mysql.connector.connect(
    host ="localhost",
    user ="root",
    password='1111',
    database="revp0"
) 
cursor=db.cursor()     #cursor used for running the sql queries.
cursor.execute("select *from customers limit 5")
rows=cursor.fetchmany(size=4)
res=cursor.fetchall()
for _ in res:
    print(_)