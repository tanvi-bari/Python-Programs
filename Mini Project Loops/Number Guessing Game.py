'''Problem Statement: Give the user a limited number of chances to guess a secret number.'''

secret = 50
attempts = 0
won = False

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret:
        print("Correct Guess! You Won!")
        won = True
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print("Attempts Used:", attempts)

if won == False:
    print("You Lost!")
    print("Secret Number:", secret)