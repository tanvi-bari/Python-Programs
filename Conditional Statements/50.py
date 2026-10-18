'''Build a simple ATM menu using match-case'''

balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Balance:", balance)
    case 2:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Updated balance:", balance)
        else:
            print("Invalid amount")
    case 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Updated balance:", balance)
        else:
            print("Invalid amount or insufficient balance")
    case _:
        print("Invalid choice")