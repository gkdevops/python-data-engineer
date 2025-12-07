# Python Data Engineer - Final Capstone Exercises

## 🎯 Overview

These 6 comprehensive exercises simulate real-world data engineering scenarios. Each exercise combines multiple Python concepts and requires you to build a complete, working solution.

**Difficulty Level:** Medium (combines basics, not advanced)

**Time Estimate:** 2-4 hours per exercise

---

## Final Exercise 1: Customer Data Integration Pipeline

### 📋 Business Scenario
Your company has customer data coming from two different systems:
- **CRM System** exports data as CSV
- **E-commerce Platform** exports data as JSON

You need to build a pipeline that integrates both sources, cleans the data, removes duplicates, and produces a unified customer master file.

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

## Final Exercise 2: Data Quality Monitoring System

### 📋 Business Scenario
You're building a data quality monitoring system that runs daily checks on your data warehouse tables. The system should validate data against configurable rules, track quality metrics over time, and generate alerts when quality drops below thresholds.

### 🎯 Requirements

```
INPUT FILES:
├── data/
│   ├── orders_2024-01-15.csv
│   ├── orders_2024-01-16.csv
│   └── orders_2024-01-17.csv
├── config/
│   └── quality_rules.json
└── history/
    └── quality_metrics.json (created/updated by system)

OUTPUT FILES:
├── reports/
│   └── quality_report_2024-01-17.txt
└── alerts/
    └── alerts_2024-01-17.json
```

### 📁 Sample Input Data

**orders_2024-01-17.csv:**
```csv
order_id,customer_id,order_date,product_id,quantity,unit_price,total,status
ORD001,C100,2024-01-17,P001,2,29.99,59.98,completed
ORD002,C101,2024-01-17,P002,-1,49.99,-49.99,completed
ORD003,,2024-01-17,P001,1,29.99,29.99,completed
ORD004,C102,2024-01-17,P003,5,19.99,99.95,pending
ORD005,C103,2024-01-32,P001,3,29.99,89.97,completed
ORD006,C104,2024-01-17,,2,39.99,79.98,completed
ORD007,C105,2024-01-17,P002,1,49.99,49.99,unknown
ORD008,C106,2024-01-17,P001,2,29.99,59.98,completed
ORD009,C107,2024-01-17,P003,0,19.99,0,completed
ORD010,C108,2024-01-17,P002,1,49.99,50.99,completed
```

**quality_rules.json:**
```json
{
  "rules": [
    {
      "id": "R001",
      "name": "No Null Customer ID",
      "field": "customer_id",
      "type": "not_null",
      "severity": "critical"
    },
    {
      "id": "R002",
      "name": "No Null Product ID",
      "field": "product_id",
      "type": "not_null",
      "severity": "critical"
    },
    {
      "id": "R003",
      "name": "Positive Quantity",
      "field": "quantity",
      "type": "range",
      "min": 1,
      "max": 1000,
      "severity": "high"
    },
    {
      "id": "R004",
      "name": "Valid Status",
      "field": "status",
      "type": "allowed_values",
      "values": ["pending", "completed", "cancelled", "refunded"],
      "severity": "medium"
    },
    {
      "id": "R005",
      "name": "Valid Date Format",
      "field": "order_date",
      "type": "date_format",
      "format": "%Y-%m-%d",
      "severity": "high"
    },
    {
      "id": "R006",
      "name": "Total Calculation Check",
      "type": "calculation",
      "formula": "quantity * unit_price",
      "target_field": "total",
      "tolerance": 0.01,
      "severity": "medium"
    }
  ],
  "thresholds": {
    "critical_max_failures": 0,
    "high_max_percent": 5,
    "medium_max_percent": 10,
    "overall_min_score": 90
  }
}
```

### ✅ Tasks

1. **Rule Engine**
   - Create a flexible rule validation system
   - Support rule types: `not_null`, `range`, `allowed_values`, `date_format`, `calculation`
   - Each rule returns: pass/fail, affected records, failure details

2. **Quality Scorer**
   - Calculate quality score per rule
   - Calculate overall data quality score (percentage of passing records)
   - Track metrics by severity level

3. **Historical Tracking**
   - Store daily quality metrics in JSON
   - Compare with previous days
   - Identify trends (improving/declining)

4. **Alert Generator**
   - Generate alerts when thresholds are breached
   - Prioritize by severity
   - Include actionable details (which records failed, why)

5. **Report Generator**
   - Create human-readable quality report
   - Include summary statistics
   - Show trend compared to previous runs

### 📤 Expected Output

**quality_report_2024-01-17.txt:**
```
╔══════════════════════════════════════════════════════════════╗
║           DATA QUALITY REPORT - 2024-01-17                   ║
╠══════════════════════════════════════════════════════════════╣
║ File: orders_2024-01-17.csv                                  ║
║ Records Analyzed: 10                                         ║
║ Overall Quality Score: 74.0% ⚠️                              ║
║ Previous Day Score: 82.0% (↓ 8.0%)                          ║
╚══════════════════════════════════════════════════════════════╝

RULE RESULTS
────────────────────────────────────────────────────────────────
Rule ID  Rule Name                  Passed  Failed  Score   Severity
────────────────────────────────────────────────────────────────
R001     No Null Customer ID        9       1       90.0%   CRITICAL
R002     No Null Product ID         9       1       90.0%   CRITICAL
R003     Positive Quantity          8       2       80.0%   HIGH
R004     Valid Status               9       1       90.0%   MEDIUM
R005     Valid Date Format          9       1       90.0%   HIGH
R006     Total Calculation Check    9       1       90.0%   MEDIUM
────────────────────────────────────────────────────────────────

FAILED RECORDS DETAIL
────────────────────────────────────────────────────────────────
Order ORD002: quantity=-1 (Rule R003: Value out of range 1-1000)
Order ORD003: customer_id=NULL (Rule R001: Null value not allowed)
Order ORD005: order_date=2024-01-32 (Rule R005: Invalid date)
Order ORD006: product_id=NULL (Rule R002: Null value not allowed)
Order ORD007: status=unknown (Rule R004: Value not in allowed list)
Order ORD009: quantity=0 (Rule R003: Value out of range 1-1000)
Order ORD010: total=50.99 expected 49.99 (Rule R006: Calculation mismatch)

ALERTS GENERATED: 2
────────────────────────────────────────────────────────────────
🚨 CRITICAL: Rule R001 has failures (threshold: 0, actual: 1)
🚨 CRITICAL: Rule R002 has failures (threshold: 0, actual: 1)

TREND ANALYSIS (Last 3 Days)
────────────────────────────────────────────────────────────────
2024-01-15: 85.0% ████████░░
2024-01-16: 82.0% ████████░░
2024-01-17: 74.0% ███████░░░ ⚠️ Declining trend detected
```

