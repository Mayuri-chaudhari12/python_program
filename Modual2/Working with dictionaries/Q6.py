# Write a Python program to count how many times each character appears in a string.

input_string = "programming"

char_count = {}

for char in input_string:
    
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Character counts:", char_count)
