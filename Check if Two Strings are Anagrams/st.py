# Input two strings

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check for anagrams
if sorted(str1.lower()) == sorted(str2.lower()):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")