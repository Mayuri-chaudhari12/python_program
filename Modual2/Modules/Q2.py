# Write a Python program to generate random numbers using the random module.

import random

random_integer = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer}")

random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

random_uniform = random.uniform(10, 50)
print(f"Random float between 10 and 50: {random_uniform}")

random_choice = random.choice([10, 20, 30, 40, 50])
print(f"Random choice from the list: {random_choice}")

sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print(f"Shuffled list: {sample_list}")
