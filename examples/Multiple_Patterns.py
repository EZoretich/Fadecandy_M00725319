#CHRISTMAS LIGHTS

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
#------------------------------------------ Function for DNA pattern
def DNA():
    led = 0
    while led < 60: #Consider all rows at the same time (60 leds in one row)
        for rows in range(6): # Divide by rows
            led_wall[led+rows*60] = (0,255,255) # Light Blue LEDs
            led_wall[59-led+rows*60] = (255,0,255) # Pink LEDs
            led = led + 1
            time.sleep(0.07)
            client.put_pixels(led_wall) # Display on Simulator

#------------------------------------------ Function for Christmas Tree (Lights OFF)
def Tree_off():
    led = 0
    while led < 60: #Consider all rows at the same time (60 leds in one row)
        for rows in range(6): # Divide by rows
                    # GREEN LEDS (Tree's leaves)
            if ((led == 31 and rows == 0) or
                ((led >29 and led < 33) and (rows == 1 or rows == 3)) or
                ((led > 28 and led < 34) and (rows == 2 or rows == 4))):
                led_wall[led + rows*60] = (0,255,0)
                    # BROWN LED (Log)
            if led == 31 and rows == 5:
                led_wall[led + rows*60] = (153,76,0)
        led = led + 1
    client.put_pixels(led_wall) # Display on Simulator

##------------------------------------------ Function for Christmas Tree (Lights ON)
def Tree_on():
    led = 0
    while led < 60: #Consider all rows at the same time (60 leds in one row)
        for rows in range(6): # Divide by rows
                        # GREEN LEDS (Tree's leaves)
            if ((led == 31 and rows == 0) or
                ((led >29 and led < 33) and (rows == 1 or rows == 3)) or
                ((led > 28 and led < 34) and (rows == 2 or rows == 4))):
                led_wall[led + rows*60] = (0,255,0)
                        # BROWN LED (Log)
            if led == 31 and rows == 5:
                led_wall[led + rows*60] = (153,76,0)
                        # LIGHT BLUE LED (Christmas decoration)
            if led == 32 and rows == 1:
                led_wall[led + rows*60] = (0,255,255)
                        # RED LED (Christmas decoration)
            if led == 30 and rows == 2:
                led_wall[led + rows*60] = (255,0,0)
                        # PINK LED (Christmas decoration)
            if led == 32 and rows == 4:
                led_wall[led + rows*60] = (255,51,255)
                        # YELLOW LEDS (Animation lightning effect)
            if (((led == 26 or led == 36) and (rows == 0 or rows == 5)) or
                ((led == 27 or led == 35) and (rows == 1 or rows == 4))):
                led_wall[led + rows*60] = (255,255,0)
        led = led + 1
    client.put_pixels(led_wall) # Display on Simulator
#---------------------------------------------
led_wall = [(0, 0, 0)]*360 #Black Display
fade = 10

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

s = 1.0
v = 1.0

#------------------------------------------ Pattern 1 - Random Colors (from 1 to 360)
while True: # Keep running (whole animation keeps looping)
    for hue in range(360): #Consider all 360 leds
        rgb_fract = colorsys.hsv_to_rgb(random.randint(hue-160,hue+160)/360.0, s, v) # Colorsys returns floats between 0 and 1
        r_fl = rgb_fract[0] # Extract said floating point numbers
        g_fl = rgb_fract[1]
        b_fl = rgb_fract[2]

        rgb = (r_fl*255, g_fl*255, b_fl*255) # Create new tuple with corrected values
        led_wall[hue] = rgb # Assing above values to main list of tuples
        client.put_pixels(led_wall) # Display
        time.sleep(0.02)

#------------------------------------------ Pattern 2 - White and Red Stripes
    led = 0
    while led < 60: #Consider all rows at the same time (60 leds in one row)
        if led % 2 == 0: # if led is in even pos
            for line in range(6): # divide by rows
                led_wall[led + line*60] = (255, 255, 255) # Display White
                
                
        else: # if led is in an odd pos
            for line in range(6): # divide by rows
                led_wall[led + line*60] = (255, 0, 0) # Display Red
                
        time.sleep(0.1)
        client.put_pixels(led_wall) # Display
        led = led + 1

#------------------------------------------ Pattern 3 - Reverse Curtains: Reverse fading from inner screen to extremities(1-Purple 2-Orange)
    led = 0
    while led < 30: #Consider all rows at the same time, but screen is divided in two sections (right and left)
        for led in range(30):
                    # PURPLE LEDS (fading)
            shade = (102 * ((led/10) - 0.2), 0, 204 * ((led/10) - 0.2)) # New tuple with values for fading
            for rows in range(6): # divide by rows
                led_wall[29-led + rows*60] = shade # Assign new values to main list of tuples
                led_wall[30+led + rows*60] = shade
            led = led + 1
            client.put_pixels(led_wall) # Display
            time.sleep(0.1)

    led = 0
    while led < 30: #Consider all rows at the same time, but screen is divided in two sections (right and left)
        for led in range(30):
                    # ORANGE LEDS (Fading)
            shade2 = (255 * ((led/10) - 0.2),128 * ((led/10) - 0.2),0) # New tuple with values for fading
            for rows in range(6): # divide by rows
                led_wall[29-led + rows*60] = shade2 # Assign new values to main list of tuples
                led_wall[30+led + rows*60] = shade2
            led = led + 1
            client.put_pixels(led_wall) # Display
            time.sleep(0.1)

