# Piramids

import opc
import time
import colorsys
import numpy
import random
import math

def Clear():
    for led in range(360): # All leds
        led_wall[led] = (0,0,0) #make them black
        led = led + 1


led_wall = [(0,0,0)]*360 #LED wall will display only blue
client = opc.Client('localhost:7890')
def Triangle(*argv):
    led = int(argv[0])
    start = int(argv[1])
    stop = int(argv[2])
    step = int(argv[3])
    for rows in range(start,stop,step):
        for i in range (3-rows):
            R = random.randint(i-20,i+360) #3 different variable, cause if I would have use only R, colors would have been only shades of grey
            G = random.randint(i-20,i+360)
            B = random.randint(i-20,i+360)
            led_wall[led+(i+rows)*60] = (R,G,B)
            led_wall[240-led+(i+rows)*60] = (R,G,B)
        led+=1
        client.put_pixels(led_wall)
        time.sleep(0.03)
while True:
    for x in range(0,60,20):
        Triangle(x+0,5,-1,-1)
        Triangle(x+5,0,6,1)
        Triangle(x+10,5,-1,-1)
        Triangle(x+15,0,6,1)
