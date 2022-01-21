#MULTIPLE PATTERNS

#Experimenting with patterns

import opc
import time
import colorsys
import numpy
import random
#import itertools

led_wall = [(0, 0, 0)]*360 #Black Display
fade = 10

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

s = 1.0
v = 1.0

#client.put_pixels(itertools.repeat(72))

#for led in range(360): # Colors are not as nice as I was hoping for (too dark and sad)
#    led_wall[led] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
#    client.put_pixels(led_wall) #send out
#    time.sleep(0.1)

for hue in range(360):
    rgb_fract = colorsys.hsv_to_rgb(random.randint(hue-160,hue+160)/360.0, s, v)
    r_fl = rgb_fract[0]
    g_fl = rgb_fract[1]
    b_fl = rgb_fract[2]

    rgb = (r_fl*255, g_fl*255, b_fl*255)
    led_wall[hue] = rgb
    client.put_pixels(led_wall)
    time.sleep(0.01)

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

#Sequence starts from edges and conjoin in the middle
#ADD nice fading
led = 0
while led < 30:
    for i in range(60):
        rgb = (0, 255, 0)
        rgb2 = (0, 0, 255)
        for x in range (6):
            led_wall[i + x*60] = rgb
            led_wall[59-i + x*60] = rgb2
    #led_wall = numpy.roll(led_wall, 3)
    client.put_pixels(led_wall)
    time.sleep(0.1)
        
        #led_wall[led + rows*60] = (0,255,0)
        #led_wall[59-led +rows*60] = (0,0,255)

    #client.put_pixels(led_wall)
    #time.sleep(0.1)
    #led = led + 1
    #for B in range(1,360,2):
        #led_wall[B] = (0,0,255)
        #B = B +1
    #client.put_pixels(led_wall)
    #time.sleep(0.1)
    
