import csv
from pathlib import Path

csv_path = Path("employees.csv")

total_salary = 0
records      = 0

with csv_path.open(newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_salary += float(row["salary"])
        records      += 1

avg_salary = total_salary / records
print(f"Average salary: ${avg_salary:,.2f}")