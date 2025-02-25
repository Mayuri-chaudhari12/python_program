lines = 7
stars = 1
space=0
mid=(lines//2)+1
for i in range(1,lines+1):
    for k in range(space):
        print(" ",end="")
    for j in range(stars):
        if j==0 or j==stars-1:
         print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<mid:
        stars+=2
        space-=1
    else:
        stars-=2
        space+=1