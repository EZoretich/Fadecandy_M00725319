import opc
import time
import numpy
import math
import tkinter as tk

'''window = tk.Tk()
window.title('M00725319 Animations')

text = tk.Label(text = "Hello! What's your favorite color?", foreground = 'black',
                width = 30, height = 3)
entry = tk.Entry(width = 10)


button_g = tk.Button(text = 'Green', foreground = 'black', background = 'green', width = 20, height = 3)
button_b = tk.Button(text = 'Blue', foreground = 'black', background = 'blue', width = 20, height = 3)
button_r = tk.Button(text = 'Red', foreground = 'black', background = 'red', width = 20, height = 3)

entry.grid(column = 1, row = 0, padx = 5, pady = 5)
button_g.grid(column = 0, row = 1, padx = 5, pady = 5)
button_b.grid(column = 1, row = 1, padx = 5, pady = 5)
button_r.grid(column = 2, row = 1, padx = 5, pady = 5)

entry.pack()
button_g.pack()
button_b.pack()
button_r.pack()'''

leds = [(255,255,255)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

window = tk.Tk()
window.title('OPC TKInter Demo')

def anim1():
    led = 0
    while led < 60:
        for rows in range(3):
            leds[led + rows*60] = (0, 255, 0)
        for rows in range (3,6):
            leds[59-led + rows*60] = (0, 0, 255)
        client.put_pixels(leds)
        time.sleep(0.1)
        led = led + 1

def placeholder1():
    pass
def placeholder2():
    pass

window.rowconfigure(0, minsize = 20, weight = 1)
window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, minsize = 20, weight = 1)

label = tk.Label(text = "Choose an animation: ")
label.grid(row = 0, column = 0)

anim1_button = tk.Button(window, text = "Anim 1", command = anim1)
anim2_button = tk.Button(window, text = "Anim 2", command = placeholder1)
anim3_button = tk.Button(window, text = "Anim 3", command = placeholder2)
exit_button = tk.Button(window, text = "Exit", command = window.destroy)

anim1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
anim2_button.grid(column = 1, row = 1, padx = 5, pady = 5)
anim3_button.grid(column = 2, row = 1, padx = 5, pady = 5)
exit_button.grid(column = 2, row = 2, padx = 5, pady = 5)