#------------------------------------------ Pattern 4 - Curtains: Fading from screen's extremities to inner part ( Right = Blue ; Left = Green)
    led = 0
    while led < 30: #Consider all rows at the same time, but screen is divided in two sections (right and left)
        for led in range(30):
            rgb = (0, 255 * abs(math.sin(led/60) - 0.5), 0) # New tuple with values for fading
            rgb2 = (0, 0, 255 * abs(math.sin(led/60) - 0.5)) # New tuple with values for fading
            for rows in range (6): # divide by rows
                led_wall[led + rows*60] = rgb # Assign new values to main list of tuples
                led_wall[59-led + rows*60] = rgb2 # Assign new values to main list of tuples
            client.put_pixels(led_wall) # Display
            led = led + 1
            time.sleep(0.1)

#------------------------------------------ Pattern 5  - Curtains: Fading from screen's extremities to inner part ( Right = Green ; Left = Blue)
    led = 0
    while led < 30: #Consider all rows at the same time, but screen is divided in two sections (right and left)
        for led in range(30):
            rgb = (0, 0, 255 * abs(math.sin(led/60) - 0.5)) # New tuple with values for fading
            rgb2 = (0, 255 * abs(math.sin(led/60) - 0.5), 0) # New tuple with values for fading
            for rows in range (6): # divide by rows
                led_wall[led + rows*60] = rgb # Assign new values to main list of tuples
                led_wall[59-led + rows*60] = rgb2 # Assign new values to main list of tuples
            client.put_pixels(led_wall) # Display
            led = led + 1
            time.sleep(0.1)
#------------------------------------------ Pattrn 6 - Gray and Pink Chess Board Pattern
    led = 0
    while led < 60: #Consider all rows at the same time (60 leds in one row)
        for rows in range(6): # divide by rows
                        # PINK LEDS
            if ((not((rows+2)%2)) and (not led % 2)): 
                led_wall[59-led+rows*60] = (255,0,255)
                        # White-ish LEDS
            elif ((not((rows+2)%2)) and  led % 2):
                led_wall[59-led+rows*60] = (224,238,238)
            elif (((rows+2)%2) and  led % 2):
                led_wall[59-led+rows*60] = (255,0,255)
            else:
                led_wall[59-led+rows*60] = (224,238,238)
        client.put_pixels(led_wall) # Display
        led = led + 1
        time.sleep(0.1)

#------------------------------------------ Pattern 7 - Rolling Alternating Rows (0 and Even = Green ; Odd = Orange/Yellow)
    for led in range(60): # Consider all leds in row (all rows scrolling) 
        for rows in range(6): # divide by rows
            if rows %2:
                        # GREEN LEDS (Fading)
                led_wall[59-led+rows*60] = (128 * (led/30),255 * (led/30),0)
                client.put_pixels(led_wall)
                time.sleep(0.003)
            else:
                        # ORANGE LEDS (Fading)
                led_wall[led+rows*60] = (255 * (led/30),128 * (led/30),0)
                time.sleep(0.01)
    delay = 8 # Variable storing 8 seconds delay
    end_time = time.time()+delay # Variable for current time + set delay
    while True: # Keep running
        led_wall = numpy.roll(led_wall, 3) # Roll tuple by 3
        client.put_pixels(led_wall) # Display
        time.sleep(0.02)
        if time.time() > end_time: # Check, if delay time already passed
            break # End the loop

#------------------------------------------Pattern 7 - Pink and Light Blue DNA
    Clear() # Clear screen ( all black)
    DNA() # Display DNA animation
    led = 0
    delay = 7 # variable for 7 seconds delay
    end_time = time.time() + delay # variable for current time + delay
    while True: # Keep running
        led_wall_preshift = [] # Make new (empty) array for scrolling effect
        led_wall_preshift.append(numpy.roll(led_wall[0:60], 3)) # add first row, rolling tuple by 3
        led_wall_preshift.append(numpy.roll(led_wall[60:120], 3)) # add second row, rolling tuple by 3
        led_wall_preshift.append(numpy.roll(led_wall[120:180], 3)) # add third row, rolling tuple by 3
        led_wall_preshift.append(numpy.roll(led_wall[180:240], 3)) # add fouth row, rolling tuple by 3
        led_wall_preshift.append(numpy.roll(led_wall[240:300], 3)) # add fifth row, rolling tuple by 3
        led_wall_preshift.append(numpy.roll(led_wall[300:360], 3)) # add sixth row, rolling tuple by 3

        led_wall = [] # empty main list

        #Add all rows to main list
        for x in led_wall_preshift:
            for y in x:
                led_wall.append(y)
                                
        client.put_pixels(led_wall) # Display
        time.sleep(0.1)
        if time.time() > end_time: # Check, if delay has already passed
            break # End the loop
#------------------------------------------Pattern 8 - Blinking Christmas Tree
    num = 5
    for x in range(num):
        Clear() # Clear screen (all black)
        Tree_off() # Send christmas tree animation (off first)
        time.sleep(0.7) # wait
        Tree_on() # Send christmas tree animation (on)
        time.sleep(0.7)# wait
        Clear() # clear screen again
        # Repeat 3 more times
    '''Tree_off()
    time.sleep(0.7)
    Tree_on()
    time.sleep(0.7)
    Clear()
    Tree_off()
    time.sleep(0.7)
    Tree_on()
    time.sleep(0.7)
    Clear()
    Tree_off()
    time.sleep(0.7)
    Tree_on()
    time.sleep(0.7)
    Clear()'''
