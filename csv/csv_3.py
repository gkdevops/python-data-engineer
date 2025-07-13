# Simple Sales CSV Processing

# First, let's create a sample sales CSV file
sales_data = """Date,Product,Price,Quantity
2024-01-01,Laptop,1200,2
2024-01-02,Mouse,25,5
2024-01-03,Keyboard,75,3
2024-01-04,Monitor,300,1
2024-01-05,Laptop,1200,1
2024-01-06,Mouse,25,10
2024-01-07,Keyboard,75,2"""

# Write the CSV file
with open('sales.csv', 'w') as file:
    file.write(sales_data)

print("Created sales.csv file")

# Now let's read and process the CSV file
print("\n=== Reading Sales Data ===")

# Read the CSV file
with open('sales.csv', 'r') as file:
    lines = file.readlines()

# Get the header
header = lines[0].strip().split(',')
print(f"Columns: {header}")

# Process each data row
sales_list = []
for line in lines[1:]:  # Skip header
    data = line.strip().split(',')
    
    # Create a dictionary for each row
    sale = {
        'date': data[0],
        'product': data[1],
        'price': float(data[2]),
        'quantity': int(data[3])
    }
    
    # Calculate total for this sale
    sale['total'] = sale['price'] * sale['quantity']
    
    sales_list.append(sale)

print(f"Loaded {len(sales_list)} sales records")

# Show all sales
print("\n=== All Sales ===")
for sale in sales_list:
    print(f"{sale['date']}: {sale['product']} - ${sale['price']} x {sale['quantity']} = ${sale['total']}")

# Calculate totals
print("\n=== Summary ===")
total_revenue = 0
for sale in sales_list:
    total_revenue += sale['total']

print(f"Total Revenue: ${total_revenue}")
print(f"Number of Sales: {len(sales_list)}")
print(f"Average Sale: ${total_revenue / len(sales_list):.2f}")

# Count products sold
product_count = {}
for sale in sales_list:
    product = sale['product']
    if product in product_count:
        product_count[product] += sale['quantity']
    else:
        product_count[product] = sale['quantity']

print("\n=== Products Sold ===")
for product, count in product_count.items():
    print(f"{product}: {count} units")

# Find best selling product
best_product = None
best_count = 0
for product, count in product_count.items():
    if count > best_count:
        best_product = product
        best_count = count

print(f"\nBest selling product: {best_product} ({best_count} units)")

# Save summary to new file
summary_text = f"""Sales Summary Report
==================
Total Revenue: ${total_revenue}
Number of Sales: {len(sales_list)}
Average Sale: ${total_revenue / len(sales_list):.2f}
Best Selling Product: {best_product} ({best_count} units)
"""

with open('sales_summary.txt', 'w') as file:
    file.write(summary_text)

print("\nSummary saved to sales_summary.txt")
