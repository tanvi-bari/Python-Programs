'''Problem Statement: Calculate payroll details for several employees. '''

n = int(input("Enter number of employees: "))

total_payroll = 0

for i in range(1, n + 1):
    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    hours = float(input("Enter overtime hours: "))

    overtime_pay = hours * 200
    gross = basic + overtime_pay

    if gross >= 50000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.05

    net_salary = gross - deduction
    total_payroll = total_payroll + net_salary

    print("Employee Name:", name)
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net_salary)

print("Total Net Payroll:", total_payroll)
print("Employee Count:", n)