**alerts_2024-01-17.json:**
```json
{
  "generated_at": "2024-01-17T10:30:00Z",
  "alerts": [
    {
      "id": "ALT001",
      "severity": "critical",
      "rule_id": "R001",
      "message": "Critical rule 'No Null Customer ID' has 1 failures",
      "affected_records": ["ORD003"],
      "action_required": "Investigate null customer_id in order ORD003"
    },
    {
      "id": "ALT002",
      "severity": "critical",
      "rule_id": "R002",
      "message": "Critical rule 'No Null Product ID' has 1 failures",
      "affected_records": ["ORD006"],
      "action_required": "Investigate null product_id in order ORD006"
    }
  ]
}
```

### 💡 Concepts Used
- JSON configuration files
- CSV processing
- Functions with parameters
- Dictionaries for rule storage
- Date validation
- Mathematical calculations
- File I/O
- Logging
- String formatting
- Conditional logic

### 🔍 Hints
```python
# Hint 1: Create a rule validator class or function factory
def create_validator(rule):
    rule_type = rule['type']
    
    if rule_type == 'not_null':
        def validator(value):
            return value is not None and value != ''
        return validator
    elif rule_type == 'range':
        def validator(value):
            return rule['min'] <= float(value) <= rule['max']
        return validator
    # ... etc

# Hint 2: For date validation
from datetime import datetime
def is_valid_date(date_str, format_str):
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False

# Hint 3: Calculate quality score
quality_score = (passed_count / total_count) * 100
```

---

## Final Exercise 3: REST API Data Collector

### 📋 Business Scenario
Your company needs to collect product and inventory data from a supplier's REST API. The API has rate limiting (max 10 requests per minute), pagination, and occasionally returns errors. You need to build a robust data collector that handles all these scenarios.

### 🎯 Requirements

```
INPUT:
├── config/
│   └── api_config.json

OUTPUT:
├── data/
│   ├── products_2024-01-17.json
│   └── inventory_2024-01-17.csv
├── logs/
│   └── api_collector.log
└── state/
    └── last_run.json (tracks progress for resume capability)
```

### 📁 Configuration & Mock API

**api_config.json:**
```json
{
  "base_url": "https://api.supplier.com/v1",
  "endpoints": {
    "products": "/products",
    "inventory": "/inventory"
  },
  "auth": {
    "api_key": "your-api-key-here"
  },
  "rate_limit": {
    "requests_per_minute": 10,
    "retry_after_seconds": 60
  },
  "pagination": {
    "page_size": 100,
    "max_pages": 50
  }
}
```

**Since we don't have a real API, create a mock API simulator:**

```python
# mock_api.py - Create this to simulate API responses

import random
import time

class MockSupplierAPI:
    def __init__(self):
        self.request_count = 0
        self.last_request_time = 0
        self.products = self._generate_products(350)  # 350 products
        self.inventory = self._generate_inventory()
        
    def _generate_products(self, count):
        categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
        products = []
        for i in range(1, count + 1):
            products.append({
                'product_id': f'PROD{i:04d}',
                'name': f'Product {i}',
                'category': random.choice(categories),
                'price': round(random.uniform(9.99, 299.99), 2),
                'active': random.choice([True, True, True, False])  # 75% active
            })
        return products
    
    def _generate_inventory(self):
        inventory = []
        for product in self.products:
            if product['active']:
                inventory.append({
                    'product_id': product['product_id'],
                    'warehouse': random.choice(['WEST', 'EAST', 'CENTRAL']),
                    'quantity': random.randint(0, 500),
                    'last_updated': '2024-01-17T08:00:00Z'
                })
        return inventory
    
    def get(self, endpoint, params=None):
        """Simulate API GET request"""
        self.request_count += 1
        
        # Simulate rate limiting (10% chance)
        if random.random() < 0.10:
            return {'status': 429, 'error': 'Rate limit exceeded', 'retry_after': 5}
        
        # Simulate server error (5% chance)
        if random.random() < 0.05:
            return {'status': 500, 'error': 'Internal server error'}
        
        # Simulate timeout (3% chance)
        if random.random() < 0.03:
            time.sleep(0.1)  # Simulate delay
            return {'status': 408, 'error': 'Request timeout'}
        
        # Success response with pagination
        page = params.get('page', 1) if params else 1
        page_size = params.get('page_size', 100) if params else 100
        
        if 'products' in endpoint:
            data = self.products
        elif 'inventory' in endpoint:
            data = self.inventory
        else:
            return {'status': 404, 'error': 'Endpoint not found'}
        
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        page_data = data[start_idx:end_idx]
        
        return {
            'status': 200,
            'data': page_data,
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_items': len(data),
                'total_pages': (len(data) + page_size - 1) // page_size,
                'has_next': end_idx < len(data)
            }
        }
```

### ✅ Tasks

1. **API Client Class**
   - Create a reusable API client
   - Handle authentication (API key in headers)
   - Implement automatic retry with exponential backoff
   - Respect rate limits (wait if limit exceeded)
   - Log all requests and responses

2. **Pagination Handler**
   - Automatically fetch all pages
   - Track progress (current page / total pages)
   - Support resume from last successful page if interrupted

3. **Error Handler**
   - Handle different HTTP status codes (429, 500, 408, etc.)
   - Implement retry logic with max attempts
   - Log errors with context

