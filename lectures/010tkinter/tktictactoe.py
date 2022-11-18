import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.title('Tic Tac Toe')
root.resizable(0,0)

states = dict()

def get_state(b):
    global states
    return states[b]

def set_state(b, letter):
    global states
    colors = {'X':'blue','O':'red',' ':'black'}
    states[b] = letter
    b.config(text=letter)
    b.config(foreground=colors[letter])
    
def initialize_buttons():
    global buttons
    buttons = list(range(3))
    for i in range(3):
        buttons[i] = list(range(3))
        for j in range(3):
            buttons[i][j] = tkinter.Button(height=2,width=4,
                                           font=("Helvetica", "32"),
                                           command=lambda r=i,c=j:click(r,c))
            buttons[i][j].grid(row=i, column=j)
            set_state(buttons[i][j], ' ')
    b = tkinter.Button(text='Reset', command=reset)
    b.grid(row=3,column=1)

def reset():
    global buttons, who
    for i in range(3):
        for j in range(3):
            set_state(buttons[i][j], ' ')
    who = 'X'

def change_turn():
    global who
    if who == 'X':
        who = 'O'
    else:
        who = 'X'
        
def click(i,j):
    global buttons, who
    b = buttons[i][j]
    if get_state(b) == ' ':
        set_state(b, who)
        winner = check_win()
        if winner != None:
            messagebox.showinfo(winner + ' WINS!', winner + ' WINS!')
            reset()
        else:
            change_turn()

def s(i,j):
    global buttons
    return get_state(buttons[i][j])

def check_win():
    global buttons
    b = buttons
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
    winner = 'NOBODY'
    for i in range(3):
        for j in range(3):
            if s(i,j) == ' ':
                winner = None
    return winner

if __name__ == '__main__':   
    who = 'X'
    initialize_buttons()
    tkinter.mainloop()
                                       
    
