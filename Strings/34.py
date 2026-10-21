# Find the ASCII value of each character

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))