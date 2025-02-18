import datetime  


# Get user input for date
date_input = input("Enter a date (YYYY-MM-DD): ")

# Convert to datetime object

try:
   date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    weekday = date_obj.strftime("%A")  # Get the day of the week
    print(f"The day of the week for {date_input} is {weekday}.") 