# Input a number

num = int(input("Enter a number: "))


# Check if perfect number
divisors_sum = sum(i for i in range(1, num) if num % i == 0)

if divisors_sum == num:
     print(f"{num} is a perfect number.")
else: