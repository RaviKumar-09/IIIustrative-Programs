# Input a string

text = input("Enter a string: ")

# Check for alphabets only
if text.isalpha():
    print(f"{text} contains only alphabets.")
else:
    print(f"{text} contains non-alphabetic characters.")