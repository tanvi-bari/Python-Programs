'''Problem Statement: Record expenses for a chosen number of days and summarize spending.'''

days = int(input("Enter number of days: "))

total = 0
highest = 0

for i in range(1, days + 1):
    expense = float(input("Enter expense for day " + str(i) + ": "))

    total = total + expense

    if i == 1 or expense > highest:
        highest = expense

average = total / days

print("Total Expense:", total)
print("Average Daily Expense:", average)
print("Highest Daily Expense:", highest)

if total > 5000:
    print("Budget Alert")
else:
    print("Budget is under control")