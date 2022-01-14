import opc
import time
import random

def  Mario():     
    led = 0

    while led < 60:
        for rows in range(6):
        #red              head                             jumper
            if ( led > 12 and led < 16 and rows == 2) or ( rows == 4 and (led == 13 or led == 15)  ) :
                leds[led + rows*60] = (255,0,0)
            if ( led > 12 and led < 17 and rows == 3):
                leds[led + rows*60] = (255,228,225)
            if ( led > 12 and led < 16 and rows == 5) or ( rows == 4 and led == 14):
                leds[led + rows*60] = (0,0,255)
           #if
           #leds[led + rows*60] = (0,70,255)
        
    
        led = led + 1
    return leds

def Tube():
    led = 0

    while led < 60:
        for rows in range(6):
            if ( led > 30 and led < 35 and rows == 3) or ( rows == 4 and ( led == 32 or led == 33) ) or ( rows == 5 and ( led == 32 or led == 33 ) ):
                leds[led + rows*60] = (50,205,50)
            if (led == 34 and (rows == 4 or rows == 5)) or (rows == 3 and led == 35):
                leds[led + rows*60] = (34,139,34)
        led = led + 1
        return leds

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)

led = 0
while led < 60: #scroll all rows at the same time
    for rows in range(6):
        leds[led + rows*60] = (110,255,255)


    led = led + 1
    client.put_pixels(leds)

    leds = Mario()
    client.put_pixels(leds)
    time.sleep(.1)



time.sleep(.1)
client.put_pixels(leds)
time.sleep(.1)

#leds=moveRight(leds)
#client.put_pixels(leds)
