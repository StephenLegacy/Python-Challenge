#THIS BASICALL HAS EVERYTHING ABOUT ERROR HANDLING
try:
    print(x)
except:
    print("Error, X is not defined")
else:
    print("There are no errors")
finally:
    print("The 'ty - except' is finished" )
    
import logging

# Setting up logging for error tracking
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception class
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

# Function demonstrating multiple exception handling and raising exceptions
def divide_numbers(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero!")  # Explicitly raise an exception
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        logging.error(e)
    except TypeError as e:
        print("Error: Inputs must be numbers.")
        logging.error(e)
    else:
        print("Division successful!")  # Executes if no exception occurs
    finally:
        print("Division attempt completed.")  # Always executes

# Function demonstrating file operations with error handling
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied for file '{filename}'.")
    else:
        print("File read successfully!")
    finally:
        print("File operation completed.")

# Main code block to demonstrate all features
if __name__ == "__main__":
    print("=== Division Example ===")
    divide_numbers(10, 0)  # Triggers ZeroDivisionError
    divide_numbers(10, "5")  # Triggers TypeError
    print(divide_numbers(10, 2))  # Valid division

    print("\n=== File Handling Example ===")
    read_file("non_existent_file.txt")  # Triggers FileNotFoundError
    read_file("example.txt")  # Replace with an existing file to see successful read

    print("\n=== Custom Exception Example ===")
    try:
        raise CustomError("This is a custom error!")  # Raising a custom exception
    except CustomError as e:
        print(f"Caught a custom error: {e.message}")

    print("\n=== Logging Example ===")
    try:
        risky_code = 10 / 0  # Intentional error for logging
    except ZeroDivisionError as e:
        logging.error(f"Caught an error during risky operation: {e}")
        print("Logged the error.")
