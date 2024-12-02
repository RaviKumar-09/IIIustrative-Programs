# Function to calculate
# GCD of two numbers
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

# Function to count maximum persons
# that can be placed in a row

def maximumRowValue(n, m):
    return gcd(n, m)

# Driver Code
if __name__ == '__main__':

     # Input
    N = 4
    M = 2