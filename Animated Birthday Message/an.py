# Import
import time

message = "🎉🎂 Happy Birthday to You! 🎂🎉"

for char in message:
    print(char, end="", flush=True)
    time.sleep(0.1)  # Delay to create animation effect
print("\nHave a fantastic day! 😊")