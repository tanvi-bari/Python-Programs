'''Check whether a triangle is equilateral, isosceles, or scalene.'''

a=int(input("Enter the side of first traingle:"))
b=int(input("Enter the side of second traingle:"))
c=int(input("Enter the side of third traingle:"))
if a==b==c:
    print("Equilateral Traingle")
elif a==b or b==c or a==c:
    print("Isosceles Traingle")
else:
    print("Scalene Traingle")
    