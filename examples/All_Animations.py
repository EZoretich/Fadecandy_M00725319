#----------------------IMPORTING LIBRARIES
import opc
import time
import colorsys
import numpy
import math
#--------------------- DEFINING FUNCTIONS
# -------------------------------------------------------- CLEAR SCREEN
def Clear():
    for led in range(360): # for all leds
        led_wall[led] = (0,0,0) #make them black
        led = led + 1
# -------------------------------------------------------- SUPER MARIO DISPLAY
# --------------- Mario Function
def  Mario():     
    led = 0

    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                    # Red LEDs (Hat and T-shirt)
            if (( led > 12 and led < 16 and rows == 2) or
                ( rows == 4 and (led == 13 or led == 15))) :
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
                    # Pink LEDs (Skin)
            if ( led > 12 and led < 17 and rows == 3):
                led_wall[led + rows*60] = (255,228,225) #Give RGB value to those leds
                    # Blue LEDs (Overall)
            if (( led > 12 and led < 16 and rows == 5) or
                ( rows == 4 and led == 14)):
                led_wall[led + rows*60] = (0,0,255) #Give RGB value to those leds
                
        led = led + 1
    return led_wall # Return led display with updated led colors

# --------------- Tube Function
def Tube():
    led = 0

    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                    # Light Green (Tube)
            if (( led > 30 and led < 35 and rows == 3) or
                ( rows == 4 and ( led == 32 or led == 33) ) or
                ( rows == 5 and ( led == 32 or led == 33 ))):
                led_wall[led + rows*60] = (50,205,50) #Give RGB value to those leds
                    # Dak Green (Tube's Shade)
            if ((led == 34 and (rows == 4 or rows == 5)) or
                (rows == 3 and led == 35)):
                led_wall[led + rows*60] = (34,139,34) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Koopa Troopa Function
def Koopa():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                    # Yellow LEDs (Turtle's Skin)
            if (( led > 46 and led < 49 and (rows == 3 or rows == 4)) or
                (rows == 5 and (led == 49 or led == 51))):
                 led_wall[led + rows*60] = (255,255,0) #Give RGB value to those leds
                    # Green LEDs (Shell)
            if ((led == 50 and rows == 3) or
            (led > 48 and led < 52 and rows == 4)):
                 led_wall[led + rows*60] = (0,255,0) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Super Mushroom Function
def Mushroom():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                    # Red LEDs (Mushroom's Cap)
            if ((led == 23 and rows == 3) or
                (rows == 4 and (led >= 24 and led < 26 or led == 22))):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
                    # Peach LEDs (Mushroom's Stem)
            if (led > 22 and led < 25 and rows == 5):
                led_wall[led + rows*60] = (229,205,109) #Give RGB value to those leds
                    # White LEDs (Mushroom's spots)
            if ((led == 24 and rows == 3) or
                (led == 23 and rows == 4)):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL SUPER MARIO FUNCTION

def Super_Mario():
    client.put_pixels(Mario()) #Place latest frame on led screen (From Mario)
    client.put_pixels(Tube()) #Place latest frame on led screen (From Tube)
    client.put_pixels(Koopa()) #Place latest frame on led screen (From Koopa)
    client.put_pixels(Mushroom()) #Place latest frame on led screen (From Mushroom)
    
