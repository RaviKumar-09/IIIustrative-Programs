# List of numbers
numbers = [10, 20, 30, 40, 50]

# Find the median
numbers.sort()
n = len(numbers)

median = numbers[n // 2] if n % 2 != 0 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("The median is:", median)