# Write a Python program to apply the map() function to square a list of numbers.

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x * x, numbers)

squared_numbers_list = list(squared_numbers)
print(f"Squared numbers: {squared_numbers_list}")
