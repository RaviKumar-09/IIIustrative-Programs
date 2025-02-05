# Function to check if all friends are available

def can_friends_meet(friends):
    if all(friends.values()):
        return "Yes! All friends are available. You can meet. 😊"
    else: