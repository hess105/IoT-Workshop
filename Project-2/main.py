# I2C Scanner MicroPython
from machine import Pin, SoftI2C
import ssd1306
import dht
import errno
import utime   # Library for timing


# You can choose any other combination of I2C pins
# This function initalizes the i2c
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

# This scanner script will how if an I2C device is connected
print('I2C SCANNER')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:', len(devices))

  for device in devices:
    print("I2C hexadecimal address: ", hex(device))
    
# Define variables and initalize the display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Here we will also define the dht11 pin
# Changing two will change which GPIO we are using
dht_pin = machine.Pin(11, machine.Pin.IN)

# Create the DHT object
dht_sensor = dht.DHT22(dht_pin)

oled.text('Sample Text', 0, 20)

oled.show()

while True:
    # Read the data
    try:
        dht_sensor.measure()
    except OSError as e:
        print(e)
        
        
    # Break up the object into its components and assign to indivudal variables
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    # Output the data to the screen
    oled.text("Temp: {} C".format(temperature), 0, 0)
    oled.text('Hum: {}%'.format(humidity), 0, 10)
    oled.text('Sample Text', 0, 20)

    oled.show()
        
    utime.sleep(2)  # Wait for 1 second
