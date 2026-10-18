'''Check whether a person can apply for a loan'''

age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible to apply for loan")
    else:
        print("Salary is too low")
else:
    print("Age is too low")