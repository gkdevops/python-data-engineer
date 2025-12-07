# Python Data Engineer - Practice Exercises

## 📝 Overview

Below are **3 exercises per topic** (36 total) ranging from beginner to intermediate difficulty. Each exercise includes the problem statement, hints, and expected output format.

---

## 01. Python Introduction

### Exercise 1.1: Variable Explorer (Easy)
**Task:** Create variables to store information about a data pipeline.

```python
# Create the following variables:
# - pipeline_name: "sales_etl_pipeline"
# - records_processed: 15000
# - success_rate: 99.5
# - is_active: True

# Print each variable with its type in this format:
# "Variable: <value>, Type: <type>"
```

**Expected Output:**
```
Variable: sales_etl_pipeline, Type: <class 'str'>
Variable: 15000, Type: <class 'int'>
Variable: 99.5, Type: <class 'float'>
Variable: True, Type: <class 'bool'>
```

---

### Exercise 1.2: String Manipulation for Data Cleaning (Medium)
**Task:** Clean and transform raw data strings.

```python
raw_data = "  John DOE,  new york,  ENGINEER  "

# Perform the following operations:
# 1. Remove leading/trailing whitespace
# 2. Split by comma into a list
# 3. Clean each element (strip whitespace, convert to title case)
# 4. Join back with " | " separator
# 5. Print the cleaned string and its length
```

**Expected Output:**
```
Cleaned Data: John Doe | New York | Engineer
Length: 31
```

---

### Exercise 1.3: Data Type Converter (Hard)
**Task:** Build a mini data type conversion utility.

```python
# Given a list of string values from a CSV import:
raw_values = ["42", "3.14159", "True", "2024", "False", "99.99"]

# Convert each to its appropriate Python type:
# - Integers for whole numbers
# - Floats for decimal numbers
# - Booleans for "True"/"False" strings

# Print each converted value with its new type
# Also calculate and print the sum of all numeric values
```

**Expected Output:**
```
42 -> <class 'int'>
3.14159 -> <class 'float'>
True -> <class 'bool'>
2024 -> <class 'int'>
False -> <class 'bool'>
99.99 -> <class 'float'>
Sum of numeric values: 2169.13
```

---

## 02. Python Conditions

### Exercise 2.1: Data Quality Flag (Easy)
**Task:** Create a data quality checker for a single record.

```python
# Given a record:
record = {"name": "Alice", "age": 25, "email": "alice@email.com"}

# Write conditions to check:
# 1. Name is not empty
# 2. Age is between 0 and 120
# 3. Email contains "@"

# Print "VALID" if all checks pass, otherwise print which check failed
```

**Expected Output:**
```
VALID
```

---

### Exercise 2.2: ETL Status Classifier (Medium)
**Task:** Classify pipeline job status based on metrics.

```python
# Given job metrics:
records_processed = 9500
records_expected = 10000
error_count = 45
runtime_seconds = 3600

# Classify the job status:
# - "SUCCESS": >= 99% records processed AND < 10 errors
# - "WARNING": >= 95% records processed AND < 100 errors
# - "PARTIAL_FAILURE": >= 80% records processed OR runtime < 7200
# - "FAILURE": otherwise

# Also add a flag if the job exceeded 1 hour runtime
```

**Expected Output:**
```
Job Status: WARNING
Runtime Alert: Job exceeded 1 hour (3600 seconds)
Processing Rate: 95.0%
```

---

### Exercise 2.3: Data Tier Assignment (Hard)
**Task:** Assign data storage tiers based on multiple criteria.

```python
# Given file metadata:
files = [
    {"name": "report_2024.csv", "size_mb": 500, "access_frequency": "daily", "age_days": 5},
    {"name": "archive_2020.csv", "size_mb": 2000, "access_frequency": "yearly", "age_days": 1500},
    {"name": "logs_current.json", "size_mb": 50, "access_frequency": "hourly", "age_days": 1},
    {"name": "backup_2023.parquet", "size_mb": 5000, "access_frequency": "monthly", "age_days": 400}
]

# Assign tiers based on:
# - "HOT": accessed hourly/daily AND age < 30 days
# - "WARM": accessed daily/weekly/monthly AND age < 365 days
# - "COLD": accessed yearly OR age >= 365 days
# - "ARCHIVE": age > 1000 days AND size > 1000 MB

# Print each file with its assigned tier and estimated monthly cost
# (HOT: $0.023/MB, WARM: $0.0125/MB, COLD: $0.004/MB, ARCHIVE: $0.001/MB)
```

**Expected Output:**
```
report_2024.csv -> WARM -> $6.25/month
archive_2020.csv -> ARCHIVE -> $2.00/month
logs_current.json -> HOT -> $1.15/month
backup_2023.parquet -> COLD -> $20.00/month
Total Monthly Cost: $29.40
```

---

## 03. Python Loops

### Exercise 3.1: Record Counter (Easy)
**Task:** Count records by category using a loop.

```python
transactions = ["sale", "return", "sale", "sale", "exchange", "return", "sale"]

# Using a for loop, count occurrences of each transaction type
# Print the counts in a formatted way
```

