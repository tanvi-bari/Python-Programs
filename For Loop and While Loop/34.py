#Check whether a string is palindrome

s=input("Enter the string:")
if s==s[::-1]:
    print("Palindrome")
else:
    print(" Not Palindrome")