#Choose Favourite Color

# v.1 = Implementing input and whole wall of uniform color
# v.2 = All color selection added
# v.3 = Implementing fading effect, The fading is uniform and syncronized

# --> Add rolling fading
# --> Implement more animation Pattern
# --> Fix R G B values = Color must fade but not be too similar to each other.


import opc
import time
import colorsys

led_wall = [(0, 0, 0)]*360
fading = 10
client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

choice = input(''' Hello!
        What's your favourite colour?
        1) Green  \t 5) Red
        2) Purple \t 6) Yellow
        3) Blue   \t 7) Orange
        4) Grey   \t 8) Pink \n Choose a number: ''')

while True:
    if choice.isdigit() == True: #if the input is a number:
        choice = int(choice)
        if choice <= 0 or choice > 8: #if the number is not between 1 and 8:
            choice = input("Please select a number from the list! \n What's your choice? ")
            continue
        else:
            break

    else:
        choice = input("Not a number! Please insert the number corresponding to you favourite color: ")

if choice == 1: # GREEN
    led_wall = [(0, 255, 0)]*360 # list with all green led
    time.sleep(.1)
    client.put_pixels(led_wall)
    #Start fading sequence
    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            
            g = g + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if g >= 255 or g<= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)

if choice == 2: # PURPLE
    led_wall = [(127, 0 , 255)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)
    
    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading
            b = b + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
        
if choice == 3: # BLUE
    led_wall = [(0, 0, 255)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            b = b + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if b >= 255 or b <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
if choice == 4: # GREY
    led_wall = [(150, 150, 150)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading
            b = b + fading
            g = g + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
if choice == 5: # RED
    led_wall = [(255, 0, 0)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
if choice == 6: # YELLOW
    led_wall = [(255, 255, 0)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading
            g = g + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
if choice == 7: # ORANGE
    led_wall = [(255, 128, 0)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading
            g = g + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
if choice == 8: # PINK
    led_wall = [(255, 102, 178)]*360
    time.sleep(.1)
    client.put_pixels(led_wall)

    led = 0
    while True:
        for led in enumerate(led_wall):
            r,g,b = led [1]
            r = r + fading
            g = g + fading
            b = b + fading

            fade_color = (r,g,b)
            led_wall[led[0]] = fade_color

            if r >= 255 or r <= 0:
                fading = -fading
        time.sleep(.1)
        client.put_pixels(led_wall)
    
