import opc
import time
import random

def  marioDude():     
    led = 0

    while led<60:
        for rows in range(6):
        #red              head                             jumper
            if ( led > 10 and led < 14 and rows == 2) or ( rows == 4 and led == 12):
                leds[led + rows*60] = (255,0,0)
            if ( led > 10 and led < 15 and rows == 3):
                leds[led + rows*60] = (255,228,225)
            if ( led > 10 and led < 14 and rows == 5) or ( rows == 4 and (led == 11 or led == 13)  ) :
                leds[led + rows*60] = (0,0,255)
           #if
           #leds[led + rows*60] = (0,70,255)
        
    
        led = led + 1
    return leds






leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)

led = 0
while led<60: #scroll all rows at the same time
    for rows in range(6):
        leds[led + rows*60] = (110,255,255)


    led = led + 1
    client.put_pixels(leds)
    
    leds=marioDude()
    client.put_pixels(leds)
    time.sleep(.1)



time.sleep(.1)
client.put_pixels(leds)
time.sleep(.1)

#leds=moveRight(leds)
#client.put_pixels(leds)
