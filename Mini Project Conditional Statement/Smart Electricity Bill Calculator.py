'''Problem Statement: Develop a small electricity billing program for a household. The electricity board 
charges different rates according to the number of units consumed.'''


name=input("Enter the Customer Name:")
unit=int(input("Enter the units consumed:"))

if unit<=100:
    energy_charge=unit*3
elif unit<=200:
    energy_charge=(100*3)+(unit-100)*5
else:
    energy_charge=(100*3)+(100*5)+(unit-200)*7

service_charge = 150
total_bill=energy_charge + service_charge

print("\n-----------Electricity Bill-----------------")
print("Customer Name:",name)
print("Units Consumed:",unit)
print("Energy Charge:Rs ",energy_charge)
print("Service Charge:Rs ",service_charge)
print("Electricity Bill = ",total_bill,"rupees")

if total_bill > 5000:
    print("Usage Message:High Usage Bill")
else:
    print("Usage Message:Normal Usage Bill")

