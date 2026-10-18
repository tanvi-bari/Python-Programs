''' Check blood donation eligibility based on age and weight'''

age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and weight >= 50:
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")