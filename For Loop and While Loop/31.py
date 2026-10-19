# Generate the first n odd numbers

n = int(input("Enter n: "))
i = 1
count = 0

while count < n:
    print(i)
    i = i + 2
    count = count + 1