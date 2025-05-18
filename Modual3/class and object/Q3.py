# Write a Python program to demonstrate the use of local and globle variables in class.

# Global variable
message = "This is a global variable"

class Demo:
    def show_variables(self):
        # Local variable (only accessible within this method)
        local_message = "This is a local variable"

        print("Inside class method:")
        print("Global message:", message)        # Accessing global variable
        print("Local message:", local_message)   # Accessing local variable

# Create object of class
demo_obj = Demo()

# Call the method
demo_obj.show_variables()

# Accessing global variable outside the class
print("\nOutside the class:")
print("Global message:", message)

# Trying to access local variable outside the class will cause an error
# Uncommenting the line below will raise a NameError
# print(local_message)
