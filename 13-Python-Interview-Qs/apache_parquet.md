# Apache Parquet: A Comprehensive Guide

## Table of Contents
1. [What is Parquet?](#what-is-parquet)
2. [Why is Parquet Popular?](#why-is-parquet-popular)
3. [Use Cases for Data Engineers](#use-cases-for-data-engineers)
4. [Use Cases for Data Analysts](#use-cases-for-data-analysts)
5. [Comparison: Parquet vs JSON vs CSV](#comparison-parquet-vs-json-vs-csv)
6. [Python Implementation](#python-implementation)
7. [Industry Use Cases](#industry-use-cases)

---

## What is Parquet?

**Apache Parquet** is an open-source, **columnar storage file format** designed for efficient data storage and retrieval. It was developed as part of the Apache Hadoop ecosystem.

### Key Characteristics:
- **Columnar Storage**: Data is stored column by column, not row by row
- **Self-describing**: Schema is embedded within the file
- **Compressed**: Built-in compression support (Snappy, GZIP, LZO, etc.)
- **Splittable**: Can be processed in parallel across distributed systems

---

## Why is Parquet Popular?

```
┌─────────────────────────────────────────────────────────────┐
│                  ROW-BASED vs COLUMNAR                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ROW-BASED (CSV/JSON):                                      │
│  ┌─────┬───────┬─────┬────────┐                            │
│  │ ID  │ Name  │ Age │ Salary │  → Row 1                   │
│  │ ID  │ Name  │ Age │ Salary │  → Row 2                   │
│  │ ID  │ Name  │ Age │ Salary │  → Row 3                   │
│  └─────┴───────┴─────┴────────┘                            │
│                                                             │
│  COLUMNAR (Parquet):                                        │
│  ┌─────┐ ┌───────┐ ┌─────┐ ┌────────┐                      │
│  │ ID  │ │ Name  │ │ Age │ │ Salary │                      │
│  │ ID  │ │ Name  │ │ Age │ │ Salary │                      │
│  │ ID  │ │ Name  │ │ Age │ │ Salary │                      │
│  └─────┘ └───────┘ └─────┘ └────────┘                      │
│    ↓        ↓        ↓        ↓                            │
│  Col 1   Col 2    Col 3    Col 4                           │
└─────────────────────────────────────────────────────────────┘
```

### Reasons for Popularity:

| Benefit | Description |
|---------|-------------|
| **Efficient Compression** | Similar data types stored together compress better (up to 75% smaller) |
| **Column Pruning** | Read only required columns, skip unnecessary data |
| **Predicate Pushdown** | Filter data at storage level before loading into memory |
| **Schema Evolution** | Add, remove, or modify columns without rewriting entire dataset |
| **Big Data Ecosystem** | Native support in Spark, Hive, Presto, AWS Athena, BigQuery |
| **Fast Aggregations** | Analytical queries (SUM, AVG, COUNT) run much faster |

---

## Use Cases for Data Engineers

### 1. **ETL/ELT Pipelines**
```
Raw Data (CSV/JSON) → Transform → Parquet (Data Lake)
```

### 2. **Data Lake Storage**
- Store processed data in cloud storage (S3, GCS, Azure Blob)
- Partitioned storage for efficient querying

### 3. **Data Warehouse Staging**
- Intermediate format between source systems and data warehouse

### 4. **Batch Processing**
- Efficient format for Spark, Hive, and Presto jobs

### 5. **Data Archival**
- Long-term storage with excellent compression

### 6. **Schema Enforcement**
- Enforce data types and schema validation

---

## Use Cases for Data Analysts

### 1. **Fast Analytical Queries**
- Quick aggregations on large datasets

### 2. **Self-Service Analytics**
- Query directly using SQL engines (Athena, Presto, Trino)

### 3. **Reporting Datasets**
- Pre-aggregated data for dashboards

### 4. **Historical Analysis**
- Analyze historical data stored efficiently

### 5. **Ad-hoc Analysis**
- Explore large datasets with tools like DuckDB

---

## Comparison: Parquet vs JSON vs CSV

### Feature Comparison Table

| Feature | Parquet | JSON | CSV |
|---------|---------|------|-----|
| **Storage Format** | Columnar (Binary) | Row-based (Text) | Row-based (Text) |
| **Human Readable** | ❌ No | ✅ Yes | ✅ Yes |
| **File Size** | ⭐ Smallest (70-90% smaller) | Largest | Medium |
| **Compression** | ⭐ Excellent (built-in) | Poor | Moderate |
| **Schema** | ⭐ Embedded & enforced | Flexible/None | None (header only) |
| **Data Types** | ⭐ Rich type support | Limited types | All text (no types) |
| **Nested Data** | ✅ Excellent support | ✅ Native support | ❌ Not supported |
| **Read Speed (Analytics)** | ⭐ Very Fast | Slow | Slow |
| **Write Speed** | Moderate | Fast | Fast |
| **Partial Reading** | ✅ Column selection | ❌ Full file read | ❌ Full file read |
| **Splittable** | ✅ Yes | ❌ No (unless line-delimited) | ✅ Yes |
| **Big Data Tools** | ⭐ Excellent support | Moderate | Moderate |
| **Streaming** | ❌ No | ✅ Yes | ✅ Yes |
| **Schema Evolution** | ✅ Yes | ✅ Flexible | ❌ No |
| **Query Pushdown** | ✅ Yes | ❌ No | ❌ No |

### Performance Comparison

| Metric | Parquet | JSON | CSV |
|--------|---------|------|-----|
| **Storage Size (1M rows)** | ~50 MB | ~500 MB | ~200 MB |
| **Read Time (full scan)** | 1x | 5-10x slower | 3-5x slower |
| **Read Time (2 columns)** | 0.2x | 5-10x slower | 3-5x slower |
| **Compression Ratio** | 10:1 | 2:1 | 3:1 |

### When to Use Each Format

| Format | Best For |
|--------|----------|
| **Parquet** | Analytics, Data Lakes, Data Warehouses, Large datasets, Columnar queries |
| **JSON** | APIs, Configuration files, Document storage, Nested/flexible data, Web applications |
| **CSV** | Data exchange, Simple data, Spreadsheet compatibility, Small datasets, Quick exports |

---

## Python Implementation

### Installation

```bash
# Install required libraries
pip install pandas pyarrow fastparquet
```

### Basic Operations

#### 1. Writing Parquet Files

```python
import pandas as pd

# Create sample data
data = {
    'order_id': [1001, 1002, 1003, 1004, 1005],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'amount': [1200.50, 800.00, 450.75, 350.00, 75.25],
    'order_date': pd.to_datetime(['2024-01-15', '2024-01-16', '2024-01-16', 
                                   '2024-01-17', '2024-01-17'])
}

df = pd.DataFrame(data)

# Write to Parquet (default compression: snappy)
df.to_parquet('orders.parquet', index=False)

# Write with specific compression
df.to_parquet('orders_gzip.parquet', compression='gzip', index=False)
df.to_parquet('orders_snappy.parquet', compression='snappy', index=False)
df.to_parquet('orders_brotli.parquet', compression='brotli', index=False)

print("Parquet files created successfully!")
```

#### 2. Reading Parquet Files

```python
import pandas as pd

# Read entire Parquet file
df = pd.read_parquet('orders.parquet')
print(df)

# Read only specific columns (Column Pruning)
df_subset = pd.read_parquet('orders.parquet', columns=['order_id', 'amount'])
print(df_subset)

# Read with filters (requires pyarrow)
df_filtered = pd.read_parquet(
    'orders.parquet',
    filters=[('amount', '>', 400)]
)
print(df_filtered)
```

#### 3. Working with PyArrow Directly

```python
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

# Create data
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'price': [10.5, 20.0, 15.75, 8.25, 12.00],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Food', 'Clothing']
}

df = pd.DataFrame(data)

# Convert to PyArrow Table
table = pa.Table.from_pandas(df)

# Write with PyArrow
pq.write_table(table, 'products.parquet', compression='snappy')

# Read with PyArrow
table_read = pq.read_table('products.parquet')
print(table_read.to_pandas())

# Read metadata
parquet_file = pq.ParquetFile('products.parquet')
print("Schema:", parquet_file.schema)
print("Metadata:", parquet_file.metadata)
print("Number of row groups:", parquet_file.num_row_groups)
```

#### 4. Partitioned Parquet Files

```python
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Create sample sales data
data = {
    'sale_id': range(1, 101),
    'product': ['Laptop', 'Phone', 'Tablet', 'Monitor'] * 25,
    'region': ['North', 'South', 'East', 'West'] * 25,
    'year': [2023, 2024] * 50,
    'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] * 8 + [1, 2, 3, 4],
    'amount': [round(100 + i * 10.5, 2) for i in range(100)]
}

df = pd.DataFrame(data)
table = pa.Table.from_pandas(df)

# Write partitioned Parquet (creates folder structure)
pq.write_to_dataset(
    table,
    root_path='sales_data',
    partition_cols=['year', 'region']
)

# This creates:
# sales_data/
#   ├── year=2023/
#   │   ├── region=North/
#   │   │   └── *.parquet
#   │   ├── region=South/
#   │   │   └── *.parquet
#   │   └── ...
#   └── year=2024/
#       └── ...

# Read partitioned data with filters (partition pruning)
df_filtered = pd.read_parquet(
    'sales_data',
    filters=[('year', '=', 2024), ('region', '=', 'North')]
)
print(df_filtered)
```

#### 5. Appending Data to Parquet

```python
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Initial data
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'value': ['A', 'B', 'C']
})

# New data to append
df2 = pd.DataFrame({
    'id': [4, 5, 6],
    'value': ['D', 'E', 'F']
})

# Write initial data
df1.to_parquet('data.parquet', index=False)

# Method 1: Read, concatenate, and write
existing_df = pd.read_parquet('data.parquet')
combined_df = pd.concat([existing_df, df2], ignore_index=True)
combined_df.to_parquet('data.parquet', index=False)

# Method 2: Using ParquetWriter for large files
writer = pq.ParquetWriter('data_appended.parquet', pa.Table.from_pandas(df1).schema)
writer.write_table(pa.Table.from_pandas(df1))
writer.write_table(pa.Table.from_pandas(df2))
writer.close()
```

#### 6. Compare File Sizes

```python
import pandas as pd
import os
import json

# Create a larger dataset for comparison
n_rows = 100000
data = {
    'id': range(n_rows),
    'name': [f'Customer_{i}' for i in range(n_rows)],
    'email': [f'customer_{i}@email.com' for i in range(n_rows)],
    'age': [25 + (i % 50) for i in range(n_rows)],
    'salary': [50000.0 + (i * 10.5) for i in range(n_rows)],
    'department': ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance'] * (n_rows // 5)
}

df = pd.DataFrame(data)

# Save in different formats
df.to_csv('comparison.csv', index=False)
df.to_json('comparison.json', orient='records')
df.to_parquet('comparison.parquet', index=False)
df.to_parquet('comparison_gzip.parquet', compression='gzip', index=False)

# Compare file sizes
files = ['comparison.csv', 'comparison.json', 'comparison.parquet', 'comparison_gzip.parquet']

print("\n" + "="*50)
print("FILE SIZE COMPARISON (100,000 rows)")
print("="*50)

for file in files:
    size = os.path.getsize(file)
    print(f"{file:30} : {size/1024/1024:.2f} MB")
```

**Example Output:**
```
==================================================
FILE SIZE COMPARISON (100,000 rows)
==================================================
comparison.csv                 : 5.82 MB
comparison.json                : 8.45 MB
comparison.parquet             : 1.23 MB
comparison_gzip.parquet        : 0.89 MB
```

#### 7. Reading Specific Row Groups

```python
import pyarrow.parquet as pq

# Read metadata without loading data
parquet_file = pq.ParquetFile('large_file.parquet')

print(f"Number of row groups: {parquet_file.num_row_groups}")
print(f"Schema: {parquet_file.schema}")

# Read specific row group
row_group_0 = parquet_file.read_row_group(0)
print(row_group_0.to_pandas())

# Read specific row groups
row_groups = parquet_file.read_row_groups([0, 1])
print(row_groups.to_pandas())
```

#### 8. Using DuckDB with Parquet (Fast Analytics)

```python
import duckdb

# Query Parquet files directly with SQL
result = duckdb.query("""
    SELECT 
        department,
        COUNT(*) as employee_count,
        AVG(salary) as avg_salary,
        MAX(salary) as max_salary
    FROM 'comparison.parquet'
    GROUP BY department
    ORDER BY avg_salary DESC
""").df()

print(result)

# Query partitioned Parquet
result = duckdb.query("""
    SELECT year, region, SUM(amount) as total_sales
    FROM 'sales_data/**/*.parquet'
    GROUP BY year, region
    ORDER BY year, total_sales DESC
""").df()

print(result)
```

---

## Industry Use Cases

### 1. **E-Commerce / Retail**

| Use Case | Description |
|----------|-------------|
| **Order Analytics** | Store billions of order records for trend analysis |
| **Customer 360** | Unified customer data for segmentation |
| **Inventory Reports** | Historical inventory levels and movements |
| **Sales Dashboards** | Pre-aggregated data for real-time dashboards |

```python
# Example: E-commerce daily sales pipeline
import pandas as pd

# Daily sales ETL
def process_daily_sales(date):
    # Extract from source
    raw_data = pd.read_csv(f'raw_sales_{date}.csv')
    
    # Transform
    processed = raw_data.groupby(['product_id', 'category']).agg({
        'quantity': 'sum',
        'revenue': 'sum',
        'order_id': 'count'
    }).reset_index()
    
    # Load to Parquet (partitioned by date)
    processed['date'] = date
    processed.to_parquet(
        f'data_lake/sales/date={date}/sales.parquet',
        index=False
    )
```

---

### 2. **Financial Services**

| Use Case | Description |
|----------|-------------|
| **Transaction History** | Store years of transaction data efficiently |
| **Risk Reporting** | Daily risk calculations and historical comparisons |
| **Regulatory Compliance** | Long-term data retention with fast retrieval |
| **Portfolio Analytics** | Historical portfolio performance analysis |

```python
# Example: Financial transaction storage
import pandas as pd
from datetime import datetime

def store_transactions(transactions_df):
    # Add partitioning columns
    transactions_df['year'] = transactions_df['timestamp'].dt.year
    transactions_df['month'] = transactions_df['timestamp'].dt.month
    
    # Write partitioned Parquet
    transactions_df.to_parquet(
        'transactions_lake',
        partition_cols=['year', 'month'],
        index=False
    )

# Query specific month (only reads relevant partition)
df = pd.read_parquet(
    'transactions_lake',
    filters=[('year', '=', 2024), ('month', '=', 1)]
)
```

---

### 3. **Healthcare**

| Use Case | Description |
|----------|-------------|
| **Patient Records** | Historical patient data for analysis |
| **Claims Processing** | Insurance claims data warehouse |
| **Clinical Analytics** | Treatment outcomes and patterns |
| **Operational Reports** | Hospital capacity and resource utilization |

---

### 4. **Telecommunications**

| Use Case | Description |
|----------|-------------|
| **CDR Processing** | Call Detail Records storage and analysis |
| **Network Analytics** | Network performance metrics |
| **Customer Usage** | Data usage patterns and billing |
| **Churn Analysis** | Historical customer behavior data |

```python
# Example: CDR processing pipeline
import pandas as pd
import pyarrow.parquet as pq

def process_cdr_batch(raw_cdr_path, output_path):
    # Read raw CDR data
    cdr = pd.read_csv(raw_cdr_path)
    
    # Process and aggregate
    hourly_summary = cdr.groupby(['cell_tower_id', 'hour']).agg({
        'call_duration': 'sum',
        'data_usage_mb': 'sum',
        'call_id': 'count'
    }).reset_index()
    
    # Store as Parquet with compression
    hourly_summary.to_parquet(
        output_path,
        compression='snappy',
        index=False
    )
```

---

### 5. **Logistics & Supply Chain**

| Use Case | Description |
|----------|-------------|
| **Shipment Tracking** | Historical shipment data for analytics |
| **Route Optimization** | Historical route data analysis |
| **Warehouse Analytics** | Inventory movement patterns |
| **Supplier Performance** | Vendor metrics over time |

---

### 6. **Media & Entertainment**

| Use Case | Description |
|----------|-------------|
| **Viewing Analytics** | Content consumption patterns |
| **Ad Performance** | Advertisement metrics and attribution |
| **Content Catalog** | Metadata storage and retrieval |
| **User Engagement** | Session data and user behavior |

---

## Best Practices Summary

```
┌────────────────────────────────────────────────────────────┐
│                   PARQUET BEST PRACTICES                   │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ✅ DO:                                                    │
│     • Use partitioning for large datasets                  │
│     • Choose appropriate compression (snappy for speed,    │
│       gzip for size)                                       │
│     • Read only required columns                           │
│     • Use predicate pushdown for filtering                 │
│     • Keep row group sizes between 50MB - 200MB            │
│                                                            │
│  ❌ DON'T:                                                 │
│     • Use Parquet for streaming/real-time data             │
│     • Store very small files (overhead not worth it)       │
│     • Over-partition (too many small files)                │
│     • Ignore schema evolution when modifying columns       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## Conclusion

| Aspect | Summary |
|--------|---------|
| **When to Use Parquet** | Large datasets, analytical queries, data lakes, ETL pipelines |
| **Key Benefits** | Compression, column pruning, fast analytics, schema support |
| **Python Libraries** | `pandas`, `pyarrow`, `fastparquet`, `duckdb` |
| **Best For** | Read-heavy workloads, aggregations, historical data |

Parquet has become the **de facto standard** for storing analytical data in modern data platforms due to its efficiency, compatibility with big data tools, and excellent compression characteristics.

---

> **Note:** The content you provided was already in Markdown format. I've preserved all the original formatting including headers, tables, code blocks, lists, and special characters. You can copy this directly into any Markdown editor or viewer.
