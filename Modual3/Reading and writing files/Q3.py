#  Write a Python program to create a file and print the string into the file. 

# Define the file name and the string to print into the file
file_name = "printed_output.txt"
text_to_print = "This string is printed into the file using Python."

# Open the file in write mode and write the string
with open(file_name, "w") as file:
    print(text_to_print, file=file)

print(f"String has been printed into '{file_name}' successfully.")

 