**Expected Output:**
```
Transaction Counts:
- sale: 4
- return: 2
- exchange: 1
Total transactions: 7
```

---

### Exercise 3.2: Batch Processor Simulator (Medium)
**Task:** Simulate processing data in batches.

```python
total_records = 47
batch_size = 10

# Using a while loop, simulate batch processing:
# - Process records in batches of 10
# - Print progress for each batch
# - Handle the final partial batch correctly
```

**Expected Output:**
```
Processing batch 1: records 1-10 (10 records)
Processing batch 2: records 11-20 (10 records)
Processing batch 3: records 21-30 (10 records)
Processing batch 4: records 31-40 (10 records)
Processing batch 5: records 41-47 (7 records)
Complete! Processed 47 records in 5 batches.
```

---

### Exercise 3.3: Data Validation Pipeline (Hard)
**Task:** Validate records with multiple rules and track statistics.

```python
records = [
    {"id": 1, "name": "Alice", "email": "alice@test.com", "age": 30},
    {"id": 2, "name": "", "email": "bob@test.com", "age": 25},
    {"id": 3, "name": "Charlie", "email": "invalid-email", "age": 35},
    {"id": 4, "name": "Diana", "email": "diana@test.com", "age": -5},
    {"id": 5, "name": "Eve", "email": "eve@test.com", "age": 28},
    {"id": 6, "name": "Frank", "email": "", "age": 40},
]

# Validate each record:
# - name must not be empty
# - email must contain "@"
# - age must be between 0 and 120

# Use continue to skip invalid records
# Use break if more than 3 records fail validation
# Track: valid_count, invalid_count, error_details
```

**Expected Output:**
```
Record 1: VALID
Record 2: INVALID - Empty name
Record 3: INVALID - Invalid email format
Record 4: INVALID - Invalid age
Record 5: VALID
Processing stopped: Too many validation failures

Summary:
- Valid records: 2
- Invalid records: 3
- Validation errors:
  * Record 2: Empty name
  * Record 3: Invalid email format
  * Record 4: Invalid age
```

---

## 04. Python Functions

### Exercise 4.1: Data Transformer Function (Easy)
**Task:** Create a function to standardize names.

```python
# Create a function called standardize_name that:
# - Takes a full name string as input
# - Returns the name in "LASTNAME, Firstname" format
# - Handles extra whitespace

# Test with:
# standardize_name("  john   doe  ")
# standardize_name("JANE SMITH")
# standardize_name("bob johnson")
```

**Expected Output:**
```
DOE, John
SMITH, Jane
JOHNSON, Bob
```

---

### Exercise 4.2: Flexible Aggregator (Medium)
**Task:** Create a function with default parameters for data aggregation.

```python
# Create a function called aggregate_data that:
# - Takes a list of numbers
# - Has optional parameters: operation="sum", round_to=2, ignore_nulls=True
# - Supports operations: "sum", "avg", "min", "max", "count"
# - Returns the result rounded to specified decimal places

data = [10.5, 20.3, None, 30.7, 15.2, None, 25.8]

# Test with different combinations:
# aggregate_data(data)
# aggregate_data(data, operation="avg")
# aggregate_data(data, operation="max", round_to=0)
# aggregate_data(data, ignore_nulls=False)  # Should handle None values
```

**Expected Output:**
```
Sum: 102.5
Average: 20.5
Max: 31.0
Sum with nulls: Error - Cannot process None values
```

---

### Exercise 4.3: Pipeline Function Factory (Hard)
**Task:** Create higher-order functions for building data pipelines.

```python
# Create the following:
# 1. A function create_validator(rules) that returns a validation function
# 2. A function create_transformer(transformations) that returns a transform function
# 3. A function pipe(*functions) that chains functions together

# Rules format: {"field": "age", "min": 0, "max": 120}
# Transformations format: {"field": "name", "operation": "upper"}

# Create a pipeline that:
# 1. Validates age is between 0-120
# 2. Transforms name to uppercase
# 3. Adds a "processed" timestamp field

# Test with sample records
sample_records = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 150},  # Should fail validation
    {"name": "charlie", "age": 35}
]
```

**Expected Output:**
```
Processing record 1:
  Validation: PASSED
  Transformed: {'name': 'ALICE', 'age': 25, 'processed': '2024-01-15 10:30:00'}

Processing record 2:
  Validation: FAILED - age out of range (0-120)
  Skipped transformation

Processing record 3:
  Validation: PASSED
  Transformed: {'name': 'CHARLIE', 'age': 35, 'processed': '2024-01-15 10:30:00'}

Pipeline Summary: 2 succeeded, 1 failed
```

---

## 05. Python Operators

### Exercise 5.1: Data Comparison Utility (Easy)
**Task:** Compare two datasets using comparison operators.

```python
dataset_a = {"records": 1000, "size_mb": 50.5, "complete": True}
dataset_b = {"records": 1200, "size_mb": 45.2, "complete": True}

# Compare the datasets and print:
# - Which has more records
# - Which is larger in size
# - If both are complete
# - If they are equal in record count
```

