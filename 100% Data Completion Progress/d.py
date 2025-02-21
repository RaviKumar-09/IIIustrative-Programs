import time

# Function to display a loading bar
def show_progress():
    total = 100
    for i in range(total + 1):
        time.sleep(0.05)
         # Simulate processing delay
        bar = "█" * (i // 2) + "-" * ((total // 2) - (i // 2))
        print(f"\rProcessing: [{bar}] {i}%", end="")
    print("\n✅ Data completed 100%!")