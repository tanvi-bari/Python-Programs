'''Problem Statement: Create a command-line quiz using a fixed set of questions.'''

questions = [
    "What is the capital of India? ",
    "How many days are in a week? ",
    "Which language are we learning? ",
    "What is 5 + 5? ",
    "What is the output of 2 * 3? "
]

answers = ["delhi", "7", "python", "10", "6"]

score = 0

for i in range(5):
    user_answer = input(questions[i]).lower()

    if user_answer == answers[i]:
        print("Correct Answer!")
        score = score + 1
    else:
        print("Wrong Answer!")

percentage = (score / 5) * 100

print("Score:", score, "out of 5")
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good")
else:
    print("Keep Practicing")