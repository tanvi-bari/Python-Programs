'''Problem Statement: Create a scholarship eligibility checker for a college. Students are selected based on 
marks, family income, and attendance. '''

name=input("Enter the name of Student:")
percentage=int(input("Enter the Percentage:"))
income=int(input("Enter the Family Income:"))
attendance=int(input("Enter the Attendence Percentage:"))

if percentage < 0 or percentage > 100 or attendance < 0 or attendance > 100 or income < 0:
    print("Invalid input")
elif percentage >= 75 and income <= 400000 and attendance >= 75:
    print("Student Name:", name)
    print("Eligibility Status: Eligible")

    if percentage>=90:
        print("Full Scholarship!!")
    else:
        print("Partail Scholarship!!")

else:
    print("Student Name:", name)
    print("Eligibility Status: Not Eligible")

    if percentage < 75:
        print("Reason: Percentage below 75%")
    elif income > 400000:
        print("Reason: Family income exceeds ₹400000")
    else:
        print("Reason: Attendance below 75%")