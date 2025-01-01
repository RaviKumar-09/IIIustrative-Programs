# Input a string
text = input("Enter a string: ")


# Initialize a counter
vowel_count = 0


# Check each character
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
    
print(f"The number of vowels in the string is: {vowel_count}")   