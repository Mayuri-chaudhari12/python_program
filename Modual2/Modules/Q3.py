# Write a Python program to demonstrate the use of functions from the math module.

import math

num = 25

sqrt_result = math.sqrt(num)
print(f"The square root of {num} is: {sqrt_result}")

ceil_result = math.ceil(5.2)
print(f"The ceiling of 5.2 is: {ceil_result}")

floor_result = math.floor(5.7)
print(f"The floor of 5.7 is: {floor_result}")

abs_result = math.fabs(-9.5)
print(f"The absolute value of -9.5 is: {abs_result}")


pow_result = math.pow(3, 4) 
print(f"3 raised to the power of 4 is: {pow_result}")

factorial_result = math.factorial(5)
print(f"The factorial of 5 is: {factorial_result}")

radians_result = math.radians(90)  
print(f"90 degrees in radians is: {radians_result}")


sin_result = math.sin(math.radians(30)) 
print(f"The sine of 30 degrees is: {sin_result}")

log_result = math.log(10)
print(f"The natural logarithm of 10 is: {log_result}")

fact_result = math.factorial(6)
print(f"The factorial of 6 is: {fact_result}")
