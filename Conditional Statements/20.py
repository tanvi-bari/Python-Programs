'''
Check ticket price based on age.'''

age=int(input("Enter the age:"))
if age < 5:
    price=0
elif age < 20:
    price=20
elif age < 50:
    price=60
elif age < 70:
    price=100
else:
    price=0
    print("Invalid!!")

print("Price : ",price)