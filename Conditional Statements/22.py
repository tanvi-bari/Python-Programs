'''
Check salary bonus based on years of service.'''

salary=float(input("Enter your salary:"))
years=int(input("Enter years of service:"))
if years > 5:
    bonus=salary*0.05
    print("Bonus Amount:",bonus)
    print("Total salary:",salary+bonus)
else:
    print("No bonus")
    