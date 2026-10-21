'''The Password Strength Checker evaluates a user-entered password and determines whether it is Weak, Medium, or Strong 
based on predefined string conditions.'''

password = input("Enter your password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) < 6:
    print("Weak Password")
elif upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Strong Password")
elif upper > 0 and lower > 0 and digit > 0:
    print("Medium Password")
else:
    print("Weak Password")