'''Calculate discounts based on total shopping amount.'''

amount = int(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 10 / 100
elif amount >= 1000:
    discount = amount * 5 / 100
else:
    discount = 0

print("Discount:", discount)
print("Final amount:", amount - discount)