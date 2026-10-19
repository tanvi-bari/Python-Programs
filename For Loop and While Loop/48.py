# Check whether a number is a strong number

'''A strong number is a number whose digits' factorials 
add up to the original number. Example: 145 = 1! + 4! + 5!.'''

n = int(input("Enter a number: "))
temp = n
total = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    n = n // 10

if temp == total:
    print("Strong number")
else:
    print("Not a strong number")