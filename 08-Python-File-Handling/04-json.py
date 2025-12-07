import json

# Load the JSON file into a Python dictionary
with open('data.json', 'r') as file:
    data = json.load(file)

print("Employee Names:")
for emp in data['employees']:
    print(emp) # This prints the complete employee dictionary
    print(emp['name']) # This prints only the employee name