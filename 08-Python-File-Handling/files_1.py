# 1: Open the file in read mode
with open('example.txt', 'r') as my_data:
    content = my_data.read()

print("Current File Content:")
print(content)

# 2: Open the file in Append mode
with open('example.txt', 'a', encoding='utf-8') as data:
    data.write('\nAppended line of text.\n')

print('Line appended successfully.')

with open('example.txt', 'r', encoding='utf-8') as data:
    content = data.read()
    print('\nFile content after appending:')
    print(content)

# 3: Modify and overwrite content
with open('example.txt', 'r') as file:
    old_content = file.read()

new_content = old_content.lower()

with open('example.txt', 'w') as file:
    file.write(new_content)

print("Content converted to lowercase and saved.")