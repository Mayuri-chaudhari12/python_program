# Write a Python program to demonstrate handling multiple exceptions.

def multiple_exception_demo():
    try:
        # Get user input
        num = int(input("Enter a number: "))
        result = 10 / num  # May raise ZeroDivisionError
        print("Result of division:", result)

        # Try to open a file
        with open("non_existent_file.txt", "r") as file:
            data = file.read()
            print("File contents:", data)

    except ValueError:
        print("Invalid input! Please enter an integer.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Run the function
multiple_exception_demo()
