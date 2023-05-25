#Nisar Ahmed
print("Welcome to prime number")
x=int(input("Enter a number for the range to end"))
prime=[]
for i in range(2,x):
    count =0 #initializing count to 0
    for x in range(2,i):#range of the number currently running till the begining to increment count individually
        if i%x==0: #checking if the number is divisible 
            count+=1 #if divisible by number then we increment count
        

    if count<1:
        prime.append(i) #appending if count less than or equal to 0
print("The prime numbers are ",prime)
