'''Problem Statement: Create a checkout program for an online shopping website. The discount depends on 
the purchase amount, and premium customers receive an additional benefit. '''

name=input("Enter the Customer Name:")
amount=int(input("Enter the Purchase Amount:"))
type=input("Enter the type of Customer(Regular or Premium):")

if amount >= 5000:
    discount=amount*20/100
elif amount >= 3000 and amount < 5000:
    discount=amount*10/100
elif amount >= 1000 and amount < 3000:
    discount=amount*5/100
else:
    discount=0

if type=='Premium':
    discount=discount + (amount*5/100)

if amount - discount  >= 2000:
    delivery_charge=0
    print("Free Delivery")
else:
    delivery_charge=100

Total=amount-discount+delivery_charge

print("-------------Details-------------------")
print("Customer Name:",name)
print("Amount:",amount)
print("Discount amount:",discount)
print("Delivery Charge:",delivery_charge)
print("Payable amount:",Total)
