'''Problem Statement: Process deposits and withdrawals and summarize a bank account's activity. '''

balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
successful = 0
rejected = 0

for i in range(1, n + 1):
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance = balance + amount
        deposits = deposits + 1
        print("Deposit Successful")

    elif choice == 2:
        if amount <= balance:
            balance = balance - amount
            successful = successful + 1
            print("Withdrawal Successful")
        else:
            rejected = rejected + 1
            print("Insufficient Balance")

    else:
        print("Invalid Choice")

print("Final Balance:", balance)
print("Deposit Count:", deposits)
print("Successful Withdrawals:", successful)
print("Rejected Withdrawals:", rejected)

if balance < 1000:
    print("Warning: Balance below ₹1000")