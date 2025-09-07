import json

def process_json_file(filepath):
    """
    Attempts to load, parse, and process data from a JSON file.
    Demonstrates comprehensive try-except-else-finally blocks.
    """
    print(f"\n--- Processing file: {filepath} ---")
    data = None
    file_handle = None # To demonstrate finally closing it

    try:
        # Attempt to open the file
        print("Attempting to open file")
        file_handle = open(filepath, 'r')
        print("File opened successfully.")

        # Attempt to parse JSON from the file
        print("Attempting to parse JSON...")
        data = json.load(file_handle)
        print("JSON parsed successfully!")

        # Attempt to access specific data (potentially problematic)
        print("Attempting to access specific data fields...")
        name = data['name'] # Common key
        age = data['age']   # Might be missing or wrong type
        
        print(f"  Name: {name}")
        print(f"  Age: {age}")

        # Intentionally try an operation that might cause TypeError if 'age' is not a number
        age_in_5_years = age + 5
        print(f"  Age in 5 years: {age_in_5_years}")

    except FileNotFoundError:
        print(f"ERROR: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"ERROR: Permission denied to read the file '{filepath}'.")
    except json.JSONDecodeError as e:
        print(f"ERROR: Could not decode JSON from '{filepath}'. Invalid JSON format.")
        print(f"  Details: {e.msg} at line {e.lineno} column {e.colno} (char {e.pos})")
    except KeyError as e:
        print(f"ERROR: A required key {e} was not found in the JSON data from '{filepath}'.")
        if data: # If data was loaded but key is missing
             print(f"  Available keys: {list(data.keys())}")
    except TypeError as e:
        print(f"ERROR: A type mismatch occurred while processing data from '{filepath}'.")
        print(f"  Details: {e}")
        print(f"  Value causing error might be '{age}' of type {type(age)} when an operation expected a different type.")
    except Exception as e: # Catch-all for any other unexpected errors
        print(f"AN UNEXPECTED ERROR OCCURRED while processing '{filepath}': {e}")
        print(f"  Error type: {type(e).__name__}")
    else:
        # This block executes if NO exceptions were raised in the try block
        print("SUCCESS: JSON data processed without any critical errors mentioned above.")
        # You could do further processing here that depends on the success of the try block
    finally:
        # This block ALWAYS executes, regardless of whether an exception occurred or not
        print("Finally block: Attempting to clean up resources...")
        # You could perform some tasks which are needed to perform at the end of code execution.

# --- Main execution ---
if __name__ == "__main__":
    # 1. Test with a valid JSON file
    process_json_file("valid_data.json")

    # 2. Test with a file that has invalid JSON syntax
    process_json_file("invalid_syntax.json")

    # 3. Test with a file that doesn't exist
    process_json_file("non_existent_file.json")