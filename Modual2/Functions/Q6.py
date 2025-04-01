
# Write a Python program to create a lambda function with two expressions.

multi_expr = lambda x, y: (x + y, x * y)


result = multi_expr(5, 3)
print("Sum:", result[0])
print("Product:", result[1])
