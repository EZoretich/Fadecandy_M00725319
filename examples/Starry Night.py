# Starry night
# Blue background, Moon (Bicolor) and Blinking starts

import opc
import time
import colorsys
import random
from random import choice

led_wall = [(0,0,255)]*360 #LED wall will display only blue

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

while True:
    random.choices(led_wall, 15) = (255,255,255)
    time.sleep(.1)
    client.put_pixels(leds)
