# Input a number
num = int(input("Enter a number: "))

# Check if it's an Armstrong number
sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
