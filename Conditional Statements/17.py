'''
Check grade based on marks (A, B, C, Fail).
'''

marks=int(input("Enter the marks of student:"))
if marks>=80:
	print("A")
elif marks>=60:
	print("B")
elif marks>=45:
	print("C")
else:
	print("FAIL")
