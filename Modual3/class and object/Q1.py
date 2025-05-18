# write a python program to create a class and access its properties using an object.

# Define a class named 'Person'
class Person:
    # Constructor to initialize the object's properties
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of the Person class
person1 = Person("Alice", 30)

# Access and print the properties using the object
print("Name:", person1.name)
print("Age:", person1.age)

