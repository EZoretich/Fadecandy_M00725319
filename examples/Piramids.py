# Piramids

import opc
import time
import colorsys
import numpy
import random
import math

led_wall = [(0,0,0)]*360 #LED wall will display only blue
client = opc.Client('localhost:7890')
#R = random.randint(i-50,i+360)
#G = random.randint(i-50,i+360)
#B = random.randint(i-50,i+360)
def up (*argv):
    led = int(argv[0])
    start = int(argv[1])
    stop = int(argv[2])
    step = int(argv[3])
    for rows in range(start,stop,step):
        for i in range (3-rows):
            R = random.randint(i-50,i+360) #3 different variable, cause if I would have use only R, colors would have been only shades of grey
            G = random.randint(i-50,i+360)
            B = random.randint(i-50,i+360)
            led_wall[led+(i+rows)*60] = (R,G,B)
            led_wall[240-led+(i+rows)*60] = (R,G,B)
        led+=1
        client.put_pixels(led_wall)
        time.sleep(0.03)

for x in range(0,60,20):
    up(x+0,5,-1,-1)
    up(x+5,0,6,1)
    up(x+10,5,-1,-1)
    up(x+15,0,6,1)

'''up(1,5,-1,-1)
up(8,0,6,1)
up(13,5,-1,-1)
up(18,0,6,1)
#
up(23,5,-1,-1)
up(28,0,6,1)
up(33,5,-1,-1)
up(38,0,6,1)
#
up(43,5,-1,-1)
up(48,0,6,1)
up(50,5,-1,-1)
up(55,0,6,1)
'''
