# input values
num = int(input('Enter the number :'))
# find the average of the numbers
def findAvg(n):
    sum = 0
    # range
    for num in range(1,n+1):
        sum = sum + num
        avg = float(sum/n)
        print('Sum = ', sum)
        return avg
# find the average of the numbers
print('Average of',num,'natural numbers', findAvg(num))
