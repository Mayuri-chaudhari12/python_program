#Write a Python program to demonstrate string slicing.

string = "Hello, World!"

substring1 = string[0:5]
print(f"Substring from index 0 to 5: {substring1}")

substring2 = string[7:]
print(f"Substring from index 7 to the end: {substring2}")

substring3 = string[:5]
print(f"Substring from the beginning to index 5: {substring3}")

substring4 = string[::2]
print(f"Substring with step of 2: {substring4}")

substring5 = string[-6:-1]
print(f"Substring from index -6 to -1: {substring5}")
