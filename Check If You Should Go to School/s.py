from datetime import datetime

# Get current time and day
now = datetime.now()
hour = now.hour

day = now.strftime("%A")  # Get current day (e.g., Monday, Tuesday)
