# Practical Example 6: Write a Python program to check if a number is prime using if_else.

for j in range(3,101):

    number = j
    flag = 0
    for i in range(2,number):
        if number%i==0:
            flag =1
            break;
    
    if flag==0:
        print(number, ": prime")
    else:
         print(number, " : not prime")
        pass