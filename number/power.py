# Input base and exponent

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate power
result = 1

for _ in range(abs(exponent)):
    result *= base

if exponent < 0:
    result = 1 / result