'''Problem Statement: Analyze daily electricity consumption over a selected period.'''

days = int(input("Enter number of days: "))

total = 0
high_days = 0
maximum = 0

for i in range(1, days + 1):
    units = float(input("Enter units consumed: "))

    total = total + units

    if units > 10:
        high_days = high_days + 1

    if i == 1 or units > maximum:
        maximum = units

average = total / days

print("Total Units:", total)
print("Average Usage:", average)
print("High Usage Days:", high_days)
print("Maximum Daily Usage:", maximum)

if total > 300:
    print("High Usage")
else:
    print("Normal Usage")