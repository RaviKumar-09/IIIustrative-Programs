# Create a list of numbers

numbers = [64, 34, 25, 12, 22, 11, 90]

# Bubble sort algorithm
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]: