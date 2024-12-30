# Input principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest}")
