'''
Check whether a number is a single-digit number or not.
'''

number=int(input("Enter the number:"))
if number>=-9 and number<=9:
	print(f"{number} is Single-Digit")
else:
	print("Not Single-Digit")