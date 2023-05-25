import random as r
h=0
t=0

y=int(input("Trial a coin for number of times = "))
for i in range(y):
    x = r.randrange(2)
    if x==0:
        print(i,"try="," Tails")
        t=t+1
    else:
        print(i,"try="," Heads")
        h=h+1
print("Total heads = ",h)
print("Total tails = ",t)
