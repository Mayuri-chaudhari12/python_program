# 5) Write a Python program to read a file and print the data on the console.

# Specify the file name to read
file_name = "printed_output.txt"

# Open the file in read mode
with open(file_name, "r") as file:
    data = file.read()
    print("Contents of the file:")
    print(data)
