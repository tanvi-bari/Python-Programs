# Generate the first n even numbers

n = int(input("Enter n: "))
i = 1
count = 0

while count < n:
    print(i * 2)
    i = i + 1
    count = count + 1