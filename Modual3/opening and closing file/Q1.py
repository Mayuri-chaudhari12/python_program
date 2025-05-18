# Write a Python program to open a file in write mode, write some text, and then close it.

# Open a file in write mode
file = open("example.txt", "w")

# Write some text to the file
file.write("Hello, this is a test.\n")
file.write("This file was created using Python.\n")

# Close the file
file.close()

print("File written and closed successfully.")
