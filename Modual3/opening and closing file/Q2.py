# Write a Python program to create a file and write a string into it.

file_name = "output.txt"
text_to_write = "This is the content written to the file."

# Open the file in write mode and write the string
with open(file_name, "w") as file:
    file.write(text_to_write)

print(f"String written to '{file_name}' successfully.")
