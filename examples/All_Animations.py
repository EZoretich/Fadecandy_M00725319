#Import all libraries
import opc
import time
import colorsys
import numpy
import math

led_wall = [(0,0,0)]*360 #List of tuples (RGB values)

client = opc.Client('localhost:7890')#Connect to led wall

client.put_pixels(led_wall) #Place led on display
client.put_pixels(led_wall)

s = 1.0
v = 1.0

print('''\t Hi! Welcome to my video presentation! \n\t Which animation would you like to see?")
      \t\t\t ___________________________________________________
      \t\t\t|                        \t                    |
      \t\t\t|                        \t                    |
      \t\t\t|    1) Favorite Color   \t 4) Animation 4     |
      \t\t\t|                        \t                    |
      \t\t\t|    2) Christmas Lights \t 5) Animation 5     |
      \t\t\t|                        \t                    |
      \t\t\t|    3) Starry Night     \t 6) Animation 6     |
      \t\t\t|                        \t                    |
      \t\t\t|___________________________________________________|''')

choice = input("\n\t Please select a number from above: ") # user input

while True: #While running
    if choice.isdigit() == True: # If the input is a number
        choice = int(choice)
        if choice <= 0 or choice > 6: #if number selected smaller or bigger than the ones available:
            choice = input("This number in not displayed! Please select a whole number from the list: ")
            continue # Continue and ask for correct input
        else: #Otherwise
            break #Interrupt the loop
    else: # If the input is not a number:
        choice = input("Not a number! Please Select a whole number: ")
        #ask for correct input
if choice == 1: # if input is 1: Play first anymation
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
