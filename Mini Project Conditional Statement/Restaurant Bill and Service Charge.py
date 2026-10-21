'''Problem Statement: Create a restaurant billing program for a customer. The service charge and discount 
depend on the bill amount and membership status.'''

name=input("Enter thye Customer Name:")
bill_amount=int(input("Enter the bill amount:"))
member=input("Membership(Yes/No):").lower()

if bill_amount<0:
    print("Invaild bill amount")
elif member not in ("yes","no"):
    print("Invalid status")
else:
    if bill_amount >= 5000:
        rate=15
    elif bill_amount >= 3000:
        rate=10
    elif bill_amount >= 1000:
        rate=5
    else:
        rate=0

    if member=="yes":
        rate=rate+5

    discount=bill_amount*rate/100
    amount=bill_amount-discount
    service=amount*5/100
    final=amount+service

    print("Customer Name:",name)
    print("Original Bill: Rs",bill_amount)
    print("Discount: Rs",discount)
    print("Service Charge: Rs",service)
    print("Total Bill: Rs",final)

    if final >= 5000:
        print("Thank you for being a valued customer!!")
    else:
        print("Thank you for visiting!!")




