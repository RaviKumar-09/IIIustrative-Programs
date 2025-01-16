# Input a string
text = input("Enter a string: ")

# Count vowels and consonants
vowels = "aeiou"
vowel_count = sum(1 for char in text.lower() if char in vowels)
consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in vowels)

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")