# Input a decimal number
# decimal
decimal = int(input("Enter a decimal number: "))

# Convert to binary
# binary
binary = bin(decimal)[2:]

#printS
print(f"The binary representation of {decimal} is {binary}.")