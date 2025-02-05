# Function to check if all friends are available

def can_friends_meet(friends):
    if all(friends.values()):
        return "Yes! All friends are available. You can meet. 😊"
    else:
        return "No, some friends are busy. Try another time. 😞"
# List of friends
friends = {}

# Number of friends
num_friends = int(input("Enter the number of friends: "))
# Get availability from each friend
for i in range(num_friends):
    name = input(f"Enter Friend {i+1} Name: ")
    available = input(f"Is {name} available? (yes/no): ").strip().lower()
    friends[name] = available == "yes"
# Check if all friends can meet
result = can_friends_meet(friends)