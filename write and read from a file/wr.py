# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")


# Read from the file
with open("example.txt", "r") as file:
    content = file.read()
    # Print statement
    print("File content:", content)
