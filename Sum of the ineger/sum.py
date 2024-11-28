# Input form the user
number = input('Enter a list of numbers separated by space: ')
num = number.split()
sum = 0
# for loop
for n in num:
    # try block
    try:
     intnum = int()
     sum = sum + intnum
    except ValueError:
     print('Entry could be converted to interger. Not valid!', n)
print('Sum of valid integer numbers: ', sum)