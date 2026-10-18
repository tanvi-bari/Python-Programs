'''
Find the greatest of three numbers.
'''

a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
c=int(input("Enter the number 3 : "))

if a>b:
	if a>c:
		print(f"{a} is Greater")
	else:
		print(f"{c} is Greater")
else:
	if b>c:
		print(f"{b} is Greater")
	else:
		print(f"{c} is Greater")


	