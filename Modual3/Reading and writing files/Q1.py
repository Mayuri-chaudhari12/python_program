# write a python program to read the contents of a file and print them on the console.

# Specify the file name
file_name = "output.txt"

# Open the file in read mode and print its contents
with open(file_name, "r") as file:
    contents = file.read()
    print("File contents:")
    print(contents)
