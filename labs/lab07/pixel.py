
def on_image(img, x, y):
    w,h = img.size
    return 0 <= x < w and 0 <= y < h

def norm(tupe):
    r,g,b = tupe
    return (r/255, g/255, b/255)

def denorm(tupe):
    r,g,b = tupe
    return (int(r*255), int(g*255), int(b*255))

def getpixel(img, x, y):
    return (norm(img.getpixel((x,y))))

def putpixel(img, x, y, color):
    img.putpixel((x,y), denorm(color))
