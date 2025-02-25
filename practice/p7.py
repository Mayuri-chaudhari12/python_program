alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
index = 0 

for i in range(1, 6):
    for j in range(i):
        print(alphabet[index], end='')  
        index += 1 
    print()  
