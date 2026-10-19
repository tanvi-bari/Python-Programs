# Check whether a number is Armstrong

n = int(input("Enter a number: "))
temp = n
total = 0


while n > 0:
    digit = n % 10
    total = total + digit*digit*digit
    n = n // 10

if temp == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")