# input values
num = int(input('Enter the number :'))
# find the average of the numbers
def findAvg(n):
    sum = 0
    for num in range(1,n+1):
        sum = sum + num
        avg = float(sum/n)
        print('Sum = ', sum)
        return avg
print('Average of',num,'natural numbers', findAvg(num))
