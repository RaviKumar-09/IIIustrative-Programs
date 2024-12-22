# Print a multiplication table for a number:



# Input a number
# number
num = int(input("Enter a number: "))


# Print the multiplication table

# for loop
for i in range(1, 11):
    # print statement
    print(f"{num} x {i} = {num * i}")