**Expected Output:**
```
Record comparison: Dataset B has more records (1200 > 1000)
Size comparison: Dataset A is larger (50.5 MB > 45.2 MB)
Both complete: True
Equal record count: False
```

---

### Exercise 5.2: Bitwise Permission Checker (Medium)
**Task:** Use bitwise operators for permission management.

```python
# Permission flags (using bitwise):
READ = 0b001     # 1
WRITE = 0b010    # 2
DELETE = 0b100   # 4

# User permissions
admin_perms = 0b111      # All permissions
analyst_perms = 0b001    # Read only
engineer_perms = 0b011   # Read and write

users = {
    "admin": admin_perms,
    "analyst": analyst_perms,
    "engineer": engineer_perms
}

# For each user, check and print:
# - Can read?
# - Can write?
# - Can delete?
# - Permission level name
```

**Expected Output:**
```
User: admin
  Read: ✓ | Write: ✓ | Delete: ✓
  Level: FULL ACCESS

User: analyst
  Read: ✓ | Write: ✗ | Delete: ✗
  Level: READ ONLY

User: engineer
  Read: ✓ | Write: ✓ | Delete: ✗
  Level: READ/WRITE
```

---

### Exercise 5.3: Expression Evaluator for Data Rules (Hard)
**Task:** Build a rule engine using operators and precedence.

```python
# Create a rule evaluator for data quality
# Rules are defined as strings and evaluated against records

records = [
    {"id": 1, "amount": 150, "status": "active", "priority": 2},
    {"id": 2, "amount": 50, "status": "pending", "priority": 1},
    {"id": 3, "amount": 500, "status": "active", "priority": 3},
    {"id": 4, "amount": 75, "status": "inactive", "priority": 1},
]

# Rules to evaluate:
rules = [
    "amount > 100 and status == 'active'",
    "priority >= 2 or amount > 200",
    "not status == 'inactive' and amount >= 50"
]

# For each record, evaluate all rules and show:
# - Which rules passed
# - Overall pass/fail (all rules must pass)
# - Use operator precedence correctly
```

**Expected Output:**
```
Record 1 (id=1):
  Rule 1 (amount > 100 and status == 'active'): PASS
  Rule 2 (priority >= 2 or amount > 200): PASS
  Rule 3 (not status == 'inactive' and amount >= 50): PASS
  Overall: ✓ ALL RULES PASSED

Record 2 (id=2):
  Rule 1: FAIL
  Rule 2: FAIL
  Rule 3: PASS
  Overall: ✗ 1/3 RULES PASSED

Record 3 (id=3):
  Rule 1: PASS
  Rule 2: PASS
  Rule 3: PASS
  Overall: ✓ ALL RULES PASSED

Record 4 (id=4):
  Rule 1: FAIL
  Rule 2: FAIL
  Rule 3: FAIL
  Overall: ✗ 0/3 RULES PASSED
```

---

## 06. Python Collections

### Exercise 6.1: List Operations for Data Batching (Easy)
**Task:** Manipulate lists for batch processing.

```python
data_ids = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Perform the following operations:
# 1. Split into batches of 3 using slicing
# 2. Get the last 4 elements
# 3. Reverse the list
# 4. Check if 105 is in the list
# 5. Find the index of 107
```

**Expected Output:**
```
Batches of 3: [[101, 102, 103], [104, 105, 106], [107, 108, 109], [110]]
Last 4 elements: [107, 108, 109, 110]
Reversed: [110, 109, 108, 107, 106, 105, 104, 103, 102, 101]
Contains 105: True
Index of 107: 6
```

---

### Exercise 6.2: Dictionary-Based Record Manager (Medium)
**Task:** Use dictionaries to manage employee records.

```python
employees = {
    "E001": {"name": "Alice", "dept": "Engineering", "salary": 75000},
    "E002": {"name": "Bob", "dept": "Sales", "salary": 65000},
    "E003": {"name": "Charlie", "dept": "Engineering", "salary": 80000},
    "E004": {"name": "Diana", "dept": "HR", "salary": 60000},
    "E005": {"name": "Eve", "dept": "Engineering", "salary": 85000}
}

# Perform these operations:
# 1. Add a new employee E006 (Frank, Sales, 70000)
# 2. Give all Engineering dept employees a 10% raise
# 3. Find the highest paid employee
# 4. Group employees by department
# 5. Calculate average salary per department
```

**Expected Output:**
```
Added: E006 - Frank

After raises:
E001: Alice - $82,500
E003: Charlie - $88,000
E005: Eve - $93,500

Highest paid: Eve ($93,500)

By Department:
- Engineering: ['Alice', 'Charlie', 'Eve']
- Sales: ['Bob', 'Frank']
- HR: ['Diana']

Average Salary by Dept:
- Engineering: $88,000
- Sales: $67,500
- HR: $60,000
```

---

### Exercise 6.3: Set Operations for Data Reconciliation (Hard)
**Task:** Use sets to reconcile data between systems.

