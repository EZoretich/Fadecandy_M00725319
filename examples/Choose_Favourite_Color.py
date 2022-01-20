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
import numpy
import math #to recreate rolling effect (like a wave --> sine)

led_wall = [(0, 0, 0)]*360
#fading = 10
client = opc.Client('localhost:7890')
client.put_pixels(led_wall)
client.put_pixels(led_wall)

s = 1.0
v = 1.0

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

if choice == 1: #GREEN
    for i in range(60):
        rgb = (0, 255 * abs(math.sin(i/54) - 0.5), 0) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 2: # PURPLE
    for i in range(60):
        rgb = (127 * abs(math.sin(i/54) - 0.5), 0, 255 * abs(math.sin(i/54) - 0.5)) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)
        
if choice == 3: # BLUE
    for i in range(60):
        rgb = (0, 0, 255 * abs(math.sin(i/54) - 0.5)) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 4: # GREY
    for i in range(60):
        rgb = (150 * abs(math.sin(i/54) - 0.5), 150 * abs(math.sin(i/54) - 0.5), 150 * abs(math.sin(i/54) - 0.5)) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 5: # RED
    for i in range(60):
        rgb = (255 * abs(math.sin(i/54) - 0.5), 0, 0) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 6: # YELLOW
    for i in range(60):
        rgb = (255 * abs(math.sin(i/54) - 0.5), 255 * abs(math.sin(i/54) - 0.5), 0) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 7: # ORANGE
    for i in range(60):
        rgb = (255 * abs(math.sin(i/54) - 0.5), 128 * abs(math.sin(i/54) - 0.5), 0) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)

if choice == 8: # PINK
    for i in range(60):
        rgb = (255 * abs(math.sin(i/54) - 0.5), 102 * abs(math.sin(i/54) - 0.5), 178 * abs(math.sin(i/54) - 0.5)) #math.sin returns sine of a number()
        for x in range(6):
            led_wall[i + x*60] = rgb

    while True:
        led_wall = numpy.roll(led_wall, 3)
        client.put_pixels(led_wall)
        time.sleep(0.01)
