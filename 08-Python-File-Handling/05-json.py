import json

# Load current data
with open('data.json', 'r') as file:
    data = json.load(file)

# Add a new employee to the list
new_employee = {"id": 3, "name": "Charlie", "role": "ML Engineer"}
data['employees'].append(new_employee)

# Write the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("New employee added successfully.")