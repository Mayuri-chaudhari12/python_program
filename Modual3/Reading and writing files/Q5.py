# 6) Write a Python program to check the current position of the file cursor using tell().

# Create and write some text to a file
file_name = "cursor_position.txt"
with open(file_name, "w") as file:
    file.write("Hello, file cursor!")

# Open the file in read mode and check cursor position
with open(file_name, "r") as file:
    print("Initial cursor position:", file.tell())  # Should be 0
    file
