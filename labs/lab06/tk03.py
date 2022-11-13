import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Don't click the button!")
greeting.pack()

def click(event):
    greeting.config(text='You clicked the button!')

button = tk.Button(text="Click me!")
button.bind('<Button-1>', click)
button.pack()
                   
window.mainloop()
