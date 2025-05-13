print("program starting.......")
try:
    #a= 10
    #b=a/0
    #print(b)


    #Value Error
    a = int(input("Enter a: "))
    print(a)
except ZeroDivisionError as a:
    print(a)

print("program end....")


