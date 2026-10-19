# Print numbers until the user enters a negative number

while True:
    n=int(input("Enter number:"))

    if n<0:
        break

    print(n)