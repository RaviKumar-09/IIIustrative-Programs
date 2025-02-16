# Current slipper condition
slipper_condition = input("Enter slipper condition (Good/Worn Out): ").strip().lower()

# Decision making
if slipper_condition == "worn out":
    print("Your slippers are worn out! 🥿➡️🛍️ Time to buy new ones!")
else:
    print("Your slippers are still in good condition. No need to buy new ones! 😊")