#VideoMaker Effect
import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(250,250,250)] * 360  # Black Display
client = opc.Client('localhost:7890')
#The following function create an effect which will change
#the color of the screen from white to black. The animation
#will start at led 1 (python led 0) and move along the frame of the simulator
#ending in the middle of it. From outer side to inner side.
###
def Frame_Anim(x,y,z):
    for led in range(x,y,z):
        led_wall[led] = (0,0,0)
        time.sleep(0.03)
        client.put_pixels(led_wall)
###
Frame_Anim(0,60,1)
Frame_Anim(119,360,60)
Frame_Anim(359,300,-1)
Frame_Anim(300,119,-60)
Frame_Anim(60,118,1)
Frame_Anim(118,358,60)
Frame_Anim(298,241,-1)
Frame_Anim(241,122,-60)
Frame_Anim(121,179,1)
Frame_Anim(238,181,-1)

led = 0
mod = 1
count = 0
start = 0 # left side of the screen (+- till middle)
limit = 60 # right side of the screen (+- till middle)

while True: #keep running
    led_wall = [(0,0,0)]*360  # Black Display
    if count == limit: #Right side of the screen
        mod = -1 # Allow the green line to move backward (right to left)
        start += 1 #add to start count
    if count == start: #Left side of the screen
        mod = 1 # Allow the green line to move forward (left to right)
        limit -= 1 # substract to limit count
    if start > limit: # if start exceed vals of limit
        break#break the loop

    
    for rows in range(6): # consider all rows
        led_wall[rows*60 + count] = (0, 255, 0) # set green for moving line
    for rows in range(6): # consider all rows
        for led in range(start): # left part of the screen
            led_wall[led+(rows*60)] = (153,50,204) # set purple as setting wall color
        for led in range(limit,60): #rigth part of the screen
            led_wall[led+(rows*60)] = (153,50,204) # set purple as setting wall color

    client.put_pixels(led_wall)
    count += mod #allows th green line to move back and forth
    time.sleep(0.0001)
