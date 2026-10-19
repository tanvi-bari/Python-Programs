# Print ASCII values of characters in a string

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))