# Program to find the platform for a train


train_name = input("Enter the train name or number: ")

# Example train details
train_platforms = {
    "12345": "Platform 1",
    "56789": "Platform 2",
     "Rajdhani Express": "Platform 3",
     "Shatabdi Express": "Platform 4"
}

if train_name in train_platforms:
    print(f"The train '{train_name}' is at {train_platforms[train_name]}.")
else:
       print("Sorry, train information is not available. Please check at the inquiry desk.")