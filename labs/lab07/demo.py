"""
Image processing demo

Geoffrey Matthews 2022

"""

import os
##from imageprocessing import *
from separation import *
import tkinter
from tkinter import filedialog
from PIL import Image
    
try:
    from PIL import ImageTk
    have_ImageTk = True
except:
    have_ImageTk = False

def showInWindow(img, name):
    if not(have_ImageTk):
        img.show()
        return
    image = ImageTk.PhotoImage(img)
    newWindow = tkinter.Toplevel(root)
    newWindow.title(name)
    name = tkinter.Label(newWindow,
                         text=name)
    name.pack()
    label = tkinter.Label(newWindow,
                  image=image)
    label.pack()
    label.image = image
    newWindow.update()
    
def processFile(fname):  
    image = Image.open(fname).convert('RGB')
    width, height = image.size
    scale = 400/width
    image = image.resize((int(scale*width), int(scale*height)))
    name = os.path.basename(fname)
    showInWindow(image,name)
    showInWindow(red(image), 'red ' + name)
    showInWindow(green(image), 'green ' + name)
    showInWindow(blue(image), 'blue' + name)
##    showInWindow(grayscale(image), 'greyscale ' + name)
##    showInWindow(posterize(image), 'poster ' + name)
##    showInWindow(edge_detect(image), 'edge detect ' + name)
##    red(image).save('red.png')
##    green(image).save('green.png')
##    blue(image).save('blue.png')
##    grayscale(image).save('gray.png')
##    posterize(image).save('poster.png')
##    edge_detect(image).save('edge.png')
    
    
def openNewWindows():
    processFile(filedialog.askopenfilename(title='Open image'))
    
root = tkinter.Tk()
label = tkinter.Label(root,
              text='Image Processing Demo').pack()
btn = tkinter.Button(root,
             text='Load image',
             command=openNewWindows).pack()
tkinter.mainloop()
