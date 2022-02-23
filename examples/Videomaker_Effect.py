#VideoMaker Effect
import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(0, 0, 0)] * 360  # Black Display
client = opc.Client('localhost:7890')
fade = 10

led = 0
mod = 1
count = 0
start = 0 # left side of the screen (+- till middle)
limit = 60 # right side of the screen (+- till middle)

while True: #keep running
    led_wall = [(0,0,0)]*360  # Black Display
    if count == limit: #Right side of the screen
        mod = -1 # move 1 backward
        start += 1 #add to start count
    if count == start: #Left side of the screen
        mod = 1 #move 1 backward
        limit -= 1 # substract to limit count
    if start > limit: # if start exceed vals of limit
        break#break the loop
    
    for rows in range(6): # consider all rows
        led_wall[rows*60 + count] = (0, 255, 0) # set green for moving line
    for rows in range(6): # consider all rows
        for led in range(start): # left part of the screen
            led_wall[led+(rows*60)] = (153,50,204) # set purple as setting wall color
        for led in range(limit,60):
            led_wall[led+(rows*60)] = (153,50,204) # set purple as setting wall color

    client.put_pixels(led_wall)
    count += mod
    time.sleep(0.005)