# --------------------------------------------------- PACMAN DISPLAY
# --------------- Mr Pacman Function
def Mr_Pacman():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Yellow LEDs (Pacman's Body)
            if (( led > 20 and led < 24 and rows == 0) or
                (led > 17 and led < 27 and rows == 1) or
                (led > 16 and led < 28 and rows == 2) or
                (led > 16 and led < 24 and rows == 3) or
                (led > 17 and led < 27 and rows == 4) or
                (led > 20 and led < 24 and rows == 5)): 
                led_wall[led + rows*60] = (255,255,0) #Give RGB value to those leds
                        # White LEDs (Dots)
            if ((led == 30 or led == 33 or led == 36) and rows == 3):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Blue Ghost Function
def Blue_Ghost():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Blue LEDs (Ghost's Body)
            if ((led > 4 and led < 8 and rows == 1) or
                (led > 2 and led < 10 and (rows == 3 or rows == 4)) or
                ((led > 2 and led < 10) and rows == 2) or
                (led == 3 or led == 5 or led == 7 or led == 9) and rows == 5):
                 led_wall[led + rows*60] = (51,153,255) #Give RGB value to those leds
                         # White LEDs (Ghost's Eyes)
            if ((led == 5 or led == 8) and rows == 2):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    return led_wall
                
# --------------- Purple Ghost Function
def Purple_Ghost():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Purple LEDs (Ghost's Body)
            if ((led > 52  and led < 56 and rows == 1) or
                (led > 50 and led < 58 and (rows == 3 or rows == 4)) or
                ((led > 50 and led < 58 ) and rows == 2) or
                (led == 51 or led == 53 or led == 55 or led == 57) and rows == 5):
                 led_wall[led + rows*60] = (121,54,189) #Give RGB value to those leds
                         # White LEDs (Ghost's Eyes)
            if ((led == 52 or led == 55) and rows == 2):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Cherry Function
def Cherry():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Red LEDs (Cherry)
            if (((led > 39 and led < 44) and rows == 3) or
                ((led == 41 or led == 42) and (rows == 2 or rows == 4))):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
                        # Green LEDs (Cherry's Stem)
            if ((led == 43 and rows == 0) or
                (led == 42 and rows == 1)):
                led_wall[led + rows*60] = (0,255,0) #Give RGB value to those leds
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL PACMAN FUNCTION
def Pacman():
    client.put_pixels(Mr_Pacman()) #Place latest frame on led screen (From Mr_Pacman)
    client.put_pixels(Blue_Ghost()) #Place latest frame on led screen (From Blue_Ghost)
    client.put_pixels(Purple_Ghost()) #Place latest frame on led screen (From Purple_Ghost)
    client.put_pixels(Cherry()) #Place latest frame on led screen (From Cherry)

# -------------------------------------------------------- POKEMON DISPLAY
# --------------- PokeBall Function
def Pokeball():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Red LEDs (Pokeball TOP)
            if (((led > 9 and led < 17) and rows == 1) or
                ((led > 8 and led < 18) and rows == 2)):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
                        # White LEDs (Pokeball BOTTOM)
            if (((led > 9 and led < 17) and rows == 5) or
                ((led > 8 and led < 18) and rows == 4) or
                (led == 13 and rows == 3)):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
                        # Dark Gray (Pokeball's line)
            if ((( led > 11 and led < 15) and (rows == 2 or rows == 4)) or
                 ((led > 8 and led < 13 or led > 13 and led < 18) and rows == 3)):
                led_wall[led + rows*60] = (64,64,64) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Pikachu Function
def Pikachu():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Yellow (Pikachu's Body)
            if (((led > 23 and led < 31) and
                 (rows == 2 or rows == 3 or rows == 4 or rows == 5)) or
                ((led == 25 or led == 29) and rows == 1)):
                led_wall[led + rows*60] = (255,255,0) #Give RGB value to those leds
            if (led == 31 and rows == 4):
                led_wall[led + rows*60] = (204,153,51) #Give RGB value to those leds
            if (led == 32 and rows == 3):
                led_wall[led + rows*60] = (85,58,4) #Give RGB value to those leds
            if ((led == 24 or led == 30) and rows == 3):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
        led = led + 1
    return led_wall

# --------------- Charmander Function
def Charmander():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Orange LEDs (Charmander's Body)
            if (((led > 39 and led < 44) and (rows == 0 or rows == 3)) or
                ((led > 38 and led < 45) and (rows == 1 or rows == 2)) or
                ((led  > 38 and led < 45) and rows == 4) or
                ((led > 43 and led < 46 or led == 39) and rows == 5) or
                (led == 46 and rows == 4)):
                led_wall[led + rows*60] = (255,128,0) #Give RGB value to those leds
                        # Yellow LEDs (Charmander's Belly & Flame)
            if (((led > 40 and led < 43) and rows == 4) or
                ((led > 39 and led < 44) and rows == 5) or
                (led == 47 and rows == 3)):
                led_wall[led + rows*60] = (255,255,0) #Give RGB value to those leds
                        # Red LEDs (Charmander's Flame)
            if (((led > 46 and led < 49) and rows == 2) or
                (led == 48 and rows == 3)):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL POKEMON FUNCTION
def Pokemon():
    client.put_pixels(Charmander()) #Place latest frame on led screen (From Charmander)
    client.put_pixels(Pokeball()) #Place latest frame on led screen (From Pokeball)
    client.put_pixels(Pikachu()) #Place latest frame on led screen (From Pikachu)

# -------------------------------------------------------- SNAKE DISPLAY
def Snake():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # White LEDs (Snake's Body)
            if (((led > 19 and led < 27) and rows == 1) or
                (led == 26 and (rows == 2 or rows == 3)) or
                ((led > 25 and led < 40) and rows == 4)):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
                        # Red LED (Dot)
            if (led == 43 and rows == 4):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen 
        led = led + 1

# -------------------------------------------------------- TETRIS DISPLAY
def Tetris():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
                        # Yellow LEDs (T)
            if (((led > 13 and led < 23) and (rows == 4 or rows == 5)) or
                ((led > 16 and led < 20) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (255,255,0) #Give RGB value to those leds
                        #Red LEDs (Z)
            if (((led > 19 and led < 26) and (rows == 2 or rows == 3)) or
                ((led > 22 and led < 29) and (rows == 4 or rows == 5))):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
                        #Purple LEDs (I)
            if (((led > 28 and led < 33) and
                 (rows > 0 and rows <= 5))):
                led_wall[led + rows*60] = (148,0,211) #Give RGB value to those leds
                        #Green LEDs (L)
            if (((led > 34 and led < 43) and (rows == 4 or rows == 5)) or
                ((led > 39 and led < 43) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (0,255,0) #Give RGB value to those leds
                        # Blue LEDs (O)
            if (((led > 44 and led < 49) and (rows > 2 and rows <= 5))):
                led_wall[led + rows*60] = (51,153,255) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen 
        led = led + 1

# -------------------------------------------------------- 3, 2, 1, GO! DISPLAY
# --------------- 3 Function
def Three():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
            if (((led > 28 and led < 33) and (rows == 0 or rows == 5)) or
                ((led == 28 or led == 33) and (rows == 1 or rows == 4)) or
                ((led > 30 and led < 34) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen
        led = led + 1

# --------------- 2 Function
def Two():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
            if (((led > 28 and led < 33) and (rows == 0 or rows == 5)) or
                ((led == 28 or led == 33) and (rows == 1 or rows == 5)) or
                (led == 30 and rows == 4) or
                (led == 31 and rows == 3) or
                (led == 32 and rows == 2)):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen 
        led = led + 1
# --------------- 1 Function
def One():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range (6): #Divide by 6 rows
            if (((led > 27 and led < 33) and rows == 5) or
                (led == 28 and rows == 1) or
                (led == 29 and rows == 0) or
                (led == 30 and (rows >= 0 and rows < 5))):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen 
        led = led + 1
# --------------- GO! Function
def Go():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6): #Divide by 6 rows
            if (((led > 24 and led < 29 or led > 32 and led < 37) and
                 (rows == 0 or rows == 5)) or
                ((led == 24 or led == 32 or led == 37) and (rows > 0 and rows < 5)) or
                (led == 40 and (rows >= 0 and rows < 4 or rows == 5)) or
                ((led > 27 and led < 30) and rows == 3) or
                ( led == 29 and rows == 4)):
                led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        client.put_pixels(led_wall) #Place latest frame on led screen 
        led = led + 1

# -------------------------------------------------------- COUNTDOWN FULL FUNCTION
def Countdown():
    Three()
    time.sleep(1)
    Clear()
    Two()
    time.sleep(1)
    Clear()
    One()
    time.sleep(1)
    Clear()
    Go()
    time.sleep(0.1)
    Clear()

# -------------------------------------------------------- WRONG ANSWER DISPLAY
def Wrong():
    led = 0
    while led<30: #Consider all rows at the same time, but only until the middle of display
        for rows in range(6): #Divide by 6 rows
            led_wall[led + rows*60] = (255,0,0)
            led_wall[59-led + rows*60] = (255,0,0)
        client.put_pixels(led_wall) #Place latest frame on led screen 
        time.sleep(0.1)
        led = led + 1

    for rows in range(6): # Will create a diagonal line, crossing all 6 rows, such as \
        led_wall[led + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    client.put_pixels(led_wall) #Place latest frame on led screen 
    for rows in range(6): # Will create a diagonal line, crossing all 6 rows, such as /
        led_wall[led-1 + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led - 1
    client.put_pixels(led_wall) #Place latest frame on led screen 
        
# -------------------------------------------------------- RIGHT ANSWER DISPLAY
def Right():
    led = 0
    while led < 30: #Consider all rows at the same time, but only until the middle of display
        for rows in range(6): #Divide by 6 rows
            led_wall[led + rows*60] = (0,255,0) #Give RGB value to leds from 0 to 30
            led_wall[59-led + rows*60] = (0,255,0)#Give RGB value leds from 60 to 30
        client.put_pixels(led_wall) #Place latest frame on led screen 
        time.sleep(0.1)
        led = led + 1

    for rows in range(6): # Will create a diagonal line, crossing all 6 rows, such as /
        led_wall[led+4 + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led - 1
    client.put_pixels(led_wall) #Place latest frame on led screen 
    for rows in range(3,6): # Will create a diagonal line, only across rows 3 to 5, such as \
        led_wall[led+2 + rows*60] = (255,255,255) #Give RGB value to those leds
        led = led + 1
    client.put_pixels(led_wall) #Place latest frame on led screen 

# --------------- Sad Function (For LOSER)
def Sad():
    led=  0
    while led < 60: #Consider all rows at the same time
        for rows in range(6):
            if (((led > 25 and led < 28 or led > 31 and led < 34) and
                 (rows == 0 or rows == 1)) or
                ((led > 24 and led < 34) and rows == 3) or
                ((led == 24 or led == 34) and rows == 4) or
                ((led == 23 or led == 35) and rows == 5)):
                led_wall[led + rows*60] = (255,0,0) #Give RGB value to those leds
        led = led + 1
    client.put_pixels(led_wall) #Place latest frame on led screen 

# --------------- Happy Function (For Winner)
def Happy():
    led = 0
    while led < 60: #Consider all rows at the same time
        for rows in range(6):
            if (((led > 25 and led < 28 or led > 31 and led < 34) and
                 (rows == 0 or rows == 1)) or
                ((led > 25 and led < 34) and rows == 5) or
                ((led == 25 or led == 34) and rows == 4) or
                ((led == 24 or led == 35) and rows == 3)):
                led_wall[led + rows*60] = (11,128,255) #Give RGB value to those leds
        led = led + 1
    client.put_pixels(led_wall)
            
# -------------------------------------------------------- LOSER DISPLAY (To fix)
def Lose():
    Sad()
    fade = 10
    while True:
        for leds in enumerate(led_wall): #Creates a list of tuples with index and contents of elements
  
            r,g,b = leds[1] # Points at second element in led - the (R,G,B) tuple
            g = g+fade
            b = b+fade

            fading = (r,g,b) # New tuple with fading updated values
            led_wall[leds[0]] = fading # Placed in original list at index
        if b >= 150 or b <= 0: # Checking if fade reached its limit
            fade = -fade # If it did, change direction
        Sad()
        client.put_pixels(led_wall) #Place latest frame on led screen 
        time.sleep(0.1) #delay
# -------------------------------------------------------- WINNER DISPLAY
def Win():
    Happy()
    fade = 10
    while True:
        for leds in enumerate(led_wall): #Creates a list of tuples with index and contents of elements
         
            r,g,b = leds[1] # Points at second element in led - the (R,G,B) tuple
            r = r+fade
            g = g+fade

            fading = (r,g,b) # New tuple with fading updated values
            led_wall[leds[0]] = fading # Placed in original list at index
        if r >= 255 or r <= 0: # Checking if fade reached its limit
            fade = -fade # If it did, change direction
               
        Happy()     
        time.sleep(0.1) #delay 
        client.put_pixels(led_wall) #Place latest frame on led screen

#------------------------------------------------------------------------------------------


led_wall = [(0,0,0)]*360 #List of tuples (RGB values)

client = opc.Client('localhost:7890')#Connect to led wall

client.put_pixels(led_wall) #Place led on display
client.put_pixels(led_wall)

s = 1.0
v = 1.0
score = 0

print('''\t Hi! Welcome to my video presentation! \n\t Which animation would you like to see?")
      \t\t\t ___________________________________________________
      \t\t\t|                        \t                    |
      \t\t\t|                        \t                    |
      \t\t\t|    1) Favorite Color   \t 4) Animation 4     |
      \t\t\t|                        \t                    |
      \t\t\t|    2) Guess the Game   \t 5) Animation 5     |
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
#---------------------------------------------------------------- ANIMATION 1: FAVORITE COLOR
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
#-------------------------------------------------- ANIMATION 2: GUESS THE GAME
if choice == 2:
    choice = input('''\t\t\t Welcome to GUESS THE GAME!
        You will see a series of recreated images on the LED display.
        Please identify the videogame and type in your answer.
        Be carefull, you will only get one chance!
        \n\t\t\t\t GOOD LUCK!
        \n\t Are You Ready to start? \t Please type 'Yes' or 'No'\n :''') #User input
while True: #Keep running
    if choice.isdigit() == False: # If the input is not a number:
        choice = str(choice)
        if choice == 'No' or choice == 'no': # If answer is no:
            choice = input("Whenever you are ready, please type 'Yes' \n :")
            continue #Stay in the loop
        if choice == 'Yes' or choice == 'yes': # If answer is yes:
            break # end the loop
        else: # If the input is something else
            choice = input("Please select 'Yes' or 'No'. \n :")
    else: # If the input si something else
        choice = input("Please type 'Yes' or 'No")



if choice == 'Yes' or choice == 'yes': # If yes, start animations
    while True:
        Countdown()
        time.sleep(1)
        Clear()
        #------------Guess First Animation (Pacman)
        Pacman() # Send pacman leds
        choice = input("Which game is this? ") # ask for input
        if choice == 'Pacman' or choice == 'pacman': # if answer is correct
            Right() # Play Right animation
            time.sleep(1)
            print("Correct!") # print "Correct"
            score = score + 1# add correct answer to the score
        else: # if answer is wrong
            Wrong() # play Wrong animation
            time.sleep(1)
            print("Oh no! That's wrong") # print "not correct"
        Clear() # clear the screen (all black)
        Countdown() # Start countdown before new animation
        time.sleep(1)
        #----------- Guess Second Animation (Pokemon)
        Pokemon()
        choice = input("Which game is this? ")
        if choice == 'Pokemon' or choice == 'pokemon':
            Right()
            time.sleep(1)
            print("Correct!")
            score = score + 1
        else:
            Wrong()
            time.sleep(1)
            print("Oh no! That's wrong")
        Clear()
        Countdown()
        time.sleep(1)
        #--------------- Guess Third Animation (Super Mario)
        Super_Mario()
        choice = input("Which game is this? ")
        if choice == 'Super Mario' or choice == 'super mario':
            Right()
            time.sleep(1)
            print("Correct!")
            score = score + 1
        else:
            Wrong()
            time.sleep(1)
            print("Oh no! That's wrong")
        Clear()
        Countdown()
        time.sleep(1)
        #--------------- Guess Fourth Animation (Tetris)
        Tetris()
        choice = input("Which game is this? ")
        if choice == 'Tetris' or choice == 'tetris':
            Right()
            time.sleep(1)
            print("Correct!")
            score = score + 1
        else:
            Wrong()
            time.sleep(1)
            print("Oh no! That's wrong")
        Clear()
        Countdown()
        time.sleep(1)
        #--------------- Guess Fifth Animation (Snake)
        Snake()
        choice = input("Which game is this? ")
        if choice == 'Snake' or choice == 'snake':
            Right()
            time.sleep(1)
            print("Correct!")
            score = score + 1
            
        else:
            Wrong()
            time.sleep(1)
            print("Oh no! That's wrong")
            
        if score > 2: # if the score is at least 3/5
            Clear() # clear screen
            print("Congrats! You won!") # print 'you won'
            Win() # play winning animation
            time.sleep(0.1)
        else: # if the score is below 3/5 (not possible to be over 5)
            Clear() # clear screen
            print(" Whoops! You lost! Better luck next time") # print ' you lost'
            Lose() # playing losign animation
            time.sleep(0.1)

