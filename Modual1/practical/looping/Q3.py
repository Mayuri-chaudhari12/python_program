# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

List1 = ['apple', 'banana', 'mango']
search_string = 'banana'

found = False 

for fruit in List1:
    if fruit == search_string:
        found = True
        print(f"{search_string} is found in the list.")
        break 

if not found:
    print(f"{search_string} is not found in the list.")
