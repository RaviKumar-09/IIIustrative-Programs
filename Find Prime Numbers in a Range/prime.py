# Input range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


# Find prime numbers
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1: