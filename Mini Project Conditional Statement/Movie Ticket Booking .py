'''Problem Statement: Create a movie ticket pricing program for a cinema. Ticket price depends on age, 
show type, and whether the booking is on a weekend. '''

name = input("Enter customer name: ")
age = int(input("Enter age: "))
show = input("Enter show type (Morning/Evening): ").lower()
day = input("Enter day type (Weekday/Weekend): ").lower()

price = 200

if age < 0:
    print("Invalid age")
elif show not in ("morning", "evening") or day not in ("weekday", "weekend"):
    print("Invalid show or day type")
else:
    if age < 12:
        discount = price * 50 / 100
    elif age >= 60:
        discount = price * 30 / 100
    else:
        discount = 0

    if show == "morning":
        discount = discount + 30

    if day == "weekend":
        surcharge = 50
    else:
        surcharge = 0

    final = price - discount + surcharge

    print("Customer Name:", name)
    print("Original Ticket Price: ₹", price)
    print("Discount: ₹", discount)
    print("Weekend Surcharge: ₹", surcharge)
    print("Final Ticket Price: ₹", final) 