```python
# Data from different sources
source_system = {"C001", "C002", "C003", "C004", "C005", "C006", "C007"}
target_system = {"C002", "C003", "C005", "C008", "C009"}
archive_system = {"C001", "C010", "C011"}
priority_customers = {"C003", "C005", "C007", "C012"}

# Perform reconciliation:
# 1. Find customers in source but not in target (need to sync)
# 2. Find customers in target but not in source (orphaned)
# 3. Find customers present in all three systems
# 4. Find priority customers that are missing from target
# 5. Create a complete customer master set
# 6. Find customers unique to only one system
```

**Expected Output:**
```
=== Data Reconciliation Report ===

1. Need to Sync (Source → Target): {'C001', 'C004', 'C006', 'C007'}
   Count: 4

2. Orphaned in Target: {'C008', 'C009'}
   Count: 2

3. Present in All Systems: {'C001'}
   Count: 1

4. Priority Customers Missing from Target: {'C007'}
   Count: 1
   ⚠️ ACTION REQUIRED: High priority data sync needed!

5. Complete Customer Master: {'C001', 'C002', ..., 'C012'}
   Total Unique Customers: 12

6. Unique to Single System:
   - Only in Source: {'C004', 'C006'}
   - Only in Target: {'C008', 'C009'}
   - Only in Archive: {'C010', 'C011'}
```

---

## 07. Python Modules & Packages

### Exercise 7.1: Standard Library Explorer (Easy)
**Task:** Use multiple standard library modules together.

```python
# Using os, datetime, and sys modules:
# 1. Print the current working directory
# 2. Print today's date in format "YYYY-MM-DD"
# 3. Print the Python version
# 4. Print the platform name
# 5. Create a timestamp-based filename pattern
```

**Expected Output:**
```
Current Directory: /home/user/projects
Today's Date: 2024-01-15
Python Version: 3.11.5
Platform: linux

Generated Filename: data_export_2024-01-15_143022.csv
```

---

### Exercise 7.2: Create a Data Utils Module (Medium)
**Task:** Create your own module with reusable functions.

```python
# Create a file called data_utils.py with:

# 1. Function: clean_string(text) - strips and lowercases
# 2. Function: validate_email(email) - returns True/False
# 3. Function: format_currency(amount, currency="USD") - returns formatted string
# 4. Constant: SUPPORTED_FORMATS = ["csv", "json", "parquet"]
# 5. Function: calculate_stats(numbers) - returns dict with min, max, avg, sum

# Then import and use the module in another script
```

**Expected Output:**
```python
# In main.py:
from data_utils import clean_string, validate_email, format_currency, calculate_stats

print(clean_string("  HELLO WORLD  "))  # "hello world"
print(validate_email("test@example.com"))  # True
print(format_currency(1234.56))  # "$1,234.56 USD"
print(calculate_stats([10, 20, 30, 40, 50]))
# {'min': 10, 'max': 50, 'avg': 30.0, 'sum': 150}
```

---

### Exercise 7.3: Package Structure Builder (Hard)
**Task:** Design and implement a complete data engineering package.

```python
# Create the following package structure:
# 
# de_toolkit/
#   ├── __init__.py
#   ├── extractors/
#   │   ├── __init__.py
#   │   ├── csv_extractor.py
#   │   └── json_extractor.py
#   ├── transformers/
#   │   ├── __init__.py
#   │   ├── cleaners.py
#   │   └── validators.py
#   └── loaders/
#       ├── __init__.py
#       └── file_loader.py

# Each module should have at least 2 functions
# The package __init__.py should expose main functions
# Include proper docstrings

# Demonstrate usage:
# from de_toolkit import extract_csv, clean_data, load_to_file
# from de_toolkit.transformers import cleaners
```

**Expected Output:**
```
Package Structure Created: de_toolkit

Available Functions:
- de_toolkit.extract_csv()
- de_toolkit.extract_json()
- de_toolkit.clean_data()
- de_toolkit.validate_schema()
- de_toolkit.load_to_file()

Usage Example:
>>> from de_toolkit import extract_csv, clean_data
>>> data = extract_csv("sales.csv")
>>> cleaned = clean_data(data, rules=["trim", "lowercase"])
>>> print(f"Processed {len(cleaned)} records")
Processed 150 records
```

---

## 08. Files-CSV Directory

### Exercise 8.1: CSV Reader and Analyzer (Easy)
**Task:** Read a CSV file and perform basic analysis.

```python
# Create a sample CSV file with this data, then read and analyze:
'''
id,name,department,salary,hire_date
1,Alice,Engineering,75000,2020-01-15
2,Bob,Sales,65000,2019-06-20
3,Charlie,Engineering,80000,2021-03-10
4,Diana,HR,60000,2018-09-05
5,Eve,Engineering,85000,2022-07-22
'''

# Tasks:
# 1. Read the CSV file
# 2. Print the number of rows and columns
# 3. Print all column headers
# 4. Calculate and print the average salary
# 5. Find the employee with the highest salary
```

