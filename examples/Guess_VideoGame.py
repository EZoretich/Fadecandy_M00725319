import opc
import time
import random
# -------------------------------------------------------- SUPER MARIO DISPLAY
# --------------- Mario Function
def  Mario():     
    led = 0

    while led < 60:
        for rows in range(6):
                    # Red LEDs (Hat and T-shirt)
            if (( led > 12 and led < 16 and rows == 2) or
                ( rows == 4 and (led == 13 or led == 15))) :
                led_wall[led + rows*60] = (255,0,0)
                    # Pink LEDs (Skin)
            if ( led > 12 and led < 17 and rows == 3):
                led_wall[led + rows*60] = (255,228,225)
                    # Blue LEDs (Overall)
            if (( led > 12 and led < 16 and rows == 5) or
                ( rows == 4 and led == 14)):
                led_wall[led + rows*60] = (0,0,255)
                
        led = led + 1
    return led_wall

# --------------- Tube Function
def Tube():
    led = 0

    while led < 60:
        for rows in range(6):
                    # Light Green (Tube)
            if (( led > 30 and led < 35 and rows == 3) or
                ( rows == 4 and ( led == 32 or led == 33) ) or
                ( rows == 5 and ( led == 32 or led == 33 ))):
                led_wall[led + rows*60] = (50,205,50)
                    # Dak Green (Tube's Shade)
            if ((led == 34 and (rows == 4 or rows == 5)) or
                (rows == 3 and led == 35)):
                led_wall[led + rows*60] = (34,139,34)
        led = led + 1
    return led_wall

# --------------- Koopa Troopa Function
def Koopa():
    led = 0
    while led < 60:
        for rows in range(6):
                    # Yellow LEDs (Turtle's Skin)
            if (( led > 46 and led < 49 and (rows == 3 or rows == 4)) or
                (rows == 5 and (led == 49 or led == 51))):
                 led_wall[led + rows*60] = (255,255,0)
                    # Green LEDs (Shell)
            if ((led == 50 and rows == 3) or
            (led > 48 and led < 52 and rows == 4)):
                 led_wall[led + rows*60] = (0,255,0)
        led = led + 1
    return led_wall

# --------------- Super Mushroom Function
def Mushroom():
    led = 0
    while led < 60:
        for rows in range(6):
                    # Red LEDs (Mushroom's Cap)
            if ((led == 23 and rows == 3) or
                (rows == 4 and (led >= 24 and led < 26 or led == 22))):
                led_wall[led + rows*60] = (255,0,0)
                    # Peach LEDs (Mushroom's Stem)
            if (led > 22 and led < 25 and rows == 5):
                led_wall[led + rows*60] = (229,205,109)
                    # White LEDs (Mushroom's spots)
            if ((led == 24 and rows == 3) or
                (led == 23 and rows == 4)):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL SUPER MARIO FUNCTION

def Super_Mario():
    client.put_pixels(Mario())
    client.put_pixels(Tube())
    client.put_pixels(Koopa())
    client.put_pixels(Mushroom())
    
# --------------------------------------------------- PACMAN DISPLAY
# --------------- Mr Pacman Function
def Mr_Pacman():
    led = 0
    while led < 60:
        for rows in range(6):
            if (( led > 20 and led < 24 and rows == 0) or
                (led > 17 and led < 27 and rows == 1) or
                (led > 16 and led < 28 and rows == 2) or
                (led > 16 and led < 24 and rows == 3) or
                (led > 17 and led < 27 and rows == 4) or
                (led > 20 and led < 24 and rows == 5)): 
                led_wall[led + rows*60] = (255,255,0)
            if ((led == 30 or led == 33 or led == 36) and rows == 3):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall

# --------------- Blue Ghost Function
def Blue_Ghost():
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > 4 and led < 8 and rows == 1) or
                (led > 2 and led < 10 and (rows == 3 or rows == 4)) or
                ((led > 2 and led < 10) and rows == 2) or
                (led == 3 or led == 5 or led == 7 or led == 9) and rows == 5):
                 led_wall[led + rows*60] = (51,153,255)
            if ((led == 5 or led == 8) and rows == 2):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall
                
# --------------- Purple Ghost Function
def Purple_Ghost():
    led = 0
    while led < 60:
        for rows in range(6):
            if ((led > 52  and led < 56 and rows == 1) or
                (led > 50 and led < 58 and (rows == 3 or rows == 4)) or
                ((led > 50 and led < 58 ) and rows == 2) or
                (led == 51 or led == 53 or led == 55 or led == 57) and rows == 5):
                 led_wall[led + rows*60] = (121,54,189)
            if ((led == 52 or led == 55) and rows == 2):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall

# --------------- Cherry Function
def Cherry():
    led = 0
    while led < 60:
        for rows in range(6):
            if (((led > 39 and led < 44) and rows == 3) or
                ((led == 41 or led == 42) and (rows == 2 or rows == 4))):
                led_wall[led + rows*60] = (255,0,0)
            if ((led == 43 and rows == 0) or
                (led == 42 and rows == 1)):
                led_wall[led + rows*60] = (0,255,0)
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL PACMAN FUNCTION
def Pacman():
    client.put_pixels(Mr_Pacman())
    client.put_pixels(Blue_Ghost())
    client.put_pixels(Purple_Ghost())
    client.put_pixels(Cherry())

# -------------------------------------------------------- POKEMON DISPLAY
# --------------- PokeBall Function
def Pokeball():
    


#------------------------------------------------------------------------------------------
led_wall = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)

#Pacman()
#Super_Mario()
time.sleep(.1)
