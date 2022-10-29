import tkinter
from tkinter import messagebox, simpledialog

## Global variables
state = dict()      # Map from button to state, 'X', 'O', or ' '
button = dict()     # Map from position to button
#position = dict()  # Map from button to position; not needed
who = 'X'

# get_state and set_state used instead of dict assignments
# because changing state also has to change button appearance

def get_state(b):
    global state
    return state[b]

def set_state(b, letter):
    global state
    state[b] = letter
    b.config(text=letter)
    colors = {'X':'blue', 'O':'red', ' ':'black'}
    b.config(foreground=colors[letter])

## get_button and set_button not needed, no side effects
    
def initialize():
    global button, state, who
    who = 'X'
    for i in range(3):
        for j in range(3):
            button[i,j] = tkinter.Button(height=1,width=3,
                                         font=("Helvetica", "24"))
            button[i,j].bind('<ButtonRelease-1>', click)
            button[i,j].grid(row=i, column=j)
            set_state(button[i,j],' ')
    b = tkinter.Button(text='Reset',
                       command=reset)
    b.grid(row=3,column=1)

def reset():
    global button, who
    for i in range(3):
        for j in range(3):
            set_state(button[i,j], ' ')
    who = 'X'

def change_turn():
    global who
    if who == 'X':
        who = 'O'
    else:
        who = 'X'
        
def click(event):
    global button, who
    b = event.widget
    if get_state(b) == ' ':
        set_state(b, who)
        winner = check_win()
        if winner != None:
            messagebox.showinfo(winner + ' WINS!', winner + ' WINS!')
            reset()
        else:
            change_turn()

def s(i,j):  # Here just to make the next function a lot smaller
    global button
    return get_state(button[i,j])

def check_win():
    # Check for 'X' or 'O' win
    winner = None
    for i in range(3):
        if s(i,0) == s(i,1) == s(i,2):
            if s(i,0) != ' ':
                winner = s(i,0)
    for j in range(3):
        if s(0,j) == s(1,j) == s(2,j):
            if s(0,j) != ' ':
                winner = s(0,j)
    if s(0,0) == s(1,1) == s(2,2):
        if s(0,0) != ' ':
            winner = s(0,0)
    if s(0,2) == s(1,1) == s(2,0):
        if s(0,2) != ' ':
            winner = s(0,2)
    if winner != None:
        return winner
    # Check for cat's game, no remaining blanks
    winner = 'NOBODY'
    for i in range(3):
        for j in range(3):
            if s(i,j) == ' ':
                winner = None
    return winner

if __name__ == '__main__': 
    root = tkinter.Tk()
    n = simpledialog.askinteger(title='Number?', prompt='N:', initialvalue=42)
    print('Your number is %d' % n)
    root.title('TTT')
    root.resizable(0,0)
    initialize()
    tkinter.mainloop()
                                       
    
