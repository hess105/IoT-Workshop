# Raspberry Pi Pico LED Flashing Program
# This program flashes the onboard LED of Raspberry Pi Pico.

# -------------------------------------------------------------------------------------------
# This section of the code is the imports.
# Here we call for prebuilt libraries to be included so we can use their functionality.
# Very similar to all other programs.
import machine # Library for conrolling hardware
import utime   # Library for timing

# -------------------------------------------------------------------------------------------
# Here we are defining a variable to a value. In this case we are assigning the LED_PIN to
# a value of 25. This corresponds with the hardware code that PIN 25 is connected to the
# onboard LED.
LED_PIN = 25

# -------------------------------------------------------------------------------------------
# In this step we are initializing a new Pin object named 'led'. We are using a function
# that we imported, 'machine', and using its Pin command to initalize the pin for our use.
# The Pin command takes two arguments (LED_PIN) and (machine.Pin.OUT). The machine.Pin.OUT is
# an argument that specifices that the pin is an output pin.
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# -------------------------------------------------------------------------------------------
# Just as in Python, we can define our own functions. Here we define a function that toggles
# the value of the LED. We can also assign the output using led.value(1) or led.value(0).
def toggle_led():
    led.value(not led.value())

# -------------------------------------------------------------------------------------------
# The general programming structure used in microprocessors in a main loop that continuously
# repeats checking for conditions or running other functions. In this case we can use while True:
# which create an infinite loop.
while True:
    toggle_led()    # Toggle LED state
    utime.sleep(1)  # Wait for 1 second