**Expected Output:**
```
File loaded: employees.csv
Rows: 5, Columns: 5
Headers: ['id', 'name', 'department', 'salary', 'hire_date']
Average Salary: $73,000.00
Highest Paid: Eve ($85,000)
```

---

### Exercise 8.2: CSV Transformer with Pandas (Medium)
**Task:** Read, transform, and write CSV data using Pandas.

```python
# Given the same employee CSV from Exercise 8.1:
# 
# 1. Read the CSV into a DataFrame
# 2. Add a new column 'years_employed' (from hire_date to today)
# 3. Add a column 'salary_band' based on:
#    - "Junior": salary < 65000
#    - "Mid": salary 65000-79999
#    - "Senior": salary >= 80000
# 4. Filter to only Engineering department
# 5. Sort by salary descending
# 6. Save the result to 'engineering_team.csv'
```

**Expected Output:**
```
Original data shape: (5, 5)
Transformed data shape: (3, 7)

Engineering Team Report:
   name  salary  years_employed salary_band
0   Eve   85000               2      Senior
1 Charlie 80000               3      Senior
2  Alice  75000               4         Mid

Saved to: engineering_team.csv
```

---

### Exercise 8.3: Multi-File CSV Pipeline (Hard)
**Task:** Process multiple CSV files with error handling.

```python
# Scenario: You have a directory with daily sales CSVs
# Files: sales_2024-01-01.csv, sales_2024-01-02.csv, etc.
# Some files might be corrupted or have missing columns

# Tasks:
# 1. Scan directory for all CSV files matching pattern sales_*.csv
# 2. Read each file with proper error handling
# 3. Validate each file has required columns: [date, product, quantity, price]
# 4. Combine all valid files into a single DataFrame
# 5. Add source_file column to track origin
# 6. Generate a processing report
# 7. Save consolidated data and error log
```

**Expected Output:**
```
=== CSV Processing Pipeline ===
Scanning directory: ./data/sales/

Found 5 files matching pattern

Processing:
  ✓ sales_2024-01-01.csv - 150 rows loaded
  ✓ sales_2024-01-02.csv - 142 rows loaded
  ✗ sales_2024-01-03.csv - ERROR: Missing column 'price'
  ✓ sales_2024-01-04.csv - 168 rows loaded
  ✗ sales_2024-01-05.csv - ERROR: File is empty

Summary:
- Files processed: 5
- Successful: 3
- Failed: 2
- Total rows consolidated: 460

Output files:
- consolidated_sales.csv (460 rows)
- processing_errors.log
```

---

## 09. JSON Directory

### Exercise 9.1: JSON Configuration Reader (Easy)
**Task:** Read and use a JSON configuration file.

```python
# Create a config.json with this content:
'''
{
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "sales_db"
    },
    "settings": {
        "batch_size": 1000,
        "timeout_seconds": 30,
        "retry_count": 3
    },
    "enabled_features": ["logging", "caching", "compression"]
}
'''

# Tasks:
# 1. Read the JSON file
# 2. Print the database connection string: "host:port/name"
# 3. Check if "logging" is an enabled feature
# 4. Update batch_size to 2000
# 5. Add a new feature "monitoring" to enabled_features
# 6. Save the updated config
```

**Expected Output:**
```
Loaded config.json

Database Connection: localhost:5432/sales_db
Logging enabled: True
Batch size updated: 1000 → 2000
Added feature: monitoring

Saved updated configuration.
```

---

### Exercise 9.2: Nested JSON Parser (Medium)
**Task:** Parse and flatten nested JSON API response.

```python
# Given this API response structure:
api_response = {
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "address": {
                    "city": "New York",
                    "country": "USA"
                },
                "orders": [
                    {"order_id": "A001", "amount": 150.00},
                    {"order_id": "A002", "amount": 89.50}
                ]
            },
            {
                "id": 2,
                "name": "Bob",
                "address": {
                    "city": "London",
                    "country": "UK"
                },
                "orders": [
                    {"order_id": "B001", "amount": 220.00}
                ]
            }
        ],
        "metadata": {
            "total_users": 2,
            "page": 1
        }
    }
}

# Tasks:
# 1. Extract all user names
# 2. Flatten to a list of order records with user info
# 3. Calculate total order amount per user
# 4. Create a CSV-ready flat structure
```

**Expected Output:**
```
User Names: ['Alice', 'Bob']

Flattened Orders:
| user_id | user_name | city     | order_id | amount |
|---------|-----------|----------|----------|--------|
| 1       | Alice     | New York | A001     | 150.00 |
| 1       | Alice     | New York | A002     | 89.50  |
| 2       | Bob       | London   | B001     | 220.00 |

Total Amount per User:
- Alice: $239.50
- Bob: $220.00
```

---

### Exercise 9.3: JSON Schema Validator (Hard)
**Task:** Build a JSON schema validator.

