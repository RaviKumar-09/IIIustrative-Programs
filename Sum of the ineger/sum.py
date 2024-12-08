# Input form the user
number = input('Enter a list of numbers separated by space: ')
# split method
num = number.split()
# sum 
sum = 0
# for loop
for n in num:
    # try block
    try:
     intnum = int()
     sum = sum + intnum
     # except block
    except ValueError:
     # print statement
     print('Entry could be converted to interger. Not valid!', n)
print('Sum of valid integer numbers: ', sum)