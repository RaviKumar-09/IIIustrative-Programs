def check_holiday(day):
    # List of weekend holidays
    weekend_holidays = ["Saturday", "Sunday"]

     # Check if the given day is a weekend
    if day.capitalize() in weekend_holidays:
        return f"{day} is a holiday!"
    else:
        return f"{day} is a working day."
    
# Input the day of the week
day_of_week = input("Enter the day of the week: ").strip()

# Check if it's a holiday or working day
result = check_holiday(day_of_week)