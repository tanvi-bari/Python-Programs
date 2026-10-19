# Check whether a number is prime

n=int(input("Enter the number:"))
count=0

for i in range(1,n+1):
        if n%i==0:
              count=count+1

if n>1 and count==2:
       print("Prime Number")
else:
       print("Not Prime Number")