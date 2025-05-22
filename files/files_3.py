# Read existing content
with open('example.txt', 'r') as file:
    old_content = file.read()

# Modify and overwrite content
new_content = old_content.upper()  # Convert text to uppercase

with open('example.txt', 'w') as file:
    file.write(new_content)

print("Content converted to uppercase and saved.")

