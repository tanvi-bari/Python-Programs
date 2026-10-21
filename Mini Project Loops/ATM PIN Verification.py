'''Problem Statement: Simulate ATM access with a limited number of PIN attempts.'''

correct_pin = "1234"
attempts = 0
access = False

while attempts < 3:
    pin = input("Enter your ATM PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        print("Access Granted")
        access = True
        break
    else:
        print("Incorrect PIN")

print("Attempts Used:", attempts)

if access == False:
    print("Card Temporarily Locked")