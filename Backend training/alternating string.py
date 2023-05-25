a=input("Enter a string")
b=input("Enter another string")
c=""
if len(a)==len(b):
    for x in range(len(a)):
        if x%2==0:
            c=c+a[x:x+1]
        else:
            c=c+b[x:x+1]
    print(c)
else:
    print("Not equal lenghts")

    
