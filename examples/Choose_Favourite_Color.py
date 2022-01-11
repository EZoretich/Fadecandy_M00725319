#Choose Favourite Color


import opc
import time
import colorsys

led_wall = [(0,0,0)]*360
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

if choice == 1:
    for led in range(360):
        led_wall[led] = (0,255,0)
        time.sleep(0.1)
        client.put_pixels(led_wall)
        client.put_pixels(led_wall)
