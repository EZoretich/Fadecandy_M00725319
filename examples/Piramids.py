# Piramids

import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(0,0,0)]*360 #LED wall will display only blue
client = opc.Client('localhost:7890')

def up (*argv):
    led = int(argv[0])
    start = int(argv[1])
    stop = int(argv[2])
    step = int(argv[3])
    #print(led)
    for rows in range(start,stop,step):
        #print("break")
    
        for i in range (6-rows):        
            #print(i+rows)
            #print("led", led)
            led_wall[led+(i+rows)*60] = (255,255,255)
        led+=1
        client.put_pixels(led_wall)
        time.sleep(0.1)
        
up(0,5,-1,-1)
up(5,0,6,1)
up(10,5,-1,-1)
up(15,0,6,1)
#
up(20,5,-1,-1)
up(25,0,6,1)
up(30,5,-1,-1)
up(35,0,6,1)
#
up(40,5,-1,-1)
up(45,0,6,1)
#up(50,5,-1,-1)
#up(55,0,6,1)

'''led_wall[0+5*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[1+5*60] = (255,255,255)
led_wall[1+4*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[2+5*60] = (255,255,255)
led_wall[2+4*60] = (255,255,255)
led_wall[2+3*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[3+5*60] = (255,255,255)
led_wall[3+4*60] = (255,255,255)
led_wall[3+3*60] = (255,255,255)
led_wall[3+2*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[4+5*60] = (255,255,255)
led_wall[4+4*60] = (255,255,255)
led_wall[4+3*60] = (255,255,255)
led_wall[4+2*60] = (255,255,255)
led_wall[4+1*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[5+5*60] = (255,255,255)
led_wall[5+4*60] = (255,255,255)
led_wall[5+3*60] = (255,255,255)
led_wall[5+2*60] = (255,255,255)
led_wall[5+1*60] = (255,255,255)
led_wall[5+0*60] = (255,255,255)
client.put_pixels(led_wall)
time.sleep(0.1)
led_wall[6+5*60] = (255,255,255)
led_wall[6+4*60] = (255,255,255)
led_wall[6+3*60] = (255,255,255)
led_wall[6+2*60] = (255,255,255)
led_wall[6+1*60] = (255,255,255)
client.put_pixels(led_wall)
'''
