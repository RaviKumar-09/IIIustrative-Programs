# Dictionary of rooms with availability status

rooms = {
    "Room 101": "Available",
    "Room 102": "Occupied",
    "Room 103": "Available",
    "Room 104": "Occupied",
    "Room 105": "Available"
}

# Function to search for an available room
def find_available_room():
    for room, status in rooms.items():
