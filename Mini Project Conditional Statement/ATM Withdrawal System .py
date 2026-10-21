'''Problem Statement: Build a simple ATM transaction program that allows a customer to withdraw money 
after checking account balance and withdrawal limits.'''

name = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if balance < 0:
    print("Invalid balance")
elif withdraw <= 0:
    print("Invalid withdrawal amount")
elif withdraw > 20000:
    print("Maximum withdrawal limit is ₹20000")
elif withdraw > balance:
    print("Insufficient balance")
else:
    remaining = balance - withdraw

    print("Account Holder:", name)
    print("Transaction Status: Successful")
    print("Withdrawn Amount: ₹", withdraw)
    print("Remaining Balance: ₹", remaining)

    if remaining < 1000:
        print("Low Balance Warning")