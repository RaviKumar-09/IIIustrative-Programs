# Input temperature and type

temp = float(input("Enter the temperature: "))
unit = input("Is this Celsius (C) or Fahrenheit (F)? ").upper()

# Convert temperature
if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted}°F.")
elif unit == "F":
    converted = (temp - 32) * 5/9
