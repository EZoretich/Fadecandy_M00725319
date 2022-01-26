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
                        # Yellow LEDs (Pacman's Body)
            if (( led > 20 and led < 24 and rows == 0) or
                (led > 17 and led < 27 and rows == 1) or
                (led > 16 and led < 28 and rows == 2) or
                (led > 16 and led < 24 and rows == 3) or
                (led > 17 and led < 27 and rows == 4) or
                (led > 20 and led < 24 and rows == 5)): 
                led_wall[led + rows*60] = (255,255,0)
                        # White LEDs (Dots)
            if ((led == 30 or led == 33 or led == 36) and rows == 3):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall

# --------------- Blue Ghost Function
def Blue_Ghost():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Blue LEDs (Ghost's Body)
            if ((led > 4 and led < 8 and rows == 1) or
                (led > 2 and led < 10 and (rows == 3 or rows == 4)) or
                ((led > 2 and led < 10) and rows == 2) or
                (led == 3 or led == 5 or led == 7 or led == 9) and rows == 5):
                 led_wall[led + rows*60] = (51,153,255)
                         # White LEDs (Ghost's Eyes)
            if ((led == 5 or led == 8) and rows == 2):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall
                
# --------------- Purple Ghost Function
def Purple_Ghost():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Purple LEDs (Ghost's Body)
            if ((led > 52  and led < 56 and rows == 1) or
                (led > 50 and led < 58 and (rows == 3 or rows == 4)) or
                ((led > 50 and led < 58 ) and rows == 2) or
                (led == 51 or led == 53 or led == 55 or led == 57) and rows == 5):
                 led_wall[led + rows*60] = (121,54,189)
                         # White LEDs (Ghost's Eyes)
            if ((led == 52 or led == 55) and rows == 2):
                led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    return led_wall

# --------------- Cherry Function
def Cherry():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Red LEDs (Cherry)
            if (((led > 39 and led < 44) and rows == 3) or
                ((led == 41 or led == 42) and (rows == 2 or rows == 4))):
                led_wall[led + rows*60] = (255,0,0)
                        # Green LEDs (Cherry's Stem)
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
    led = 0
    while led < 60:
        for rows in range(6):
                        # Red LEDs (Pokeball TOP)
            if (((led > 9 and led < 17) and rows == 1) or
                ((led > 8 and led < 18) and rows == 2)):
                led_wall[led + rows*60] = (255,0,0)
                        # White LEDs (Pokeball BOTTOM)
            if (((led > 9 and led < 17) and rows == 5) or
                ((led > 8 and led < 18) and rows == 4) or
                (led == 13 and rows == 3)):
                led_wall[led + rows*60] = (255,255,255)
                        # Dark Gray (Pokeball's line)
            if ((( led > 11 and led < 15) and (rows == 2 or rows == 4)) or
                 ((led > 8 and led < 13 or led > 13 and led < 18) and rows == 3)):
                led_wall[led + rows*60] = (64,64,64)
        led = led + 1
    return led_wall

# --------------- Pikachu Function
def Pikachu():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Yellow (Pikachu's Body)
            if (((led > 23 and led < 31) and
                 (rows == 2 or rows == 3 or rows == 4 or rows == 5)) or
                ((led == 25 or led == 29) and rows == 1)):
                led_wall[led + rows*60] = (255,255,0)
            if (led == 31 and rows == 4):
                led_wall[led + rows*60] = (204,153,51)
            if (led == 32 and rows == 3):
                led_wall[led + rows*60] = (85,58,4)
            if ((led == 24 or led == 30) and rows == 3):
                led_wall[led + rows*60] = (255,0,0)
        led = led + 1
    return led_wall

# --------------- Charmander Function
def Charmander():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Orange LEDs (Charmander's Body)
            if (((led > 39 and led < 44) and (rows == 0 or rows == 3)) or
                ((led > 38 and led < 45) and (rows == 1 or rows == 2)) or
                ((led  > 38 and led < 45) and rows == 4) or
                ((led > 43 and led < 46 or led == 39) and rows == 5) or
                (led == 46 and rows == 4)):
                led_wall[led + rows*60] = (255,128,0)
                        # Yellow LEDs (Charmander's Belly & Flame)
            if (((led > 40 and led < 43) and rows == 4) or
                ((led > 39 and led < 44) and rows == 5) or
                (led == 47 and rows == 3)):
                led_wall[led + rows*60] = (255,255,0)
                        # Red LEDs (Charmander's Flame)
            if (((led > 46 and led < 49) and rows == 2) or
                (led == 48 and rows == 3)):
                led_wall[led + rows*60] = (255,0,0)
        led = led + 1
    return led_wall

#---------------------------------------------------- FULL POKEMON FUNCTION
def Pokemon():
    client.put_pixels(Charmander())
    client.put_pixels(Pokeball())
    client.put_pixels(Pikachu())

# -------------------------------------------------------- SNAKE DISPLAY
def Snake():
    led = 0
    while led < 60:
        for rows in range(6):
                        # White LEDs (Snake's Body)
            if (((led > 19 and led < 27) and rows == 1) or
                (led == 26 and (rows == 2 or rows == 3)) or
                ((led > 25 and led < 40) and rows == 4)):
                led_wall[led + rows*60] = (255,255,255)
                        # Red LED (Dot)
            if (led == 43 and rows == 4):
                led_wall[led + rows*60] = (255,0,0)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)

# -------------------------------------------------------- TETRIS DISPLAY
def Tetris():
    led = 0
    while led < 60:
        for rows in range(6):
                        # Yellow LEDs (T)
            if (((led > 13 and led < 23) and (rows == 4 or rows == 5)) or
                ((led > 16 and led < 20) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (255,255,0)
                        #Red LEDs (Z)
            if (((led > 19 and led < 26) and (rows == 2 or rows == 3)) or
                ((led > 22 and led < 29) and (rows == 4 or rows == 5))):
                led_wall[led + rows*60] = (255,0,0)
                        #Purple LEDs (I)
            if (((led > 28 and led < 33) and
                 (rows > 0 and rows <= 5))):
                led_wall[led + rows*60] = (148,0,211)
                        #Green LEDs (L)
            if (((led > 34 and led < 43) and (rows == 4 or rows == 5)) or
                ((led > 39 and led < 43) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (0,255,0)
                        # Blue LEDs (O)
            if (((led > 44 and led < 49) and (rows > 2 and rows <= 5))):
                led_wall[led + rows*60] = (51,153,255)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)

# -------------------------------------------------------- 3, 2, 1, GO! DISPLAY
# --------------- 3 Function
def Three():
    led = 0
    while led < 60:
        for rows in range(6):
            if (((led > 28 and led < 33) and (rows == 0 or rows == 5)) or
                ((led == 28 or led == 33) and (rows == 1 or rows == 4)) or
                ((led > 30 and led < 34) and (rows == 2 or rows == 3))):
                led_wall[led + rows*60] = (255,255,255)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)

# --------------- 2 Function
def Two():
    led = 0
    while led < 60:
        for rows in range(6):
            if (((led > 28 and led < 33) and (rows == 0 or rows == 5)) or
                ((led == 28 or led == 33) and (rows == 1 or rows == 5)) or
                (led == 30 and rows == 4) or
                (led == 31 and rows == 3) or
                (led == 32 and rows == 2)):
                led_wall[led + rows*60] = (255,255,255)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)
# --------------- 1 Function
def One():
    led = 0
    while led < 60:
        for rows in range (6):
            if (((led > 27 and led < 33) and rows == 5) or
                (led == 28 and rows == 1) or
                (led == 29 and rows == 0) or
                (led == 30 and (rows >= 0 and rows < 5))):
                led_wall[led + rows*60] = (255,255,255)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)
# --------------- GO! Function
def Go():
    led = 0
    while led < 60:
        for rows in range(6):
            if (((led > 24 and led < 29 or led > 32 and led < 37) and
                 (rows == 0 or rows == 5)) or
                ((led == 24 or led == 32 or led == 37) and (rows > 0 and rows < 5)) or
                (led == 40 and (rows >= 0 and rows < 4 or rows == 5)) or
                ((led > 27 and led < 30) and rows == 3) or
                ( led == 29 and rows == 4)):
                led_wall[led + rows*60] = (255,255,255)
        client.put_pixels(led_wall)
        led = led + 1
    return client.put_pixels(led_wall)

# -------------------------------------------------------- WRONG ANSWER DISPLAY
def Wrong():
    led = 0
    while led<30: 
        for rows in range(6):
            led_wall[led + rows*60] = (255,0,0)
            led_wall[59-led + rows*60] = (255,0,0)
        client.put_pixels(led_wall)
        time.sleep(0.1)
        led = led + 1

    for rows in range(6):
        led_wall[led + rows*60] = (255,255,255)
        led = led + 1
    client.put_pixels(led_wall)
    for rows in range(6):
        led_wall[led-1 + rows*60] = (255,255,255)
        led = led - 1
    client.put_pixels(led_wall)

    return client.put_pixels(led_wall)
        
# -------------------------------------------------------- RIGHT ANSWER DISPLAY
def Right():
    led = 0
    while led < 30:
        for rows in range(6):
            led_wall[led + rows*60] = (0,255,0)
            led_wall[59-led + rows*60] = (0,255,0)
        client.put_pixels(led_wall)
        time.sleep(0.1)
        led = led + 1

    for rows in range(6):
        led_wall[led+4 + rows*60] = (255,255,255)
        led = led - 1
    client.put_pixels(led_wall)
    for rows in range(3,6):
        led_wall[led+2 + rows*60] = (255,255,255)
        led = led + 1
    client.put_pixels(led_wall)

    return client.put_pixels(led_wall)
            
# -------------------------------------------------------- LOSER DISPLAY
def Lose():
    #led_wall = [(255,255,255)]*360
    fade = 10
    while True:
        for led in enumerate(led_wall):
  
            r,g,b = led[1]
            r = r+fade
            g = g+fade
            b = b+fade

            fading = (r,g,b)
            led_wall[led[0]] = fading

            if r >= 255 or r <= 0:
                fade = -fade

        client.put_pixels(led_wall)
        time.sleep(0.1)

    return client.put_pixels(led_wall)
# -------------------------------------------------------- WINNER DISPLAY
#------------------------------------------------------------------------------------------
led_wall = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(led_wall)

#Pacman()
#Super_Mario()
#Pokemon()
#Snake()
#Tetris()
#Three()
#Two()
#One()
#Go()
#Wrong()
#Right()
Lose()

time.sleep(.1)
