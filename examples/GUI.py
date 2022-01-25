import tkinter as tk

window = tk.Tk() # object that is root window
window.title('TKInter Demo')

text = tk.Label(text = "Hello! What's your name?", foreground = 'white',
                background = 'blue', width = 30, height = 3) #Sequence doesn't matter, as soon as you call them correctly
text.pack() #Place text in the window

entry = tk.Entry(width = 30)
entry.pack()

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

#print(text.configure().keys()) #Shows you all library possibilities
window.mainloop() # event loop --> how it starts