4. **Data Collector**
   - Collect all products and save as JSON
   - Collect all inventory and save as CSV
   - Track collection statistics

5. **State Management**
   - Save progress after each successful page
   - Allow resume from last state if script restarts
   - Clean up state file on successful completion

### 📤 Expected Output

**api_collector.log:**
```
2024-01-17 10:00:00 - INFO - Starting API data collection
2024-01-17 10:00:00 - INFO - Loading configuration from api_config.json
2024-01-17 10:00:00 - INFO - Fetching products endpoint
2024-01-17 10:00:00 - DEBUG - GET /products?page=1&page_size=100 - Status: 200
2024-01-17 10:00:01 - DEBUG - GET /products?page=2&page_size=100 - Status: 200
2024-01-17 10:00:02 - WARNING - GET /products?page=3 - Status: 429 (Rate Limited)
2024-01-17 10:00:02 - INFO - Rate limited. Waiting 5 seconds before retry...
2024-01-17 10:00:07 - DEBUG - GET /products?page=3&page_size=100 - Status: 200 (Retry successful)
2024-01-17 10:00:08 - DEBUG - GET /products?page=4&page_size=100 - Status: 200
2024-01-17 10:00:08 - INFO - Products collection complete: 350 items in 4 pages
2024-01-17 10:00:09 - INFO - Fetching inventory endpoint
2024-01-17 10:00:09 - DEBUG - GET /inventory?page=1&page_size=100 - Status: 200
2024-01-17 10:00:10 - ERROR - GET /inventory?page=2 - Status: 500 (Server Error)
2024-01-17 10:00:10 - INFO - Retrying in 2 seconds (attempt 1/3)
2024-01-17 10:00:12 - DEBUG - GET /inventory?page=2&page_size=100 - Status: 200 (Retry successful)
2024-01-17 10:00:13 - DEBUG - GET /inventory?page=3&page_size=100 - Status: 200
2024-01-17 10:00:13 - INFO - Inventory collection complete: 263 items in 3 pages
2024-01-17 10:00:13 - INFO - Collection complete. Summary:
2024-01-17 10:00:13 - INFO -   Products: 350 records saved to products_2024-01-17.json
2024-01-17 10:00:13 - INFO -   Inventory: 263 records saved to inventory_2024-01-17.csv
2024-01-17 10:00:13 - INFO -   Total API calls: 9 (2 retries)
2024-01-17 10:00:13 - INFO -   Duration: 13.2 seconds
```

**products_2024-01-17.json:**
```json
{
  "collected_at": "2024-01-17T10:00:13Z",
  "total_records": 350,
  "products": [
    {
      "product_id": "PROD0001",
      "name": "Product 1",
      "category": "Electronics",
      "price": 149.99,
      "active": true
    },
    ...
  ]
}
```

**inventory_2024-01-17.csv:**
```csv
product_id,warehouse,quantity,last_updated
PROD0001,WEST,234,2024-01-17T08:00:00Z
PROD0002,EAST,56,2024-01-17T08:00:00Z
PROD0003,CENTRAL,189,2024-01-17T08:00:00Z
...
```

**last_run.json (during collection):**
```json
{
  "run_id": "run_20240117_100000",
  "started_at": "2024-01-17T10:00:00Z",
  "endpoints": {
    "products": {
      "status": "completed",
      "last_page": 4,
      "total_pages": 4,
      "records_collected": 350
    },
    "inventory": {
      "status": "in_progress",
      "last_page": 2,
      "total_pages": 3,
      "records_collected": 200
    }
  }
}
```

### 💡 Concepts Used
- Classes and object-oriented design
- HTTP concepts (simulated)
- JSON and CSV file handling
- Exception handling with retries
- Logging
- Configuration management
- State management
- Time and sleep functions
- Pagination logic

### 🔍 Hints
```python
# Hint 1: Exponential backoff for retries
import time

def retry_with_backoff(func, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        result = func()
        if result['status'] == 200:
            return result
        delay = base_delay * (2 ** attempt)  # 1, 2, 4 seconds
        time.sleep(delay)
    raise Exception("Max retries exceeded")

# Hint 2: Pagination loop
def collect_all_pages(api, endpoint):
    all_data = []
    page = 1
    while True:
        response = api.get(endpoint, {'page': page, 'page_size': 100})
        all_data.extend(response['data'])
        if not response['pagination']['has_next']:
            break
        page += 1
    return all_data

# Hint 3: State management
def save_state(state, filepath='last_run.json'):
    with open(filepath, 'w') as f:
        json.dump(state, f, indent=2)

def load_state(filepath='last_run.json'):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return None
```

---

## Final Exercise 4: Server Log Analytics Pipeline

### 📋 Business Scenario
Your DevOps team needs a tool to analyze web server access logs. The tool should parse logs, extract metrics, identify patterns, detect anomalies, and generate daily reports. This is crucial for monitoring application health and detecting potential issues.

### 🎯 Requirements

```
INPUT:
├── logs/
│   ├── access_2024-01-15.log
│   ├── access_2024-01-16.log
│   └── access_2024-01-17.log

OUTPUT:
├── reports/
│   └── analytics_2024-01-17.txt
├── metrics/
│   └── hourly_metrics_2024-01-17.csv
└── alerts/
    └── anomalies_2024-01-17.json
```

### 📁 Sample Input Data

