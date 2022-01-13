#Experimenting with patterns

import opc
import time
import colorsys
import numpy
import random

led_wall = [(0, 0, 0)]*360 #Black Display
fade = 10
led = 0

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

#Sequence should scroll through all led, Blue --> make them change color

for led in range(360):#all leds

    if led >= 0 or led < 360:
            led_wall[led] = (0, 0, 255)
            time.sleep(0.1)
            client.put_pixels(led_wall)
    if led > 1:
            led_wall[led-1] = (0, 255, 0)
            time.sleep(0.1)
            client.put_pixels(led_wall)
    if led > 2:
            led_wall[led-2] = (255, 0, 0)
            time.sleep(0.1)
            client.put_pixels(led_wall)
    if led > 3:
            led_wall[led-3] = (200, 250, 50)
            time.sleep(0.1)
            client.put_pixels(led_wall)
    if led > 4:
            led_wall[led-4] = (0, 200, 150)
            time.sleep(0.1)
            client.put_pixels(led_wall)
            

    #led_wall[led] = (0, 0, 255)
    #time.sleep(0.1)
    #client.put_pixels(led_wall)
    #time.sleep(1)
    #led_wall = numpy.roll(led_wall, 1) # list, shift val

    

#Sequence should create white and red stripes
led = 0
while led < 60: 
    if led % 2 == 0: # if led is in even pos
        for line in range(6): # divide by rows
            led_wall[led + line*60] = (255, 255, 255)
            
            
    else:
        for line in range(6):
            led_wall[led + line*60] = (255, 0, 0)
            
    time.sleep(0.1)
    client.put_pixels(led_wall)
    led = led + 1


