#CHRISTMAS LIGHTS(?)

import opc
import time
import colorsys
import numpy
import random
import math

def Clear():
    led_wall = [(0,0,0)]*360
    client.put_pixels(led_wall)

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
    time.sleep(0.02)

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
#----------------------------------
led = 0
while led < 30:
    for led in range(30):
        shade = (102 * ((led/10) - 0.2), 0, 204 * ((led/10) - 0.2))
        #shade2 = (255 * abs(math.sin(led/20) - 0.5),128 * abs(math.sin(led/40) - 0.5),0)
        for rows in range(6):
            led_wall[29-led + rows*60] = shade
            led_wall[30+led + rows*60] = shade
        led = led + 1
        client.put_pixels(led_wall)
        time.sleep(0.1)

led = 0
while led < 30:
    for led in range(30):
        shade2 = (255 * ((led/10) - 0.2),128 * ((led/10) - 0.2),0)
        for rows in range(6):
            led_wall[29-led + rows*60] = shade2
            led_wall[30+led + rows*60] = shade2
        led = led + 1
        client.put_pixels(led_wall)
        time.sleep(0.1)

#----------------------------------
led = 0
while led < 30:
    for led in range(30):
        rgb = (0, 255 * abs(math.sin(led/60) - 0.5), 0)
        rgb2 = (0, 0, 255 * abs(math.sin(led/60) - 0.5))
        for rows in range (6):
            led_wall[led + rows*60] = rgb
            led_wall[59-led + rows*60] = rgb2
        client.put_pixels(led_wall)
        led = led + 1
        time.sleep(0.1)

#----------------------------------
led = 0
while led < 30:
    for led in range(30):
        rgb = (0, 0, 255 * abs(math.sin(led/60) - 0.5))
        rgb2 = (0, 255 * abs(math.sin(led/60) - 0.5), 0)
        for rows in range (6):
            led_wall[led + rows*60] = rgb
            led_wall[59-led + rows*60] = rgb2
        client.put_pixels(led_wall)
        led = led + 1
        time.sleep(0.1)
#-------------------------------------- iter. T F T /n F T F
led = 0
while led < 60:
    for rows in range(6):
        if ((not((rows+2)%2)) and (not led % 2)):
            led_wall[59-led+rows*60] = (255,0,255)
        elif ((not((rows+2)%2)) and  led % 2):
            led_wall[59-led+rows*60] = (224,238,238)
        elif (((rows+2)%2) and  led % 2):
            led_wall[59-led+rows*60] = (255,0,255)
        else:
            led_wall[59-led+rows*60] = (224,238,238)
    client.put_pixels(led_wall)
    led = led + 1
    time.sleep(0.1)

#----------------------------------------- Alternating col of rows, with nupy rolling effect
for led in range(60):
    for rows in range(6):
        if rows %2:
            led_wall[59-led+rows*60] = (128 * (led/30),255 * (led/30),0)
            client.put_pixels(led_wall)
            time.sleep(0.003)
        else:
            led_wall[led+rows*60] = (255 * (led/30),128 * (led/30),0)
            time.sleep(0.01)
while True:
    led_wall = numpy.roll(led_wall, 3)
    client.put_pixels(led_wall)
    time.sleep(0.02)
    #time.sleep(5)
    break

#----------------------------------------- DNA
Clear()
led = 0
while led < 60:
    for rows in range(6):
        led_wall[led+rows*60] = (0,255,255)
        led_wall[59-led+rows*60] = (255,0,255)
        led = led + 1
        time.sleep(0.1)
        client.put_pixels(led_wall)
