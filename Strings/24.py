# Extract only digits from a string

s = input("Enter a string: ")
count = ""
for ch in s:
    if ch.isdigit():
        count+= ch
print(count)