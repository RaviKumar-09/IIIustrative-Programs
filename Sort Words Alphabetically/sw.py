# Input a sentence

sentence = input("Enter a sentence: ")

# Sort words
words = sentence.split()
sorted_words = sorted(words)

print("Sorted words:", " ".join(sorted_words))