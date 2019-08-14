# Basic example of using framebuf capabilities on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
import time
import board
import busio
from digitalio import DigitalInOut

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# A reset line may be required if there is no auto-reset circuitry
reset_pin = DigitalInOut(board.D5)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# The I2C address for these displays is 0x3d or 0x3c, change to match
# A reset line may be required if there is no auto-reset circuitry
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=reset_pin)


display.fill(0)
display.show()

display.text('hello world', 0, 0, 1)
display.show()