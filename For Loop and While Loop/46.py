# Print the first n multiples of a number

n=int(input("Enter the number:"))
terms=int(input("Enter the number of multiples:"))

for i in range(1,terms+1):
    print(n*i)