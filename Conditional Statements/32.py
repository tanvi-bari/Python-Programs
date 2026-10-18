'''Check whether a student is eligible for an exam (attendance + marks)'''

attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: Low marks")
else:
    print("Not eligible: Low attendance")