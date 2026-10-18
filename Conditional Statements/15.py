'''
Check whether a number is divisible by both 3 and 7 or not.
'''

number=int(input("Enter the number:"))
if number%3==0 and number%7==0:
	print(f"{number} is Divisible by 3 and 7")
else:
	print(f"{number} is not Divisible ")