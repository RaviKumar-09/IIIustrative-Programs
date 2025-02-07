# List of friends and their availability
friends = {
    "Rahul": "yes",
    "Priya": "no",
    "Arjun": "yes",
    "Sita": "yes"
}

# Check if all friends are available

if all(availability == "yes" for availability in friends.values()):
    print("Yes! All friends are available. Let's go for a movie! 🎬🍿")