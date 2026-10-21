'''Problem Statement: Print a multiplication table and analyze a range of integers.'''

num = int(input("Enter a positive integer: "))

while num <= 0:
    print("Enter a positive number!")
    num = int(input("Enter a positive integer: "))

print("Multiplication Table")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start > end:
    print("Invalid range! Start must be less than or equal to end.")
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

even_count = 0
odd_count = 0
total = 0

for i in range(start, end + 1):
    total = total + i

    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Sum of Range:", total)