import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Create a new directory
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"Created directory: {new_dir}")

# List the contents of the current directory
contents = os.listdir()
print(f"Directory contents: {contents}")

# Rename the new directory
os.rename(new_dir, "renamed_directory")
print(f"Renamed directory to: renamed_directory")

# List the contents of the current directory
contents = os.listdir()
print(f"Directory contents: {contents}")

# Remove the directory
os.rmdir("renamed_directory")
print("Removed directory")
