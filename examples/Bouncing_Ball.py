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
                led_wall[led+rows*60] = (204,102,0)
            if ((led == (2 + x) and rows == 3) or (led == (4 + x)  and rows == 2) or
                (led == (3 +x) and (rows == 1 or rows == 4))):
                led_wall[led+rows*60] = (255,255,255)
        led = led + 1
        client.put_pixels(led_wall)
def Ball_Up(y):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (11+y) and led < (14+y)) and (rows==0 or rows==2) or
                ((led > (10+y) and led < (15+y)) and rows == 1)):
                led_wall[led+rows*60] = (204,102,0)
            if ((led == (8+y) and rows == 2) or (led == (10+y) and rows == 3) or
                (led == (9+y) and (rows == 1 or rows == 4))):
                 led_wall[led+rows*60] = (255,255,255)
        led = led + 1
        client.put_pixels(led_wall)

def Ball_Mid_Up(w):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (8+w) and led < (11+w)) and (rows==1 or rows==3) or
                ((led > (7+w) and led < (12+w)) and rows ==2 )):
                led_wall[led+rows*60] = (204,102,0)
            if (((led == (6+w) or led == (9+w)) and rows ==4 ) or (led == (7+w) and rows ==3 ) or
                (led == (8+w) and rows == 5)):
                 led_wall[led+rows*60] = (255,255,255)
        led = led + 1
        client.put_pixels(led_wall)
        
def Ball_Mid_Down(z):
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > (14+z) and led < (17+z)) and (rows==2 or rows==4) or
                ((led > (13+z) and led < (18+z)) and rows ==3 )):
                led_wall[led+rows*60] = (204,102,0)
            if ((led == (12+z) and rows ==2 ) or (led == (14+z) and rows ==1 ) or
                (led == (13+z) and (rows ==0  or rows ==3 ))):
                 led_wall[led+rows*60] = (255,255,255)
        led = led + 1
        client.put_pixels(led_wall)

#---------------------------------------- STICKMAN
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
                 led_wall[led+rows*60] = (0,255,0)
            if (((led == (14+j) or led == (18+j)) and rows == 3) or
                ((led == (15+j) or led == (17+j)) and rows == 2)):
                led_wall[led+rows*60] = (102,255,105) # Green sleeves
            if ((led == (17+j) and (rows == 4 or rows == 5)) or
                ((led > (13+j) and led < (16+j)) and rows == 4)):
                led_wall[led+rows*60] = (0,0,255) # pants
        led = led + 1
        client.put_pixels(led_wall)

#------------- PUT IN A LOOP
        #---------- Maybe add 2 more transitions (Up&Down), make bounce effect smoother
# First lup
while True:
    Ball_Down(0)
    Stickman_Run(0)
    time.sleep(0.5)
    Clear()
    Ball_Mid_Up(0)
    Stickman_Rest(0)
    time.sleep(0.5)
    Clear()
    Ball_Up(0)
    Stickman_Run(8)
    time.sleep(0.5)
    Clear()
    Ball_Mid_Down(0)
    Stickman_Rest(8)
    time.sleep(0.5)
    Clear()
    '''# Second lup
    Ball_Down(11)
    Stickman_Run(15)
    time.sleep(0.5)
    Clear()
    Ball_Mid_Up(11)
    Stickman_Rest(15)
    time.sleep(0.5)
    Clear()
    Ball_Up(11)
    Stickman_Run(23)
    time.sleep(0.5)
    Clear()
    Ball_Mid_Down(11)
    Stickman_Rest(23)
    time.sleep(0.5)
    Clear()
    # Third lup'''
