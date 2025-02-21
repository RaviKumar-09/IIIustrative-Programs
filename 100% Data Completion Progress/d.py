import time

# Function to display a loading bar
def show_progress():
    total = 100
    for i in range(total + 1):
        time.sleep(0.05)