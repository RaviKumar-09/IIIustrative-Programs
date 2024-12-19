# Input a word
word = input("Enter a word: ")

# Check if it's a palindrome

# if statement
if word == word[::-1]:
     print(f"{word} is a palindrome!")

# else statement
else:
     print(f"{word} is not a palindrome.")