**access_2024-01-17.log** (Apache Combined Log Format):
```
192.168.1.100 - user1 [17/Jan/2024:08:15:23 +0000] "GET /api/products HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
192.168.1.101 - - [17/Jan/2024:08:15:24 +0000] "GET /api/products/123 HTTP/1.1" 200 567 "-" "Mozilla/5.0"
192.168.1.102 - user2 [17/Jan/2024:08:15:25 +0000] "POST /api/orders HTTP/1.1" 201 890 "-" "Mozilla/5.0"
192.168.1.100 - user1 [17/Jan/2024:08:15:26 +0000] "GET /api/cart HTTP/1.1" 401 123 "-" "Mozilla/5.0"
10.0.0.50 - - [17/Jan/2024:08:15:27 +0000] "GET /admin/config HTTP/1.1" 403 89 "-" "curl/7.68.0"
192.168.1.103 - - [17/Jan/2024:08:15:28 +0000] "GET /api/products HTTP/1.1" 500 234 "-" "Mozilla/5.0"
192.168.1.104 - user3 [17/Jan/2024:08:15:29 +0000] "GET /api/products?page=2 HTTP/1.1" 200 1456 "-" "Mozilla/5.0"
192.168.1.100 - user1 [17/Jan/2024:08:15:30 +0000] "DELETE /api/products/456 HTTP/1.1" 403 78 "-" "Mozilla/5.0"
10.0.0.51 - - [17/Jan/2024:08:15:31 +0000] "GET /api/../../etc/passwd HTTP/1.1" 400 45 "-" "curl/7.68.0"
192.168.1.105 - - [17/Jan/2024:08:15:32 +0000] "GET /api/products HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

**Generate more log lines (at least 1000) using a script for realistic testing.**

### ✅ Tasks

1. **Log Parser**
   - Parse Apache Combined Log Format using regex
   - Extract: IP, user, timestamp, method, path, status, bytes, user_agent
   - Handle malformed lines gracefully

2. **Metrics Calculator**
   - Requests per hour/minute
   - Response status code distribution
   - Top 10 endpoints by request count
   - Top 10 IPs by request count
   - Average response size by endpoint
   - Error rate (4xx and 5xx responses)

3. **Anomaly Detector**
   - Detect unusual traffic patterns:
     - More than 100 requests from single IP in 1 minute
     - Error rate > 10% for any endpoint
     - Suspicious paths (SQL injection patterns, path traversal)
     - Unusual user agents (automated scripts)
   - Score each anomaly by severity

4. **Report Generator**
   - Create comprehensive daily report
   - Include visualizations using ASCII charts
   - Compare with previous day metrics
   - Highlight significant changes

5. **Security Alerts**
   - Flag potential security issues
   - Identify suspicious patterns
   - Generate actionable alerts

### 📤 Expected Output

**analytics_2024-01-17.txt:**
```
╔═══════════════════════════════════════════════════════════════════╗
║              SERVER LOG ANALYTICS REPORT                          ║
║                    2024-01-17                                     ║
╠═══════════════════════════════════════════════════════════════════╣
║  Total Requests: 15,234        Previous Day: 14,892 (↑ 2.3%)     ║
║  Unique IPs: 1,247             Unique Users: 423                  ║
║  Error Rate: 4.2%              Previous Day: 3.8% (↑ 0.4%)       ║
║  Avg Response Size: 2.3 KB     Avg Response Time: N/A            ║
╚═══════════════════════════════════════════════════════════════════╝

REQUEST STATUS DISTRIBUTION
─────────────────────────────────────────────────────────────────────
2xx Success    ████████████████████████████████████████  12,456 (81.8%)
3xx Redirect   ████                                         612 (4.0%)
4xx Client Err ██████████                                 1,523 (10.0%)
5xx Server Err ███                                          643 (4.2%)

HOURLY TRAFFIC PATTERN
─────────────────────────────────────────────────────────────────────
00:00 ███                          234
01:00 ██                           156
02:00 █                             89
03:00 █                             67
04:00 █                             78
05:00 ██                           134
06:00 ████                         345
07:00 ████████                     689
08:00 ████████████████           1,234
09:00 ██████████████████████     1,892   ← Peak Hour
10:00 █████████████████████      1,756
11:00 ███████████████████        1,623
12:00 ████████████████           1,345
... (continues)

TOP 10 ENDPOINTS BY REQUESTS
─────────────────────────────────────────────────────────────────────
Rank  Endpoint                      Requests   Errors   Error %
─────────────────────────────────────────────────────────────────────
1     GET /api/products              4,567      123      2.7%
2     GET /api/products/{id}         3,234       89      2.8%
3     POST /api/orders               1,892       45      2.4%
4     GET /api/cart                  1,456      234     16.1%  ⚠️
5     GET /api/users/profile         1,123       23      2.0%
6     POST /api/auth/login             987       56      5.7%
7     GET /api/categories              876       12      1.4%
8     PUT /api/cart/{id}               654       78     11.9%  ⚠️
9     GET /api/search                  543       34      6.3%
10    DELETE /api/cart/{id}            234       12      5.1%

TOP 10 CLIENT IPs
─────────────────────────────────────────────────────────────────────
IP Address       Requests   Errors   User          Last Seen
─────────────────────────────────────────────────────────────────────
192.168.1.100       567       23     user1         08:45:23
192.168.1.101       456       12     user234       09:12:45
10.0.0.50           234      189     -             08:15:27   ⚠️
192.168.1.102       198        5     user567       10:23:12
... (continues)

ANOMALIES DETECTED: 3
─────────────────────────────────────────────────────────────────────
🚨 CRITICAL: Potential path traversal attack
   IP: 10.0.0.51
   Path: /api/../../etc/passwd
   Count: 12 attempts
   Time: 08:15:31 - 08:20:45

⚠️ HIGH: High error rate on endpoint
   Endpoint: GET /api/cart
   Error Rate: 16.1% (threshold: 10%)
   Sample Errors: 401 Unauthorized (majority)

