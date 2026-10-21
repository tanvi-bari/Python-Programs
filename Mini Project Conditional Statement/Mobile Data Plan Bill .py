'''Problem Statement: Build a mobile data billing program for a telecom customer. The monthly bill 
depends on the selected plan and additional data usage. '''

name = input("Enter customer name: ")
plan = input("Enter plan (Basic/Standard/Premium): ").lower()
extra = float(input("Enter extra data used in GB: "))

if extra<0:
    print("Invalid output")
else:
    if plan == "basic":
        base = 299
    elif plan == "standard":
        base = 499
    elif plan == "premium":
        base = 799
    else:
        base = 0
        print("Invalid plan type")

    if base > 0:
        extra_charge = extra * 20

        if extra > 10:
            surcharge = 100
        else:
            surcharge = 0

        total = base + extra_charge + surcharge

        print("Customer Name:", name)
        print("Plan Type:", plan)
        print("Base Plan Charge: ₹", base)
        print("Extra Data Charge: ₹", extra_charge)
        print("Surcharge: ₹", surcharge)
        print("Final Bill: ₹", total)