```python
# Create a schema definition and validator

schema = {
    "type": "object",
    "required": ["id", "name", "email"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 2, "maxLength": 50},
        "email": {"type": "string", "pattern": "^[\\w.-]+@[\\w.-]+\\.\\w+$"},
        "age": {"type": "integer", "minimum": 0, "maximum": 120},
        "tags": {"type": "array", "items": {"type": "string"}}
    }
}

test_records = [
    {"id": 1, "name": "Alice", "email": "alice@test.com", "age": 30},
    {"id": "two", "name": "Bob", "email": "bob@test.com"},  # Invalid id type
    {"id": 3, "name": "C", "email": "charlie@test.com"},     # Name too short
    {"id": 4, "name": "Diana", "email": "not-an-email"},     # Invalid email
    {"id": 5, "name": "Eve", "email": "eve@test.com", "age": 150}  # Age out of range
]

# Validate each record and report errors
```

**Expected Output:**
```
=== JSON Schema Validation Results ===

Record 1: ✓ VALID

Record 2: ✗ INVALID
  - Field 'id': Expected integer, got string

Record 3: ✗ INVALID
  - Field 'name': Length 1 is less than minimum 2

Record 4: ✗ INVALID
  - Field 'email': Does not match pattern (valid email required)

Record 5: ✗ INVALID
  - Field 'age': Value 150 exceeds maximum 120

Validation Summary:
- Total: 5 records
- Valid: 1
- Invalid: 4
```

---

## 10. Randoms Directory

### Exercise 10.1: Random Data Sampler (Easy)
**Task:** Use the random module for data sampling.

```python
import random

customer_ids = list(range(1001, 1051))  # 50 customers

# Tasks:
# 1. Select 5 random customers for a survey
# 2. Shuffle the list and get the first 10 for A/B testing
# 3. Generate a random discount percentage (5-25%)
# 4. Simulate a coin flip to decide treatment group
# 5. Set a seed for reproducibility and demonstrate
```

**Expected Output:**
```
Survey Sample (5 random): [1023, 1007, 1045, 1012, 1038]
A/B Test Group (10): [1019, 1003, 1041, 1027, 1015, 1008, 1033, 1021, 1044, 1006]
Random Discount: 17%
Treatment Group: Control (Heads)

With seed=42:
Run 1: [1037, 1012, 1025]
Run 2: [1037, 1012, 1025]  # Same results!
```

---

### Exercise 10.2: Synthetic Data Generator (Medium)
**Task:** Generate realistic synthetic data for testing.

```python
import random
from faker import Faker

# Generate a dataset of 10 synthetic customer records with:
# - id (sequential starting from 1)
# - name (realistic fake name)
# - email (based on name)
# - phone (fake phone number)
# - registration_date (within last 2 years)
# - account_balance (random float between 0-10000, 2 decimals)
# - status (weighted random: 70% active, 20% inactive, 10% suspended)

# Save as both JSON and CSV
```

**Expected Output:**
```
Generated 10 synthetic customer records:

| id | name           | email                  | balance   | status   |
|----|----------------|------------------------|-----------|----------|
| 1  | John Smith     | john.smith@email.com   | 4,532.18  | active   |
| 2  | Maria Garcia   | maria.garcia@email.com | 892.45    | active   |
| 3  | David Lee      | david.lee@email.com    | 7,123.00  | inactive |
...

Status Distribution:
- Active: 7 (70%)
- Inactive: 2 (20%)
- Suspended: 1 (10%)

Saved to: synthetic_customers.json, synthetic_customers.csv
```

---

### Exercise 10.3: Monte Carlo Data Simulator (Hard)
**Task:** Simulate data scenarios using Monte Carlo methods.

```python
import random
import statistics

# Simulate a data pipeline with random failures
# Parameters:
# - Daily record count: normally distributed, mean=10000, std=1500
# - Per-record failure rate: 0.1%
# - System outage probability: 2% per day
# - Outage impact: lose 50-100% of that day's records

# Run simulation for 365 days
# Calculate:
# 1. Total expected records vs actual processed
# 2. Distribution of daily failure counts
# 3. Number of outage days
# 4. 95th percentile worst day
# 5. Probability of processing >99% records in a month
```

**Expected Output:**
```
=== Monte Carlo Pipeline Simulation (365 days) ===
Simulation runs: 1000

Results Summary:
- Expected annual records: 3,650,000
- Average processed: 3,584,230 (98.2%)
- Std deviation: 45,230

Daily Statistics:
- Average daily processed: 9,819
- Min day: 2,340 (outage impact)
- Max day: 14,523

Outage Analysis:
- Average outage days per year: 7.3
- Outage probability: 2.0%

Percentiles:
- 50th percentile (median day): 9,842 records
- 95th percentile worst day: 4,521 records
- 99th percentile worst day: 1,892 records

Monthly Success Rate (>99% processed):
- Probability: 67.3%
- Months meeting target (avg): 8.1 / 12

Risk Assessment:
- Days below 5000 records: 12.4 per year
- Annual data loss: 1.8% (65,770 records)
```

---

## 11. Blocks Directory

### Exercise 11.1: Reusable Code Blocks (Easy)
**Task:** Create modular code blocks for common operations.

