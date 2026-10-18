'''Check exam results (Distinction, First Class, Pass, Fail).'''

result=int(input("Enter the result:"))
if result>=80:
    print("Distinction")
elif result>=60:
    print("First Class")
elif result>=45:
    print("Pass")
else:
    print("Fail")