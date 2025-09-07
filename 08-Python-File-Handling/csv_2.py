import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv('sales_basic.csv')

# Basic exploration
print("Dataset shape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))

print("\nData types:")
print(df.dtypes)

# Simple operations
df['total_value'] = df['price'] * df['quantity']
print("\nDataset with calculated total value:")
print(df)

# Basic filtering
expensive_products = df[df['price'] > 700]
print("\nProducts with price > 700:")
print(expensive_products)

# Simple aggregation
total_revenue = df['total_value'].sum()
print(f"\nTotal revenue: ${total_revenue}")