# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if string2 is a substring of string1
if string2 in string1:
     print(f"'{string2}' is a substring of '{string1}'.")