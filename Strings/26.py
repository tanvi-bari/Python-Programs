# Find the first and last occurrence of a character

s = input("Enter a string: ")
ch = input("Enter a character: ")
print("First occurrence:", s.find(ch))
print("Last occurrence:", s.rfind(ch))