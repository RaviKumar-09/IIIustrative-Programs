# display give number is prime number
num = int(input('Enter the number: '))
import math
prime = True
x = int(math.sqrt(num))
while x>1:
    if num%x == 0:
        print(x,'divides',num)
        prime = False
        break
    else:
        x -=1
    if prime:
        # prime number display
        print('The number',num,'is prime')
        # not prime number display
    else:
      print('The number',num,'is Not prime')  
        
