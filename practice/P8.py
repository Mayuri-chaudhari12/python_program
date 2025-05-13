#file=open("test.txt","w")
#file.write("python programing")
#file.close()

with open("Home.txt",'w') as file:
    file.write("Hello python")
    file.seek(0)
    dt = file.read(                          )
    print(dt)
