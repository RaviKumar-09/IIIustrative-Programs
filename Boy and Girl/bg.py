# Function to calculate
# GCD of two numbers
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

# Function to count maximum persons
# that can be placed in a row