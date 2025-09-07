import json

# Load data
with open('data.json', 'r') as file:
    data = json.load(file)

# Filter only Data Engineers
data_engineers = [emp for emp in data['employees'] if emp['role'] == 'Data Engineer']

# Save filtered data to a new JSON file
with open('data_engineers.json', 'w') as file:
    json.dump({"data_engineers": data_engineers}, file, indent=2)

print("Filtered data written to data_engineers.json.")