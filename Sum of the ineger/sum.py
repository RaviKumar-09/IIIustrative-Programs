number = input('Enter a list of numbers separated by space: ')
num = number.split()
sum = 0
for n in num:
    try:
     intnum = int()
     sum = sum + intnum
    except ValueError:
     print('Entry could be converted to interger. Not valid!', n)