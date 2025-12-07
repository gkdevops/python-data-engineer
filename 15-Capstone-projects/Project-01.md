# Python Data Engineer - Final Capstone Exercise - 1

## 🎯 Customer Data Integration Pipeline

### 📋 Business Scenario
Your company has customer data coming from two different systems:
- **CRM System** exports data as CSV
- **E-commerce Platform** exports data as JSON

You need to build a pipeline that integrates both sources, cleans the data, removes duplicates, and produces a unified customer master file.

**Difficulty Level:** Medium

**Time Estimate:** 2-4 hours per exercise

---

### 🎯 Requirements

```
INPUT FILES:
├── crm_customers.csv
└── ecommerce_customers.json

OUTPUT FILES:
├── customer_master.csv
├── duplicate_report.csv
└── integration_log.txt
```

### 📁 Sample Input Data

**crm_customers.csv:**
```csv
customer_id,full_name,email,phone,signup_date,status
CRM001,John Smith,john.smith@email.com,+1-555-0101,2023-01-15,active
CRM002,Jane Doe,JANE.DOE@EMAIL.COM,555.0102,2023-02-20,active
CRM003,Bob Wilson,bob.wilson@email.com,+1-555-0103,2023-03-10,inactive
CRM004,Alice Brown,alice.b@email.com,,2023-04-05,active
CRM005,john smith,j.smith@email.com,+1-555-0101,2023-05-12,active
```

**ecommerce_customers.json:**
```json
{
  "customers": [
    {
      "id": "EC1001",
      "name": {"first": "John", "last": "Smith"},
      "contact": {"email": "john.smith@email.com", "phone": "5550101"},
      "registered": "2023-01-15T10:30:00Z",
      "orders_count": 5
    },
    {
      "id": "EC1002",
      "name": {"first": "Mary", "last": "Johnson"},
      "contact": {"email": "mary.j@email.com", "phone": "5550104"},
      "registered": "2023-03-22T14:15:00Z",
      "orders_count": 3
    },
    {
      "id": "EC1003",
      "name": {"first": "Jane", "last": "Doe"},
      "contact": {"email": "jane.doe@email.com", "phone": "5550102"},
      "registered": "2023-02-20T09:00:00Z",
      "orders_count": 8
    }
  ]
}
```

### ✅ Tasks

1. **Extract Phase**
   - Read both data sources
   - Handle file not found errors gracefully
   - Log the number of records from each source

2. **Transform Phase**
   - Normalize all data to a common schema:
     ```
     unified_id, full_name, email, phone, signup_date, source_system, status
     ```
   - Clean data:
     - Standardize email to lowercase
     - Standardize phone to format: `5550101` (digits only)
     - Standardize names to Title Case
     - Parse dates to `YYYY-MM-DD` format
   - Handle missing values (replace with "N/A" or appropriate default)

3. **Deduplicate Phase**
   - Identify duplicates based on:
     - Exact email match, OR
     - Same phone number, OR
     - Similar name (same name, case-insensitive)
   - Keep the record with more information (fewer N/A values)
   - Log duplicates found with reason

4. **Load Phase**
   - Write unified customer master to CSV
   - Write duplicate report showing which records were merged
   - Write detailed log file

### 📤 Expected Output

**customer_master.csv:**
```csv
unified_id,full_name,email,phone,signup_date,source_system,status
CUST001,John Smith,john.smith@email.com,5550101,2023-01-15,CRM+ECOM,active
CUST002,Jane Doe,jane.doe@email.com,5550102,2023-02-20,CRM+ECOM,active
CUST003,Bob Wilson,bob.wilson@email.com,5550103,2023-03-10,CRM,inactive
CUST004,Alice Brown,alice.b@email.com,N/A,2023-04-05,CRM,active
CUST005,Mary Johnson,mary.j@email.com,5550104,2023-03-22,ECOM,active
```

**duplicate_report.csv:**
```csv
kept_id,removed_ids,match_reason,removed_sources
CUST001,"CRM005,EC1001",email+phone+name,CRM
CUST002,EC1003,email+phone,ECOM
```

**integration_log.txt:**
```
2024-01-15 10:30:00 - INFO - Pipeline started
2024-01-15 10:30:00 - INFO - Loaded 5 records from crm_customers.csv
2024-01-15 10:30:00 - INFO - Loaded 3 records from ecommerce_customers.json
2024-01-15 10:30:01 - INFO - Total raw records: 8
2024-01-15 10:30:01 - INFO - Duplicates found: 3
2024-01-15 10:30:01 - WARNING - Record CRM005 merged with CRM001 (duplicate phone)
2024-01-15 10:30:01 - INFO - Final unique customers: 5
2024-01-15 10:30:01 - INFO - Pipeline completed successfully
```

### 💡 Concepts Used
- File I/O (CSV, JSON)
- Data structures (lists, dictionaries, sets)
- String manipulation and cleaning
- Date parsing
- Functions and modular code
- Logging
- Exception handling
- Loops and conditions

### 🔍 Hints
```python
# Hint 1: Structure your code with these functions
def extract_csv(filepath):
    pass

def extract_json(filepath):
    pass

def normalize_record(record, source):
    pass

def find_duplicates(records):
    pass

def merge_duplicates(duplicates):
    pass

def load_to_csv(records, filepath):
    pass

# Hint 2: For phone normalization
import re
clean_phone = re.sub(r'\D', '', phone)  # Remove non-digits

# Hint 3: For duplicate detection, create a "fingerprint"
def create_fingerprint(record):
    return (record['email'].lower(), record['phone'])
```

---

## 📊 Grading Rubric

Exercise is evaluated on:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Functionality** | 65% | Does the code work correctly? |
| **Code Quality** | 20% | Is the code clean, readable, and well-organized? |
| **Error Handling** | 5% | Are edge cases and errors handled gracefully? |
| **Logging & Output** | 5% | Is there appropriate logging and clear output? |
| **Documentation** | 5% | Are there comments and docstrings? |

---

## 💪 Bonus Challenge

If you complete the exercise, try these extensions:

1. **Add unit tests** for your code using `pytest`
2. **Create a web dashboard** using Flask to visualize results
3. **Containerize** your solutions with Docker
4. **Add type hints** throughout your code
5. **Implement parallel processing** for large file handling

---

