from datetime import datetime

# Get current time and day
now = datetime.now()
hour = now.hour

day = now.strftime("%A")  # Get current day (e.g., Monday, Tuesday)


# Check if it's a school day and morning time

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] and hour < 8:
    print("Good to go to school! 📚🏫")
else:
    print("No school now! Enjoy your time. 😊")