# Input Value
num = input('Enter two numbers separated by space:')
# number one
num1= int(num.split()[0])
# number two
num2 = int(num.split()[1])
# While loop
while num2 !=0 :
    t = num2
    num2 = num1%num2
    num1 = t
# print the value
print('num1 = ', num1 , 'num2 = ', num2)
