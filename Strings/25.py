# Extract only alphabets from a string

s = input("Enter a string: ")
count = ""
for ch in s:
    if ch.isalpha():
        count += ch
print(count)