⚠️ MEDIUM: Suspicious user agent activity
   User Agent: curl/7.68.0
   Requests: 234 (15.3% error rate)
   Accessing: /admin/* endpoints

SECURITY RECOMMENDATIONS
─────────────────────────────────────────────────────────────────────
1. Block IP 10.0.0.51 - Multiple path traversal attempts
2. Investigate /api/cart 401 errors - Possible auth issue
3. Review admin endpoint access from curl user agents
```

**hourly_metrics_2024-01-17.csv:**
```csv
hour,total_requests,successful,errors,error_rate,unique_ips,avg_response_bytes
0,234,220,14,5.98,45,2345
1,156,148,8,5.13,34,1987
2,89,85,4,4.49,23,2156
...
```

**anomalies_2024-01-17.json:**
```json
{
  "report_date": "2024-01-17",
  "anomalies": [
    {
      "id": "ANOM001",
      "type": "security",
      "severity": "critical",
      "description": "Path traversal attack detected",
      "details": {
        "source_ip": "10.0.0.51",
        "pattern": "/api/../../etc/passwd",
        "occurrences": 12,
        "first_seen": "08:15:31",
        "last_seen": "08:20:45"
      },
      "recommended_action": "Block IP immediately"
    },
    {
      "id": "ANOM002",
      "type": "performance",
      "severity": "high",
      "description": "High error rate on endpoint",
      "details": {
        "endpoint": "GET /api/cart",
        "error_rate": 16.1,
        "threshold": 10.0,
        "primary_error": "401 Unauthorized"
      },
      "recommended_action": "Investigate authentication flow"
    }
  ]
}
```

### 💡 Concepts Used
- Regular expressions (regex) for log parsing
- Datetime parsing and manipulation
- Collections (dictionaries, Counter)
- Statistical calculations
- File I/O
- String formatting
- Pattern matching
- Data aggregation

### 🔍 Hints
```python
# Hint 1: Regex pattern for Apache Combined Log Format
import re

log_pattern = r'(\S+) \S+ (\S+) \[([^\]]+)\] "(\S+) (\S+) \S+" (\d+) (\d+|-) "[^"]*" "([^"]*)"'

def parse_log_line(line):
    match = re.match(log_pattern, line)
    if match:
        return {
            'ip': match.group(1),
            'user': match.group(2) if match.group(2) != '-' else None,
            'timestamp': match.group(3),
            'method': match.group(4),
            'path': match.group(5),
            'status': int(match.group(6)),
            'bytes': int(match.group(7)) if match.group(7) != '-' else 0,
            'user_agent': match.group(8)
        }
    return None

# Hint 2: Detect suspicious patterns
suspicious_patterns = [
    r'\.\./\.\.',           # Path traversal
    r'(?:union|select)',     # SQL injection
    r'<script>',             # XSS
    r'/etc/passwd',          # System file access
]

def is_suspicious(path):
    return any(re.search(p, path, re.I) for p in suspicious_patterns)

# Hint 3: ASCII bar chart
def ascii_bar(value, max_value, width=40):
    filled = int((value / max_value) * width)
    return '█' * filled + '░' * (width - filled)
```

---

## Final Exercise 5: Multi-Source Data Reconciliation Tool

### 📋 Business Scenario
Your company's financial data exists in three systems: the ERP system (source of truth for transactions), the CRM system (customer information), and the Data Warehouse (analytical reports). Monthly reconciliation is required to ensure data consistency. Build a tool that automates this reconciliation process.

### 🎯 Requirements

```
INPUT:
├── data/
│   ├── erp_transactions_202401.csv      (Source of truth)
│   ├── crm_customer_orders_202401.csv   (CRM view)
│   └── dw_sales_facts_202401.csv        (Data warehouse)
├── config/
│   └── reconciliation_rules.json

OUTPUT:
├── reports/
│   ├── reconciliation_summary_202401.txt
│   └── reconciliation_detail_202401.csv
├── issues/
│   └── discrepancies_202401.json
└── audit/
    └── reconciliation_audit_202401.log
```

### 📁 Sample Input Data

**erp_transactions_202401.csv (Source of Truth):**
```csv
transaction_id,customer_id,order_date,product_id,quantity,unit_price,total_amount,status
TXN001,CUST100,2024-01-05,PROD001,2,49.99,99.98,completed
TXN002,CUST101,2024-01-05,PROD002,1,29.99,29.99,completed
TXN003,CUST100,2024-01-06,PROD003,5,19.99,99.95,completed
TXN004,CUST102,2024-01-07,PROD001,1,49.99,49.99,completed
TXN005,CUST103,2024-01-08,PROD004,3,39.99,119.97,refunded
TXN006,CUST104,2024-01-10,PROD002,2,29.99,59.98,completed
TXN007,CUST100,2024-01-12,PROD005,1,99.99,99.99,completed
TXN008,CUST105,2024-01-15,PROD001,4,49.99,199.96,pending
TXN009,CUST101,2024-01-18,PROD003,2,19.99,39.98,completed
TXN010,CUST106,2024-01-20,PROD002,1,29.99,29.99,cancelled
```

**crm_customer_orders_202401.csv:**
```csv
order_id,customer_id,customer_name,order_date,total_value,order_status
TXN001,CUST100,John Smith,2024-01-05,99.98,completed
TXN002,CUST101,Jane Doe,2024-01-05,29.99,completed
TXN003,CUST100,John Smith,2024-01-06,99.95,completed
TXN004,CUST102,Bob Wilson,2024-01-07,49.99,completed
TXN005,CUST103,Alice Brown,2024-01-08,119.97,completed
TXN006,CUST104,Charlie Davis,2024-01-10,59.98,completed
TXN007,CUST100,John Smith,2024-01-12,99.99,completed
TXN009,CUST101,Jane Doe,2024-01-18,39.98,completed
TXN011,CUST107,New Customer,2024-01-22,79.99,completed
```

**dw_sales_facts_202401.csv:**
```csv
fact_id,transaction_id,customer_key,date_key,product_key,quantity,amount,status
F001,TXN001,100,20240105,1,2,99.98,completed
F002,TXN002,101,20240105,2,1,29.99,completed
F003,TXN003,100,20240106,3,5,99.95,completed
F004,TXN004,102,20240107,1,1,49.99,completed
F005,TXN005,103,20240108,4,3,119.97,completed
F006,TXN006,104,20240110,2,2,60.00,completed
F007,TXN007,100,20240112,5,1,99.99,completed
F008,TXN008,105,20240115,1,4,199.96,completed
F009,TXN009,101,20240118,3,2,39.98,completed
```

**reconciliation_rules.json:**
```json
{
  "comparisons": [
    {
      "name": "ERP vs CRM",
      "source": "erp",
      "target": "crm",
      "key_fields": ["transaction_id"],
      "compare_fields": [
        {"source": "total_amount", "target": "total_value", "tolerance": 0.01},
        {"source": "status", "target": "order_status"}
      ]
    },
    {
      "name": "ERP vs DW",
      "source": "erp",
      "target": "dw",
      "key_fields": ["transaction_id"],
      "compare_fields": [
        {"source": "total_amount", "target": "amount", "tolerance": 0.01},
        {"source": "quantity", "target": "quantity"},
        {"source": "status", "target": "status"}
      ]
    }
  ],
  "aggregations": [
    {
      "name": "Monthly Totals",
      "group_by": null,
      "metric": "total_amount",
      "tolerance_percent": 0.1
    },
    {
      "name": "Daily Totals",
      "group_by": "order_date",
      "metric": "total_amount",
      "tolerance_percent": 0.5
    }
  ]
}
```

### ✅ Tasks

1. **Data Loader**
   - Load all three data sources
   - Normalize column names and data types
   - Handle missing values

2. **Record-Level Reconciliation**
   - Match records across systems using key fields
   - Identify missing records (in source but not target, and vice versa)
   - Compare values with configurable tolerance
   - Categorize discrepancies by type and severity

3. **Aggregate Reconciliation**
   - Compare totals across systems
   - Compare by date, customer, product
   - Calculate variance percentages

4. **Discrepancy Classifier**
   - Classify issues by type:
     - Missing records
     - Value mismatches
     - Status inconsistencies
     - Timing differences
   - Assign severity (critical, high, medium, low)
   - Suggest root cause

5. **Report Generator**
   - Executive summary with key metrics
   - Detailed discrepancy listing
   - Trend analysis (if historical data available)
   - Recommended actions

### 📤 Expected Output

**reconciliation_summary_202401.txt:**
```
╔═══════════════════════════════════════════════════════════════════╗
║           MONTHLY DATA RECONCILIATION REPORT                      ║
║                   January 2024                                    ║
╠═══════════════════════════════════════════════════════════════════╣
║  Period: 2024-01-01 to 2024-01-31                                 ║
║  Run Date: 2024-02-01 10:30:00                                    ║
║  Status: ISSUES FOUND ⚠️                                          ║
╚═══════════════════════════════════════════════════════════════════╝

SYSTEM COMPARISON SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        ERP (Source)     CRM          Data Warehouse
────────────────────────────────────────────────────────────────────
Total Records           10               9            9
Completed Orders        7                8            8
Total Amount            $829.78          $779.81      $799.80
Unique Customers        7                7            7

RECONCILIATION RESULTS BY COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ERP vs CRM
──────────
Match Rate: 77.8% (7/9 records matched perfectly)
├── ✓ Matched: 7 records
├── ⚠ Missing in CRM: 2 records (TXN008, TXN010)
├── ⚠ Missing in ERP: 1 record (TXN011)
├── ✗ Value Mismatch: 1 record
└── ✗ Status Mismatch: 1 record

ERP vs Data Warehouse
─────────────────────
Match Rate: 88.9% (8/9 records matched perfectly)
├── ✓ Matched: 8 records
├── ⚠ Missing in DW: 1 record (TXN010)
├── ⚠ Missing in ERP: 0 records
└── ✗ Value Mismatch: 1 record

AGGREGATE RECONCILIATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Monthly Totals (Completed Orders Only)
──────────────────────────────────────
System              Amount          Variance
ERP                 $679.82         (baseline)
CRM                 $659.83         -$19.99 (-2.9%) ⚠️
Data Warehouse      $679.84         +$0.02 (0.0%) ✓

DISCREPANCIES DETAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID    Severity   Type              Transaction   Systems      Details
────────────────────────────────────────────────────────────────────
D001  HIGH       Missing Record    TXN008        ERP→CRM      Pending order not synced to CRM
D002  LOW        Missing Record    TXN010        ERP→CRM      Cancelled order not in CRM
D003  CRITICAL   Ghost Record      TXN011        CRM Only     Order exists in CRM but not ERP
D004  MEDIUM     Value Mismatch    TXN005        ERP↔CRM      Status: refunded vs completed
D005  LOW        Value Mismatch    TXN006        ERP↔DW       Amount: $59.98 vs $60.00

ROOT CAUSE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Issue Pattern: Missing Pending/Cancelled Orders in CRM
Likely Cause: CRM only syncs completed orders
Recommendation: Verify CRM integration rules

Issue Pattern: Status Mismatch for Refunds
Likely Cause: Refund status not propagating to CRM
Recommendation: Review refund workflow integration

Issue Pattern: Ghost Record in CRM (TXN011)
Likely Cause: Possible data entry directly in CRM
Recommendation: Investigate and create ERP transaction

RECOMMENDED ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Priority  Action
────────────────────────────────────────────────────────────────────
1 (HIGH)  Investigate TXN011 ghost record in CRM - potential fraud risk
2 (HIGH)  Fix refund status sync between ERP and CRM
3 (MED)   Review DW ETL rounding logic (TXN006 amount variance)
4 (LOW)   Evaluate syncing pending/cancelled orders to CRM
```

**discrepancies_202401.json:**
```json
{
  "report_id": "RECON-202401-001",
  "generated_at": "2024-02-01T10:30:00Z",
  "period": "2024-01",
  "summary": {
    "total_discrepancies": 5,
    "by_severity": {"critical": 1, "high": 1, "medium": 1, "low": 2},
    "by_type": {"missing_record": 3, "value_mismatch": 2}
  },
  "discrepancies": [
    {
      "id": "D001",
      "type": "missing_record",
      "severity": "high",
      "transaction_id": "TXN008",
      "source_system": "ERP",
      "target_system": "CRM",
      "description": "Record exists in ERP but not in CRM",
      "source_values": {
        "total_amount": 199.96,
        "status": "pending"
      },
      "target_values": null,
      "probable_cause": "Pending orders not synced",
      "recommended_action": "Verify CRM sync rules for pending orders"
    }
  ]
}
```

### 💡 Concepts Used
- Multiple file processing
- Data comparison algorithms
- Dictionary operations
- Set operations (for finding missing records)
- Tolerance-based number comparison
- Data aggregation
- Report generation
- Logging and auditing

### 🔍 Hints
```python
# Hint 1: Find missing records using sets
erp_ids = set(erp_data['transaction_id'])
crm_ids = set(crm_data['order_id'])
missing_in_crm = erp_ids - crm_ids
missing_in_erp = crm_ids - erp_ids

# Hint 2: Compare with tolerance
def values_match(val1, val2, tolerance=0.01):
    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        return abs(val1 - val2) <= tolerance
    return str(val1).lower() == str(val2).lower()

# Hint 3: Create lookup dictionaries for fast matching
erp_lookup = {row['transaction_id']: row for row in erp_data}
crm_lookup = {row['order_id']: row for row in crm_data}

# Hint 4: Aggregate by group
from collections import defaultdict
daily_totals = defaultdict(float)
for row in erp_data:
    daily_totals[row['order_date']] += row['total_amount']
```

---

## Final Exercise 6: Automated Data Pipeline with Scheduling Simulation

### 📋 Business Scenario
Build a complete automated data pipeline that simulates a production ETL workflow. The pipeline should:
- Run on a schedule (simulated)
- Process data from multiple sources
- Apply transformations
- Load to a destination
- Handle failures with retries
- Send notifications (simulated)
- Maintain comprehensive logging and metrics

### 🎯 Requirements

```
PROJECT STRUCTURE:
├── pipeline/
│   ├── __init__.py
│   ├── config.py
│   ├── extractors.py
│   ├── transformers.py
│   ├── loaders.py
│   ├── scheduler.py
│   ├── notifier.py
│   └── metrics.py
├── data/
│   ├── input/
│   ├── staging/
│   └── output/
├── logs/
├── config/
│   └── pipeline_config.json
└── main.py
```

### 📁 Configuration

**pipeline_config.json:**
```json
{
  "pipeline_name": "daily_sales_pipeline",
  "version": "1.0.0",
  "schedule": {
    "type": "daily",
    "time": "02:00",
    "timezone": "UTC"
  },
  "extract": {
    "sources": [
      {
        "name": "sales_orders",
        "type": "csv",
        "path": "data/input/sales_orders_{date}.csv",
        "required": true
      },
      {
        "name": "product_catalog",
        "type": "json",
        "path": "data/input/products.json",
        "required": true
      },
      {
        "name": "customer_data",
        "type": "csv",
        "path": "data/input/customers.csv",
        "required": true
      }
    ]
  },
  "transform": {
    "steps": [
      {"name": "clean_nulls", "type": "cleaner", "config": {"strategy": "drop"}},
      {"name": "enrich_products", "type": "joiner", "config": {"left": "sales_orders", "right": "product_catalog", "on": "product_id"}},
      {"name": "enrich_customers", "type": "joiner", "config": {"left": "enriched", "right": "customer_data", "on": "customer_id"}},
      {"name": "calculate_metrics", "type": "aggregator", "config": {"group_by": ["date", "product_category"], "metrics": ["total_revenue", "order_count"]}},
      {"name": "format_output", "type": "formatter", "config": {"date_format": "%Y-%m-%d", "currency_format": "USD"}}
    ]
  },
  "load": {
    "destinations": [
      {
        "name": "daily_summary",
        "type": "csv",
        "path": "data/output/daily_summary_{date}.csv"
      },
      {
        "name": "metrics_db",
        "type": "sqlite",
        "path": "data/output/metrics.db",
        "table": "daily_metrics"
      }
    ]
  },
  "error_handling": {
    "max_retries": 3,
    "retry_delay_seconds": 5,
    "on_failure": "notify_and_stop"
  },
  "notifications": {
    "on_success": ["log", "email"],
    "on_failure": ["log", "email", "slack"],
    "recipients": {
      "email": ["data-team@company.com"],
      "slack": ["#data-alerts"]
    }
  }
}
```

### ✅ Tasks

1. **Pipeline Framework**
   - Create base classes for Extract, Transform, Load steps
   - Implement a Pipeline class that orchestrates all steps
   - Support configuration-driven pipeline construction

2. **Extractors Module**
   - CSVExtractor: Read CSV files with date placeholders
   - JSONExtractor: Read and parse JSON files
   - Handle missing files gracefully

3. **Transformers Module**
   - CleanerTransformer: Handle nulls, duplicates
   - JoinerTransformer: Join datasets on keys
   - AggregatorTransformer: Group by and calculate metrics
   - FormatterTransformer: Format dates, currencies

4. **Loaders Module**
   - CSVLoader: Write to CSV files
   - SQLiteLoader: Insert into SQLite database
   - Handle schema creation and updates

5. **Scheduler (Simulated)**
   - Check if it's time to run based on schedule
   - Track last run time
   - Support manual trigger

6. **Error Handling & Retries**
   - Wrap operations in try/except
   - Implement retry with exponential backoff
   - Track failed attempts

7. **Metrics & Monitoring**
   - Track execution time per step
   - Track records processed
   - Calculate success/failure rates
   - Store metrics history

8. **Notifications (Simulated)**
   - Log-based notifications
   - Format success/failure messages
   - Include relevant metrics

### 📤 Expected Output

**Pipeline Execution Log (logs/pipeline_2024-01-17.log):**
```
════════════════════════════════════════════════════════════════════
                 PIPELINE EXECUTION STARTED
             daily_sales_pipeline v1.0.0
             Run ID: RUN-20240117-020000
             Triggered: Scheduled (daily @ 02:00 UTC)
════════════════════════════════════════════════════════════════════

[02:00:00] INFO  | Starting pipeline execution
[02:00:00] INFO  | Loading configuration from pipeline_config.json

━━━ EXTRACT PHASE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[02:00:01] INFO  | Extracting: sales_orders (CSV)
[02:00:01] INFO  |   Path: data/input/sales_orders_2024-01-17.csv
[02:00:02] INFO  |   Records: 1,247
[02:00:02] INFO  | Extracting: product_catalog (JSON)
[02:00:02] INFO  |   Path: data/input/products.json
[02:00:02] INFO  |   Records: 156
[02:00:02] INFO  | Extracting: customer_data (CSV)
[02:00:02] INFO  |   Path: data/input/customers.csv
[02:00:03] INFO  |   Records: 892
[02:00:03] INFO  | Extract phase complete: 3/3 sources loaded

━━━ TRANSFORM PHASE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[02:00:03] INFO  | Step 1/5: clean_nulls
[02:00:03] INFO  |   Input: 1,247 records
[02:00:03] INFO  |   Nulls dropped: 23
[02:00:03] INFO  |   Output: 1,224 records
[02:00:04] INFO  | Step 2/5: enrich_products
[02:00:04] INFO  |   Joining sales_orders with product_catalog on product_id
[02:00:04] INFO  |   Matched: 1,220 | Unmatched: 4
[02:00:04] WARN  |   4 records had unknown product_id
[02:00:05] INFO  | Step 3/5: enrich_customers
[02:00:05] INFO  |   Joining with customer_data on customer_id
[02:00:05] INFO  |   Matched: 1,218 | Unmatched: 2
[02:00:05] INFO  | Step 4/5: calculate_metrics
[02:00:05] INFO  |   Grouping by: date, product_category
[02:00:05] INFO  |   Aggregations: total_revenue, order_count
[02:00:06] INFO  |   Output groups: 12
[02:00:06] INFO  | Step 5/5: format_output
[02:00:06] INFO  |   Formatting dates and currency
[02:00:06] INFO  | Transform phase complete: 5/5 steps executed

━━━ LOAD PHASE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[02:00:06] INFO  | Loading: daily_summary (CSV)
[02:00:06] INFO  |   Path: data/output/daily_summary_2024-01-17.csv
[02:00:07] INFO  |   Records written: 12
[02:00:07] INFO  | Loading: metrics_db (SQLite)
[02:00:07] INFO  |   Table: daily_metrics
[02:00:07] INFO  |   Records inserted: 12
[02:00:07] INFO  | Load phase complete: 2/2 destinations loaded

════════════════════════════════════════════════════════════════════
                 PIPELINE EXECUTION SUMMARY
════════════════════════════════════════════════════════════════════
Status:           SUCCESS ✓
Duration:         7.23 seconds
Records Input:    1,247 (sales orders)
Records Output:   1,218 (enriched) | 12 (aggregated)
Records Dropped:  29 (2.3%)

Step Performance:
  Extract:        3.12s (43.2%)
  Transform:      3.05s (42.2%)
  Load:           1.06s (14.6%)

Quality Metrics:
  Null Records:   23 dropped
  Unmatched Joins: 6 total
  Data Coverage:  97.7%

════════════════════════════════════════════════════════════════════
              NOTIFICATION SENT
              To: data-team@company.com
              Channel: #data-alerts (slack)
              Message: daily_sales_pipeline completed successfully
════════════════════════════════════════════════════════════════════
```

**Output File (data/output/daily_summary_2024-01-17.csv):**
```csv
date,product_category,order_count,total_revenue,avg_order_value
2024-01-17,Electronics,234,45678.90,195.21
2024-01-17,Clothing,189,12345.67,65.32
2024-01-17,Home & Garden,156,23456.78,150.36
2024-01-17,Sports,123,8901.23,72.37
...
```

**Metrics Database (data/output/metrics.db - schema):**
```sql
CREATE TABLE daily_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date DATE,
    run_id TEXT,
    product_category TEXT,
    order_count INTEGER,
    total_revenue REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pipeline_runs (
    run_id TEXT PRIMARY KEY,
    pipeline_name TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT,
    records_processed INTEGER,
    records_output INTEGER,
    error_message TEXT
);
```

### 💡 Concepts Used
- Object-oriented programming (classes, inheritance)
- Modules and packages
- Configuration management
- File I/O (CSV, JSON)
- SQLite database operations
- Exception handling
- Logging
- Decorators (for timing, retries)
- Context managers
- String formatting

### 🔍 Hints
```python
# Hint 1: Base class for pipeline steps
class PipelineStep:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        
    def execute(self, data):
        raise NotImplementedError
        
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

class Extractor(PipelineStep):
    pass

class Transformer(PipelineStep):
    pass

class Loader(PipelineStep):
    pass

# Hint 2: Pipeline orchestrator
class Pipeline:
    def __init__(self, config):
        self.config = config
        self.extractors = []
        self.transformers = []
        self.loaders = []
        self.metrics = {}
        
    def run(self):
        data = {}
        for extractor in self.extractors:
            data[extractor.name] = extractor.execute()
        for transformer in self.transformers:
            data = transformer.execute(data)
        for loader in self.loaders:
            loader.execute(data)
        return self.metrics

# Hint 3: Retry decorator
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay * (2 ** attempt))
        return wrapper
    return decorator

# Hint 4: SQLite loader
import sqlite3

class SQLiteLoader(Loader):
    def execute(self, data):
        conn = sqlite3.connect(self.config['path'])
        cursor = conn.cursor()
        # Insert data
        conn.commit()
        conn.close()
```

---

## 📊 Grading Rubric

Each exercise is evaluated on:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Functionality** | 40% | Does the code work correctly? |
| **Code Quality** | 25% | Is the code clean, readable, and well-organized? |
| **Error Handling** | 15% | Are edge cases and errors handled gracefully? |
| **Logging & Output** | 10% | Is there appropriate logging and clear output? |
| **Documentation** | 10% | Are there comments and docstrings? |

---

## 🚀 Submission Checklist

For each exercise, submit:

- [ ] All source code files
- [ ] Sample input files (if created)
- [ ] Sample output files (generated by your code)
- [ ] A README explaining how to run your solution
- [ ] Any additional dependencies (requirements.txt)

---

## 💪 Bonus Challenges

If you complete all 6 exercises, try these extensions:

1. **Add unit tests** for your code using `pytest`
2. **Create a web dashboard** using Flask to visualize results
3. **Containerize** your solutions with Docker
4. **Add type hints** throughout your code
5. **Implement parallel processing** for large file handling

---

**Good luck! These exercises represent real-world data engineering challenges you'll face in your career. 🎯**
