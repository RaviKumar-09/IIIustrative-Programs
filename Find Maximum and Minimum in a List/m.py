from machine import Pin, I2C
import ssd1306
import time


# Initialize I2C
i2c = I2C(0, scl=Pin(3), sda=Pin(2), freq=400000)


# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Function to display text on OLED
def display_text(text, x=0, y=0, clear=True):
    if clear:
        oled.fill(0)  # Clear the display
    oled.text(text, x, y)
    oled.show()

# Main loop
try:
    while True:
        display_text("Welcome to", 0, 0)
        display_text("Smart Notice", 0, 16, clear=False)
        display_text("Board", 0, 32, clear=False)
        time.sleep(2)
        
        display_text("Raspberry Pi", 0, 0)
        display_text("OLED Display", 0, 16, clear=False)
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Program stopped")