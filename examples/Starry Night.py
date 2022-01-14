# Starry night
# Blue background, Moon (Bicolor) and Blinking starts

import opc
import time
import colorsys
import random

led_wall = [(0,0,255)]*360 #LED wall will display only blue
random_stars = [(0,0,255)]*360
client = opc.Client('localhost:7890')

fade = 10


def Stars(random_stars):
    for stars in range(50):
        rows = random.randrange(0,5)
        led = random.randrange(0,59)
        #print(f'random star will be at y %s and x %s', y, x)
        #random_stars.append((y,x))
        random_stars[led + rows*60] = (255,255,255)
    return random_stars
        
#print(random_stars)

time.sleep(0.1)

time.sleep(0.1)
client.put_pixels(Stars(led_wall))
random_stars=(Stars(led_wall))
z=255
while True:
    
    for led in enumerate(random_stars):
        r,g,b = led[1]
        r = r + fade
        g = g + fade
        b = b + fade

        fade_star = (r,g,b)
        #print("led 0")
        print(random_stars[led[0]])
        #random_stars[led] = fade_star[0]
        
        time.sleep(.5)
        if random_stars[led[0]] == z and random_stars[led[1]] == z and random_stars[led[2]] == z :
            z=z+fade
            fade = -fade
            random_stars[led[0]] = fade_star
            print(hit)
            
    time.sleep(0.1)
    #client.put_pixels(Stars(random_stars))