```python
# Create these reusable code blocks as functions:

# Block 1: Timer decorator
# - Measures and prints execution time of any function

# Block 2: Retry block
# - Retries a function N times on failure with delay

# Block 3: Safe file reader
# - Reads a file with proper error handling
# - Returns content or None with error message

# Demonstrate each block
```

**Expected Output:**
```
=== Timer Block Demo ===
@timer
def slow_function():
    time.sleep(2)
    return "done"

Result: done
Execution time: 2.003 seconds

=== Retry Block Demo ===
Attempt 1: Failed - Connection timeout
Attempt 2: Failed - Connection timeout
Attempt 3: Success!
Result: Data retrieved

=== Safe Reader Block Demo ===
Reading 'valid_file.txt': Success (1,234 bytes)
Reading 'missing_file.txt': Failed - FileNotFoundError
```

---

### Exercise 11.2: ETL Block Templates (Medium)
**Task:** Create template blocks for ETL pipeline stages.

```python
# Create these ETL block templates:

# ExtractBlock
# - Configurable source (file, API, database)
# - Connection handling
# - Returns standardized data format

# TransformBlock
# - Chain of transformations
# - Each transformation is configurable
# - Logging of each step

# LoadBlock
# - Configurable destination
# - Batch processing
# - Transaction handling

# Create a mini-pipeline using these blocks
```

**Expected Output:**
```
=== ETL Pipeline Execution ===

[EXTRACT] Starting extraction from: sales_data.csv
[EXTRACT] Connection established
[EXTRACT] Rows extracted: 1,000
[EXTRACT] Extraction complete ✓

[TRANSFORM] Starting transformations
  Step 1/3: Clean nulls → 15 rows affected
  Step 2/3: Normalize dates → 1,000 rows affected
  Step 3/3: Calculate totals → New column added
[TRANSFORM] Transformation complete ✓

[LOAD] Starting load to: data_warehouse
[LOAD] Batch 1/10: 100 rows inserted
[LOAD] Batch 2/10: 100 rows inserted
...
[LOAD] Batch 10/10: 100 rows inserted
[LOAD] Transaction committed ✓
[LOAD] Load complete ✓

Pipeline Summary:
- Duration: 12.5 seconds
- Rows processed: 1,000
- Status: SUCCESS
```

---

### Exercise 11.3: Plugin-Based Processing Blocks (Hard)
**Task:** Create a plugin architecture for processing blocks.

```python
# Build a plugin system where:
# 1. Blocks are registered dynamically
# 2. Pipeline is built from configuration
# 3. New blocks can be added without modifying core code

# Core classes:
# - BlockRegistry: registers and retrieves blocks
# - BlockBase: abstract base class for all blocks
# - PipelineBuilder: constructs pipeline from config

# Built-in blocks:
# - FilterBlock: filters rows by condition
# - MapBlock: applies function to each row
# - AggregateBlock: groups and aggregates
# - JoinBlock: joins two datasets

# Pipeline config example:
pipeline_config = {
    "name": "sales_analysis",
    "blocks": [
        {"type": "FilterBlock", "condition": "amount > 100"},
        {"type": "MapBlock", "function": "calculate_tax"},
        {"type": "AggregateBlock", "group_by": "region", "agg": "sum"}
    ]
}
```

**Expected Output:**
```
=== Block Registry ===
Registered blocks:
- FilterBlock (built-in)
- MapBlock (built-in)
- AggregateBlock (built-in)
- JoinBlock (built-in)
- CustomValidatorBlock (plugin: validators.py)

=== Building Pipeline: sales_analysis ===
Loading configuration...
Validating block sequence...
Instantiating blocks...

Pipeline Structure:
  Input → FilterBlock → MapBlock → AggregateBlock → Output

=== Executing Pipeline ===
Input records: 5,000

[FilterBlock] Condition: amount > 100
  - Rows in: 5,000
  - Rows out: 3,247

[MapBlock] Function: calculate_tax
  - Applied to 3,247 rows
  - New column: 'tax_amount'

[AggregateBlock] Group by: region, Aggregation: sum
  - Groups created: 5
  - Output columns: ['region', 'total_amount', 'total_tax']

Final Output:
| region     | total_amount | total_tax |
|------------|--------------|-----------|
| North      | 125,430.00   | 12,543.00 |
| South      | 98,230.00    | 9,823.00  |
| East       | 156,780.00   | 15,678.00 |
| West       | 87,650.00    | 8,765.00  |
| Central    | 112,340.00   | 11,234.00 |
```

---

## 12. Logging Directory

### Exercise 12.1: Basic Logger Setup (Easy)
**Task:** Configure and use Python's logging module.

```python
import logging

# Tasks:
# 1. Create a logger named "data_pipeline"
# 2. Set up console handler with INFO level
# 3. Set up file handler with DEBUG level
# 4. Use format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# 5. Log messages at different levels
# 6. Demonstrate that DEBUG only appears in file
```

