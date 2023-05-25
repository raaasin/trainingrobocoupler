import os
f=open("example.txt","w")
f.write("Hello")
f.close()



f=open("example.txt")
x=f.read()
print(x)
f.close()


os.remove("example.txt")
