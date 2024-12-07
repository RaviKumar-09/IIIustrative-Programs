# display give number is prime number
# Input from the user
num = int(input('Enter the number: '))

# import module
import math
prime = True
x = int(math.sqrt(num))

# while loop
while x>1:
    # if condtion
    if num%x == 0:
        print(x,'divides',num)
        prime = False
        break
    else:
        x -=1
    # If condition
    if prime:
        # prime number display
        print('The number',num,'is prime')
        # not prime number display
    else:
      print('The number',num,'is Not prime')  
        
