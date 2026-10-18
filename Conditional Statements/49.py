'''Print result status using match-case'''

status = input("Enter result status (pass/fail/absent): ")

match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("Better luck next time.")
    case "absent":
        print("You were absent.")
    case _:
        print("Invalid result status")