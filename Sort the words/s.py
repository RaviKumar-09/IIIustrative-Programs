# text input
text = input('Enter some text: ')
word = text.split()
count = 0
for w in word:
    count += 1
print('Number of words in the entered text is : ')
word.sort()
print('The words in sorted order are: ')
for w in word:
    print(w)