'''Problem Statement: Create a simple hotel booking calculator. The room price depends on room type and 
the number of nights. Customers may also receive a discount based on their stay.'''

name = input("Enter guest name: ")
room = input("Enter room type (Standard/Deluxe/Suite): ").lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Invalid number of nights")
else:
    if room == "standard":
        price = 2000
    elif room == "deluxe":
        price = 3500
    elif room == "suite":
        price = 6000
    else:
        price = 0
        print("Invalid room type")

    if price > 0:
        charge = price * nights

        if nights >= 10:
            discount = charge * 20 / 100
        elif nights >= 5:
            discount = charge * 10 / 100
        else:
            discount = 0

        final = charge - discount

        print("Guest Name:", name)
        print("Room Type:", room)
        print("Number of Nights:", nights)
        print("Room Charge: ₹", charge)
        print("Discount: ₹", discount)
        print("Final Booking Amount: ₹", final)