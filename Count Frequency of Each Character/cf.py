# Input a string
text = input("Enter a string: ")
# Count frequency
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
