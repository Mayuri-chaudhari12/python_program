# Write a Python program to write multiple strings into a file

# Define the file name and strings to write
file_name = "multiple_lines.txt"
lines = [
    "First line of text.\n",
    "Second line of text.\n",
    "Third line of text.\n"
]

# Open the file in write mode and write the strings
with open(file_name, "w") as file:
    file.writelines(lines)

print(f"Multiple strings written to '{file_name}' successfully.")
