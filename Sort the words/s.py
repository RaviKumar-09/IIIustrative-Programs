# text input
text = input('Enter some text: ')
word = text.split()
count = 0
# for loop for count the values
for w in word:
    count += 1
# print statements
print('Number of words in the entered text is : ')
word.sort()
print('The words in sorted order are: ')
# for loop for print w words
for w in word:
    print(w)