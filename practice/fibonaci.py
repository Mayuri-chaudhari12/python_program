length = 15
a = 0
b = 1
print(a, b, end=" ")

i = 2  
while i < length:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    i += 1
