'''Problem Statement: Calculate a customer's shopping bill from multiple products.'''

n = int(input("Enter number of products: "))

subtotal = 0

for i in range(1, n + 1):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    while price < 0 or quantity < 0:
        print("Invalid price or quantity!")
        price = float(input("Enter product price again: "))
        quantity = int(input("Enter quantity again: "))

    item_total = price * quantity
    subtotal = subtotal + item_total

if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0

amount = subtotal - discount

if amount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = amount + delivery

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery Charge:", delivery)
print("Final Payable Amount:", final_amount)