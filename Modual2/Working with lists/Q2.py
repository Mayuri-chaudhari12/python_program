# Write a Python program to sort a list using both sort() and sorted().

my_list = [30, 10, 50, 20, 40]

my_list.sort()
print("List after using sort():", my_list)

another_list = [30, 10, 50, 20, 40]

sorted_list = sorted(another_list)
print("List after using sorted():", sorted_list)

print("Original list after using sorted():", another_list)
