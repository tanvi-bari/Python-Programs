# Count vowels in a string

s=input("Enter the string:")
count=0
for ch in s:
    if  ch in "AEIOUaeiou":
        count=count+1
print("vowels:",count)