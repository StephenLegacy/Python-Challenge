def read_and_modify_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")
        
        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.readlines()
        
        # Modify content (example: adding line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]
        
        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)
        
        print(f"File has been modified and saved as {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don’t have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
