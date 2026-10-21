'''Problem Statement: Develop an insurance premium calculator. The premium category depends on age, 
occupation risk, and smoking status.'''

name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ").lower()
smoker = input("Are you a smoker? (Yes/No): ").lower()

base = 10000

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Customer Name:", name)
    print("Eligibility: Not Eligible")
elif risk not in ("low", "medium", "high") or smoker not in ("yes", "no"):
    print("Invalid input")
else:
    extra = 0

    if age > 50:
        extra = extra + 5000

    if risk == "high":
        extra = extra + 7000
    elif risk == "medium":
        extra = extra + 3000

    if smoker == "yes":
        extra = extra + 5000

    final = base + extra

    print("Customer Name:", name)
    print("Eligibility: Eligible")
    print("Base Premium: ₹", base)
    print("Additional Charges: ₹", extra)
    print("Final Premium: ₹", final)

    if extra >= 10000:
        print("High Risk Policy")
    else:
        print("Normal Risk Policy")