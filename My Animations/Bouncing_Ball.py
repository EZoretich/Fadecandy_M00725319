# Bouncing Ball

import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(0,0,0)]*360 #LED wall will display only blue
client = opc.Client('localhost:7890')
#--------------------------------------- BALL ANIMATIONS
def Clear():
    for led in range(360): # All leds
        led_wall[led] = (0,0,0) #make them black
        led = led + 1

def Ball_Down(x):
    led = 0
    while led < 60:
        for rows in range(6):
          
            if ((led > (5 +x) and led < (8 +x)) and (rows==3 or rows==5) or
                ((led >(4 +x) and led < (9 + x) ) and rows == 4)):
                led_wall[led+rows*60] = (204,102,0) #Ball body
            if ((led == (2 + x) and rows == 3) or (led == (4 + x)  and rows == 2) or
                (led == (3 +x) and (rows == 1 or rows == 4))):
                led_wall[led+rows*60] = (255,255,255) # Movement trails
        led = led + 1
        client.put_pixels(led_wall)
def Ball_Up(y):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (11+y) and led < (14+y)) and (rows==0 or rows==2) or
                ((led > (10+y) and led < (15+y)) and rows == 1)):
                led_wall[led+rows*60] = (204,102,0) #Ball body
            if ((led == (8+y) and rows == 2) or (led == (10+y) and rows == 3) or
                (led == (9+y) and (rows == 1 or rows == 4))):
                 led_wall[led+rows*60] = (255,255,255) #Movement trails
        led = led + 1
        client.put_pixels(led_wall)

def Ball_Mid_Up(w):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (8+w) and led < (11+w)) and (rows==1 or rows==3) or
                ((led > (7+w) and led < (12+w)) and rows ==2 )):
                led_wall[led+rows*60] = (204,102,0) #Ball body
            if (((led == (6+w) or led == (9+w)) and rows ==4 ) or (led == (7+w) and rows ==3 ) or
                (led == (8+w) and rows == 5)):
                 led_wall[led+rows*60] = (255,255,255) #Movement trails
        led = led + 1
        client.put_pixels(led_wall)
        
def Ball_Mid_Down(z):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (14+z) and led < (17+z)) and (rows==2 or rows==4) or
                ((led > (13+z) and led < (18+z)) and rows ==3 )):
                led_wall[led+rows*60] = (204,102,0) #Ball body
            if ((led == (12+z) and rows ==2 ) or (led == (14+z) and rows ==1 ) or
                (led == (13+z) and (rows ==0  or rows ==3 ))):
                 led_wall[led+rows*60] = (255,255,255) #Movement trails
        led = led + 1
        client.put_pixels(led_wall)

#---------------------------------------- STICKMAN ANIMATIONS
def Stickman_Run(k):
    led = 0
    while led<60:
        for rows in range(6):
            if ((led > (11+k) and led < (14+k)) and (rows == 0 or rows == 1)):
                led_wall[led+rows*60] = (255,153,204) #pink face
            if ((led == (12+k) and (rows == 2 or rows == 3))):
                 led_wall[led+rows*60] = (0,255,0) #Shirt green
            if (((led == (10+k) or led == (14+k)) and rows == 1) or
                ((led == (11+k) or led == (13+k)) and rows == 2)):
                led_wall[led+rows*60] = (102,255,105) # Green sleeves
            if ((led == (11+k) and (rows == 4 or rows == 5)) or
                ((led > (12+k) and led < (15+k)) and rows == 4)):
                led_wall[led+rows*60] = (0,0,255) # pants
        led = led + 1
        client.put_pixels(led_wall)

def Stickman_Rest(j):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led >(15+j) and led <(18+j)) and (rows ==0 or rows ==1)):
                led_wall[led+rows*60] = (255,153,204) #pink face
            if ((led == (16+j) and (rows == 2 or rows == 3))):
                 led_wall[led+rows*60] = (0,255,0) # Green t-shirt
            if (((led == (14+j) or led == (18+j)) and rows == 3) or
                ((led == (15+j) or led == (17+j)) and rows == 2)):
                led_wall[led+rows*60] = (102,255,105) # Green sleeves
            if ((led == (17+j) and (rows == 4 or rows == 5)) or
                ((led > (13+j) and led < (16+j)) and rows == 4)):
                led_wall[led+rows*60] = (0,0,255) # pants
        led = led + 1
        client.put_pixels(led_wall)

#------------- MAIN CODE (LOOP)
#------- The loop will multiplicate functions parameters (exponential)
#------- Creating a scrolling, running effect for both ball and Stickman
while True: # Keep running
    for i in range(5): # iterate 5 times (then repeats)
        Ball_Down(i*11)# 1i*11, 2i*11, 3i*11....
        Stickman_Run(i*11)# 1i*11, 2i*11, 3i*11....
        time.sleep(0.5)# Minimum value that sllep can have without crashing the animation
        Clear()# Make screen all black
        Ball_Mid_Up(i*11) # 1i*11, 2i*11, 3i*11....
        Stickman_Rest(i*11) # 1i*11, 2i*11, 3i*11....
        time.sleep(0.5) # wait
        Clear() # Clear screen (all black)
        Ball_Up(i*11) # 1i*11, 2i*11, 3i*11....
        Stickman_Run(i*11+6)# Since the Stickman has only 2 functions,
                            # And they needed to be moved further: 18*11+6, 2i*11+6....
        time.sleep(0.5) # wait
        Clear() # clear screen (all black)
        Ball_Mid_Down(i*11) # 1i*11, 2i*11, 3i*11....
        Stickman_Rest(i*11+6)# # 1i*11+6, 2i*11+6, 3i*11+6....
        time.sleep(0.5) # wait
        Clear() # clear screen
