#Write a generator function that generates the first 10 even numbers.
even_numbers = (num for num in range(2, 21, 2))
for number in even_numbers:
    print(number)

