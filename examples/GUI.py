######## 1) First commands
import tkinter as tk

window = tk.Tk() # object that is root window
window.title('TKInter Demo')

text = tk.Label(text = "Hello! What's your name?", foreground = 'white',
                background = 'blue', width = 30, height = 3) #Sequence doesn't matter, as soon as you call them correctly
#text.pack() #Place text in the window

entry = tk.Entry(width = 30)
#entry.pack()

##name = entry.get()
##entry.delete(0, len(name))  --> Implemented into the following function
#entry.delete(0,7) #delete text input, (start from, end with [not included]
#tk.END has the same function as len(name).
#It deletes the whole name no matter the lenght

def save_and_print():
    name = entry.get()
    entry.delete(0, len(name))
    print(name)
    

button = tk.Button(text = 'Submit', width = 30, height = 5,
                   command = save_and_print)
button.pack(padx = 5, pady = 5)

#window.bind('<Return>', save_and_print) # same as follow: (but isn't working rn)
window.bind('<Return>', lambda event: save_and_print())

frame = tk.Frame(master = window)
label = tk.Label(master = frame, text = 'Frame')


frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)

text.grid(column = 0, row = 0, padx = 5, pady = 5)
entry.grid(column = 0, row = 1, padx = 5, pady = 5)
button.grid(column = 1, row = 0, padx = 5, pady = 5)
label.grid(column = 1, row = 1, padx = 5, pady = 5)

#print(text.configure().keys()) #Shows you all library possibilities
window.mainloop() # event loop --> how it starts

######## 2) Colors, background and fitting
'''import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(width = 100, height = 100, bg = 'green')
frame2 = tk.Frame(width = 20, height = 20, bg = 'red')
frame3 = tk.Frame(width = 50, height = 50, bg = 'blue')

frame1.pack(side = tk.LEFT, fill = tk.Y)
frame2.pack(side = tk.LEFT, fill = tk.X)
frame3.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

window.mainloop()'''

######## 3) More demo
'''import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight = 1, minsize = 75)
    window.rowconfigure(i, weight = 1, minsize = 75)

for row in range (3):
    for col in range(3):
        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
        frame.grid(row = row, column = col, padx = 5, pady = 5)
        label = tk.Label(master = frame, text = f"{row}, {col}")
        label.pack() #Label is 'children' of the frame, hence, we gotta .pack()

window.mainloop()'''
