from datetime import datetime, timedelta


# Check if tomorrow is a weekend
if (datetime.now() + timedelta(days=1)).weekday() >= 5:
     print("You can take leave tomorrow. 😊")
