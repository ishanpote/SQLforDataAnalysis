import pandas as pd
import sqlite3

# 1. Load the dataset with the correct encoding
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Clean up column names to make them standard lowercase SQL identifiers
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.lower()

# 2. Normalize data into separate tables to practice JOINs
# Dimension Table: Customers
customers = df[['customer_id', 'customer_name', 'segment', 'country', 'city', 'state', 'postal_code', 'region']].drop_duplicates(subset=['customer_id'])

# Dimension Table: Products
products = df[['product_id', 'category', 'sub_category', 'product_name']].drop_duplicates(subset=['product_id'])

# Fact Table: Orders
orders = df[['row_id', 'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id', 'product_id', 'sales', 'quantity', 'discount', 'profit']]

# 3. Create and connect to the SQLite database file
conn = sqlite3.connect('superstore.db')

# Write the data frames to separate SQL tables
customers.to_sql('customers', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
orders.to_sql('orders', conn, if_exists='replace', index=False)

print("--- Database Setup Successful! ---")
print("Created file: 'superstore.db'")
print(f"Tables loaded: 'orders' ({len(orders)} rows), 'customers' ({len(customers)} rows), 'products' ({len(products)} rows)")

conn.close()