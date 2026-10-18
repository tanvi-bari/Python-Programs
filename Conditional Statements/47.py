'''Check user role (admin, user, guest) using match-case'''

role = input("Enter user role: ")

match role:
    case "admin":
        print("Full access")
    case "user":
        print("Normal access")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role")