**Expected Output:**
```
Console Output:
2024-01-15 10:30:00 - data_pipeline - INFO - Pipeline started
2024-01-15 10:30:01 - data_pipeline - INFO - Processing 1000 records
2024-01-15 10:30:05 - data_pipeline - WARNING - Slow query detected (3.5s)
2024-01-15 10:30:10 - data_pipeline - ERROR - Failed to connect to database
2024-01-15 10:30:10 - data_pipeline - INFO - Pipeline completed with errors

File Output (pipeline.log) - includes DEBUG:
2024-01-15 10:30:00 - data_pipeline - DEBUG - Initializing connections
2024-01-15 10:30:00 - data_pipeline - DEBUG - Config loaded: batch_size=100
2024-01-15 10:30:00 - data_pipeline - INFO - Pipeline started
... (all messages including DEBUG)
```

---

### Exercise 12.2: Structured Logging for Data Pipelines (Medium)
**Task:** Implement structured JSON logging.

```python
import logging
import json

# Create a structured logger that:
# 1. Outputs logs in JSON format
# 2. Includes custom fields: job_id, step_name, records_processed
# 3. Includes execution metrics: duration, memory_usage
# 4. Handles exceptions with full traceback in structured format

# Implement a LogContext class to manage contextual information
# throughout pipeline execution
```

**Expected Output:**
```json
{
    "timestamp": "2024-01-15T10:30:00.000Z",
    "level": "INFO",
    "logger": "data_pipeline",
    "message": "Batch processing complete",
    "context": {
        "job_id": "job_20240115_001",
        "step_name": "transform",
        "records_processed": 1000,
        "records_failed": 3
    },
    "metrics": {
        "duration_ms": 2340,
        "memory_mb": 256.5,
        "cpu_percent": 45.2
    }
}

{
    "timestamp": "2024-01-15T10:30:05.000Z",
    "level": "ERROR",
    "logger": "data_pipeline",
    "message": "Database connection failed",
    "context": {
        "job_id": "job_20240115_001",
        "step_name": "load"
    },
    "exception": {
        "type": "ConnectionError",
        "message": "Unable to connect to host:5432",
        "traceback": ["File 'pipeline.py', line 45, in connect...", ...]
    }
}
```

---

### Exercise 12.3: Advanced Logging System (Hard)
**Task:** Build a comprehensive logging system for production.

```python
# Build a logging system with:
# 1. Multiple handlers: console, file, remote (simulated)
# 2. Log rotation: by size and by time
# 3. Log aggregation: collect logs from multiple modules
# 4. Alert system: send alerts (print) for CRITICAL errors
# 5. Log analysis: method to parse and analyze log files
# 6. Performance tracking: measure and log function performance

# Classes to implement:
# - PipelineLogger: main logging class
# - LogRotator: handles log rotation
# - AlertManager: manages alerts for critical events
# - LogAnalyzer: parses and analyzes log files
```

**Expected Output:**
```
=== Logging System Initialized ===
Handlers configured:
  - Console (INFO+)
  - File: logs/pipeline.log (DEBUG+, max 10MB, 5 backups)
  - File: logs/pipeline.log.1 (rotated)
  - Alert Manager (CRITICAL → email simulation)

=== Running Pipeline with Logging ===
[INFO] Starting pipeline execution
[DEBUG] Loading configuration from config.json
[INFO] Step 1: Extract - Started
[DEBUG] Connecting to source: postgres://localhost:5432/sales
[INFO] Step 1: Extract - Complete (2,500 rows, 1.2s)
[WARN] Step 2: Transform - 15 null values found
[INFO] Step 2: Transform - Complete (2,485 rows, 3.4s)
[CRITICAL] Step 3: Load - Connection timeout after 30s

🚨 ALERT TRIGGERED 🚨
Type: CRITICAL
Message: Load step failed - Connection timeout
Sent to: ops-team@company.com

=== Log Analysis Report ===
Log file: logs/pipeline.log
Time range: 2024-01-15 00:00:00 to 2024-01-15 23:59:59

Statistics:
  Total entries: 1,247
  By level:
    - DEBUG: 523 (42%)
    - INFO: 612 (49%)
    - WARNING: 87 (7%)
    - ERROR: 21 (2%)
    - CRITICAL: 4 (<1%)

Performance Metrics:
  Average step duration: 2.3s
  Slowest step: Transform (avg 4.1s)
  Most frequent error: ConnectionError (12 occurrences)

Recommendations:
  ⚠️ High error rate in Load step - investigate connection issues
  ⚠️ Transform step showing performance degradation
```

---

## 📋 Answer Key / Solutions Guide

For each exercise, solutions should demonstrate:

| Difficulty | Expectations |
|------------|--------------|
| **Easy** | Basic syntax, single concept, working code |
| **Medium** | Multiple concepts combined, error handling, clean code |
| **Hard** | Advanced patterns, edge cases, production-ready code |

---

## 🎯 Suggested Learning Path

```
Week 1: Topics 1-3 (Introduction, Conditions, Loops)
Week 2: Topics 4-6 (Functions, Operators, Collections)
Week 3: Topics 7-9 (Modules, Files/CSV, JSON)
Week 4: Topics 10-12 (Randoms, Blocks, Logging)
```

---

**Good luck with your Python Data Engineering journey! 🐍📊**
