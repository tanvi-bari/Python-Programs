'''
find the smallest of three numbers.'''

a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
c=int(input("Enter the number 3 : "))

if a<b and a<c:
    print(a," is Smaller")
elif b<a and b<c:
    print(b," is Smaller")
else:
    print(c," is Smaller")
     