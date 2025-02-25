# Write a Python program that filters out even numbers using the filter() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(lambda x: x % 2 != 0, numbers)

odd_numbers_list = list(odd_numbers)
print(f"Odd numbers: {odd_numbers_list}")


