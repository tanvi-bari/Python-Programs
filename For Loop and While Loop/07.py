'''Calculate factorial of a number using for loop.'''

n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of ",n," = ",fact)