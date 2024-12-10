# A simple Python program to suggest a phone based on your preferences

# List of available phones (you can add more phones with specifications)
phones = [
    {"name": "iPhone 15", "price": 1200, "camera": 48, "battery": 5000, "storage": 128},
    {"name": "Samsung Galaxy S23", "price": 1000, "camera": 50, "battery": 4500, "storage": 256},
    {"name": "Google Pixel 8", "price": 800, "camera": 48, "battery": 4300, "storage": 128},
    {"name": "OnePlus 11", "price": 700, "camera": 50, "battery": 5000, "storage": 256},
    {"name": "Xiaomi 13", "price": 600, "camera": 54, "battery": 4700, "storage": 128},
]


def suggest_phone(budget, min_camera, min_battery, min_storage):
    suggested_phones = [
        phone
        for phone in phones
        if phone["price"] <= budget
        and phone["camera"] >= min_camera
        and phone["battery"] >= min_battery
        and phone["storage"] >= min_storage
    ]
    return suggested_phones


# Input preferences
print("Welcome to Phone Finder!")
budget = int(input("Enter your budget (in USD): "))
min_camera = int(input("Enter the minimum camera quality (in MP): "))
min_battery = int(input("Enter the minimum battery capacity (in mAh): "))
min_storage = int(input("Enter the minimum storage (in GB): "))