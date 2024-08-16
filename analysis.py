import matplotlib.pyplot as plt
import seaborn as sns
import Main as m


# Boxplot for numerical columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=m.customers_df[['customer_id']])
plt.title('Boxplot for customer_id')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Convert the 'datetime' column to datetime format
m.transactions_df['datetime'] = pd.to_datetime(m.transactions_df['datetime'])

# Plot transaction amounts over time
plt.figure(figsize=(12, 6))
plt.plot(m.transactions_df['datetime'], m.transactions_df['price'], marker='o', linestyle='-')
plt.title('Transaction Amounts Over Time')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()