# Find the length without using len()

s = input("Enter a string: ")
count = 0

for ch in s:
    count += 1
print("Length:", count)