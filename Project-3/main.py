
from simple import MQTTClient
import network
import time
from time import sleep
from machine import Pin

# WiFi Setup
WiFi_SSID = "**********"
WiFi_PASS = "*************"

# Thingspeak Setup
SERVER = "mqtt.thingspeak.com"

# MQTT Setup
client = MQTTClient("umqtt_client", SERVER) CHANNEL_ID = "********" WRITE_API_KEY = "***************"

p23=Pin(23, Pin.IN) #initializing the pin for dht11

d=dht.DHT11(p23) #initializing the dht11

# Connect to WiFi
def do_connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
      if not wlan.isconnected():
           print('connecting to network...')
           wlan.connect(WiFi_SSID, WiFi_PASS)
           while not wlan.isconnected():
              pass print('network config:', wlan.ifconfig())

do_connect()

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

while True:
  
  d.measure() #collect data from the dht11

  t=d.temperature() #read temperature

  h=d.humidity() #read humidity

  payload = "field1="+str(t)+"&field2="+str(h) #prepare the text to send

  client.connect() #connect to the server

  client.publish(topic, payload) #send the text

  client.disconnect() #disconnect from the server

  time.sleep(60) #waiting 1 min