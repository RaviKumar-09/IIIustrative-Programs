# Input a string

string = input("Enter a string: ")


# Check for palindrome
if string == string[::-1]:
     print(f"{string} is a palindrome.")
else: