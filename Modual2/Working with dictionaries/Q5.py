# Write a Python program to convert two lists into one dictionary using a for loop.

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:", merged_dict)
