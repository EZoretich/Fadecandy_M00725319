# Bouncing Ball

import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(0,0,0)]*360 #LED wall will display only blue
client = opc.Client('localhost:7890')

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
            if ((led > (+y) and led < (14+y)) and (rows==0 or rows==2) or
                ((led > (10+y) and led < (15+y)) and rows == 1)):
                led_wall[led+rows*60] = (204,102,0)
            if ((led == (8+y) and rows == 2) or (led == (10+y) and rows == 3) or
                (led == (9+y) and (rows == 1 or rows == 4))):
                 led_wall[led+rows*60] = (255,255,255)
        led = led + 1
        client.put_pixels(led_wall)
        
def Ball_Mid_Down(z):
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

#------------- PUT IN A LOOP
        #---------- Maybe add 2 more transitions (Up&Down), make bounce effect smoother
def Bounce():
    Ball_Down(0)
    time.sleep(0.8)
    Clear()
    Ball_Up(0)
    time.sleep(0.8)
    Clear()
    #
    Ball_Down(11)
    time.sleep(0.8)
    Clear()
    Ball_Up(11)
    time.sleep(0.8)
    Clear()
    #
    Ball_Down(22)
    time.sleep(0.8)
    Clear()
    Ball_Up(22)
    time.sleep(0.8)
    Clear()
    #
    Ball_Down(33)
    time.sleep(0.8)
    Clear()
    Ball_Up(33)
    time.sleep(0.8)
    Clear()
    #
    Ball_Down(44)
    time.sleep(0.8)
    Clear()
    Ball_Up(44)
    time.sleep(0.8)
    Clear()

Bounce()
