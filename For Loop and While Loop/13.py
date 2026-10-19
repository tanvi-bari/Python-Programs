# Check whether a number is palindrome

n=int(input("Enter the number:"))
temp=n
sum=0

while n>0:
    digit=n%10
    sum=sum*10+digit
    n=n//10
if temp==sum:
    print("Palindrome")
else:
    print("Not Palindrome")