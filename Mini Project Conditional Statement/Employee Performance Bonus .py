'''Problem Statement: Develop a salary bonus calculator for a company. The bonus depends on years of 
experience and performance rating. '''

name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))
experience = float(input("Enter years of experience: "))
rating = int(input("Enter rating (1-5): "))

if salary < 0 or experience < 0:
    print("Invalid salary or experience")
elif rating < 1 or rating > 5:
    print("Invalid rating")
else:
    if experience >= 10 and rating >= 4:
        rate = 20
    elif experience >= 5 and rating >= 4:
        rate = 15
    elif experience >= 2 and rating >= 3:
        rate = 10
    else:
        rate = 0

    bonus = salary * rate / 100
    final_salary = salary + bonus

    print("Employee Name:", name)
    print("Bonus Percentage:", rate, "%")
    print("Bonus Amount: ₹", bonus)
    print("Final Salary: ₹", final_salary)

    if rating == 5:
        print("Excellent Performer")
    else:
        print("Performance Rating:", rating)