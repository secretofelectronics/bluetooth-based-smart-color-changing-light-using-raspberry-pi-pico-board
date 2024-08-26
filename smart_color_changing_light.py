from machine import Pin, UART
import time
import neopixel

# Set up UART communication on UART0 (TX=Pin 0, RX=Pin 1)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Set up the NeoPixel LED
num_leds = 1  # Number of NeoPixel LEDs
pin = Pin(2, Pin.OUT)  # NeoPixel connected to Pin 2
np = neopixel.NeoPixel(pin, num_leds)

# Function to set the color of the NeoPixel LED
def set_color(r, g, b):
    np[0] = (r, g, b)
    np.write()

# Function to receive and process RGB data from the smartphone
def receive_and_set_color():
    while True:
        if uart.any():  # Check if there's any data received
            received_data = uart.read().decode('utf-8').strip()  # Read and decode the data
            try:
                # Expecting data in the format 'R,G,B' (e.g., '255,100,50')
                r, g, b = map(int, received_data.split(','))
                set_color(r, g, b)
                print(f"Set color to R:{r}, G:{g}, B:{b}")
            except ValueError:
                print("Invalid data received. Please send in 'R,G,B' format.")

# Main loop
try:
    receive_and_set_color()
except KeyboardInterrupt:
    print("Program stopped.")