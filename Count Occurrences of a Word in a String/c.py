# Input a string and a word
sentence = input("Enter a sentence: ")
word = input("Enter the word to count: ")

# Count occurrences
count = sentence.lower().split().count(word.lower())
print(f"The word '{word}' appears {count} times.")
