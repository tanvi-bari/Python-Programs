# Calculate the sum of cubes of the first n numbers

n=int(input("Enter the number:"))
sum=0

for i in range(1,n+1):
    sum=sum+i*i*i

print("Total:",sum)