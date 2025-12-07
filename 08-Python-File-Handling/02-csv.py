import csv
from pathlib import Path

csv_path = Path("employees.csv")

total_salary = 0
records      = 0

with csv_path.open(newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        #print(row)
        #print(row["salary"])
        total_salary += float(row["salary"])
        #print(total_salary)
        records      += 1

avg_salary = total_salary / records
print(f"Average salary: ${avg_salary:,.2f}")