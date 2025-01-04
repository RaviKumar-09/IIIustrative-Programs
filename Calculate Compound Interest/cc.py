# Input principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = int(input("Enter the time in years: "))

# Calculate compound interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal