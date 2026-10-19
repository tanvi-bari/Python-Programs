# Count consonants in a string

s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count = count + 1

print("Consonants =", count)