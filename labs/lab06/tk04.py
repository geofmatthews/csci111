import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Don't click the button!",
                    font=("Helvetica", "36"))
greeting.pack()

def click(event):
    greeting.config(text='Mouse was at coordinates (%d, %d)'
                    % (event.x, event.y))

button = tk.Button(text="Click me!",
                   font=("Times", "52"))
button.bind('<Button-1>', click)
button.pack()
                   
window.mainloop()
