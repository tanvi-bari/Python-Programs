'''Print menu-based food selection using match-case'''

print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Pasta")
print("5. Pav Bhaji")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Sandwich")
    case 4:
        print("You selected Pasta")
    case 5:
        print("You selected Pav Bhaji")
    case _:
        print("Invalid choice")